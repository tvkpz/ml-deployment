# ml-deployment

Code repository that was started for ML Innovate 2020 on the topic of ML Deployment. Watch out for this repo as more useful code gets added to this repo to help developers deploy their ML Solutions on AWS.

Most of the code in this repository is adapted from the [aws-sagemeaker-examples](https://github.com/awslabs/amazon-sagemaker-examples) repo.

The topics covered are:

- [Resource Profiling using CloudWatch Metrics](resource-profiling)
- [Load Testing Deployment Endpoint using Serverless-Artillery](loadTesting)
- [Offline Deployment Using Batch Transform](batch-transform)
- [Online Deployment Using Sagemaker Hosting](hosting)
- [Using Sagemaker Inference Pipelines to string together Pre, Inference, Post-processing steps as a single deployment](inference-pipelines)
- [Sagemaker Multi-model Deployment Endpoint](multi-model)
- [Using Elastic Inference for Flexibly adding GPU accelerators](elastic-inference)
- [Preparing Models in different frameworks for different target hardware using Sagemaker Neo](neo)
- [Deploying using tensorflow serving](tf-serving)


## Things to To

While the above topics have some meterials and on going topics, expect more example code on the following topics to be included:

- Deployment in K8s: [EKS](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html) | [EKS-docs](https://github.com/awsdocs/amazon-eks-user-guide/blob/master/doc_source/doc-history.md) | [Sagemaker Operators for K8s](https://github.com/aws/amazon-sagemaker-operator-for-k8s) | [EKS Workshop](https://eksworkshop.com/)
- Model Governance: [Version Code | Version Data | Version Model](https://d1.awsstatic.com/whitepapers/Deep_Learning_on_AWS.pdf)
- ML Deployment Workflows: [Airflow](https://sagemaker.readthedocs.io/en/stable/using_workflow.html) | [Step Function](https://github.com/awslabs/amazon-sagemaker-examples/tree/master/step-functions-data-science-sdk) | [Kubeflow](https://github.com/kubeflow/pipelines/tree/master/components/aws/sagemaker) | [Docs](https://d1.awsstatic.com/whitepapers/Deep_Learning_on_AWS.pdf)
- Model Monitoring: [Doc](https://docs.aws.amazon.com/sagemaker/latest/dg/model-monitor.html) | [Deequ](https://github.com/awslabs/deequ) | [Code](https://github.com/awslabs/amazon-sagemaker-examples/tree/master/sagemaker_model_monitor)
- Automated Deployment: [Example Code](https://github.com/aws-samples/amazon-sagemaker-custom-object-detection/blob/master/sam-template.yaml) | [More Code](https://github.com/aws-samples/amazon-sagemaker-to-aws-lambda-pipeline-blogpost/) | [Blogs](https://aws.amazon.com/blogs/machine-learning/automated-and-continuous-deployment-of-amazon-sagemaker-models-with-aws-step-functions/)
- Adversarial Attacks: [Docs](https://openai.com/blog/adversarial-example-research/) | [Books](https://www.amazon.com/Strengthening-Deep-Neural-Networks-Susceptible/dp/1492044954) | [Stealing ML Models](https://www.usenix.org/system/files/conference/usenixsecurity16/sec16_paper_tramer.pdf) | [Membership Inference Attacks](https://github.com/spring-epfl/mia)
- MLOps: [Workshop](https://github.com/awslabs/amazon-sagemaker-mlops-workshop)

Feel free to raise requests to cover topics that you would like covered with code.



