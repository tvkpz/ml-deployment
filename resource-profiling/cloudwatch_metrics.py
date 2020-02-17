
# Example starter code to retrieve Sagemaker Endpoint CloudWatch metrics programmatically

import boto3
from datetime import datetime
from datetime import timedelta
from pytz import timezone
import sagemaker as sm

def getresource_metrics(metric_name, region):
    tz = timezone('Asia/Singapore')
    delta = timedelta(days=0, hours=0, minutes=10, seconds=60)
    cloudwatch = boto3.client('cloudwatch', region_name=region)
    response = cloudwatch.get_metric_data(
        MetricDataQueries=[{
                'Id': 'memcheck_1',
                'MetricStat': {
                    'Metric': {
                        'Namespace': '/aws/sagemaker/Endpoints',
                        'MetricName': metric_name,
                        'Dimensions': [
                        {
                            'Name': 'EndpointName',
                            'Value': 'autopilot-test-endpoint', #name of endpoint
                        },
                        {
                            'Name': 'VariantName',
                            'Value': 'sg-autopilot-test-1', #name of variant
                        }
                        ],
                    },
                    'Period': 60,
                    'Stat': 'Maximum',
                },
                'ReturnData': True,
                }],
        StartTime=datetime.now(tz)-delta,
        EndTime=datetime.now(tz),
        ScanBy='TimestampDescending')
    
    return response['MetricDataResults'][0]['Values']

sess = sm.Session()
account = sess.boto_session.client('sts').get_caller_identity()['Account']
region = sess.boto_session.region_name

print('MemoryUtilization = ', getresource_metrics('MemoryUtilization', region))
print('CPUUtilization = ', getresource_metrics('CPUUtilization', region))
print('DiskUtilization = ', getresource_metrics('DiskUtilization', region))