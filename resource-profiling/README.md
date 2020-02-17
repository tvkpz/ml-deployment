# Profiling

Profiling is an important step in verifying the resource needs for deployment and right sizing of resources. Note that resource usage in production is not just about loading a model and serving requests. It also involves many other processes that are running in parallel in the same instance to monitor and manage the deployment. 

When you deploy on AWS all the resource usage logs and metrics and available through CloudWatch. You need a programmatic way of getting those logs and metric information to automate decision taking. This repository collects the relevant materials you would need for doing just that.

This repo is WIP and more code and relevant documentation will be added over time.

`cloudwatch_metrics.py` is an example code that demonstrates how to programmatically retireve CloudWatch Metrics.


