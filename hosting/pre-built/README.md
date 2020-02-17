# Sagemaker Hosting: Pre-built First Party Containers

For using first party Sagemaker images you just need to point to the right image in ECR. Use `1` as the latest stable version to use. Use `latest` for the latest built.

```
from sagemaker.amazon.amazon_estimator import get_image_uri
container = get_image_uri(boto3.Session().region_name, 'xgboost')

primary_container = {
    'Image': container, 
    'ModelDataUrl': model_url, #model in S3 bucket
}

create_model_response2 = sm_client.create_model(
    ModelName = model_name,
    ExecutionRoleArn = role,
    PrimaryContainer = primary_container)
```