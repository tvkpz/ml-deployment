# Load Testing

Use serverless-artillery to perform load testing of your deployment.

## Installing on local machine
You can install serverless-artillery on your local machine as follows.
### Prerequisite
#### 1. Node JS
Before installing serverless-artillery, install Node JS from https://nodejs.org/en/download/ or with your operating system’s package manager. You can install the latest LTS version. We support any version higher than maintenance LTS (v8+).
#### 2. Serverless Framework CLI
Before installing serverless-artillery, install Serverless Framework CLI (a.k.a. Serverless) (v1.38+). It should be either installed globally or available in the local node_modules. To install globally use the following command.
```
npm install -g serverless
```
#### 3. Setup your AWS Profile
Instructions for setting up your AWS profile can be found [here](https://github.com/Nordstrom/serverless-artillery-workshop/tree/master/Lesson0%20-%20Before%20the%20workshop) and [here](https://github.com/Nordstrom/serverless-artillery-workshop/blob/master/Lesson0%20-%20Before%20the%20workshop/LEAST-PERMISSIONS-USER.md)

### Installing serverless-artillery
Now you can install serverless-artillery on your local machine using the following command.
```
npm install -g serverless-artillery
```
To check that the installation succeeded, run:
```
slsart --version
```
You should see serverless-artillery print its version if the installation has been successful.

### Load Testing using serverless-artillery
Configure serverless-artillery. This command creates a local copy of the deployment assets for modification and deployment of serverless-artillery resources:

```
slsart configure
```

Modify `runtime: XX` to current value of `nodejs12.x` in `serverless.yml`. Create a Lambda function for load testing:

```
slsart deploy --stage <your-unique-stage-name>
```

Create a local serverless-artillery script that you can customize for your load requirements:

```
slsart script
```
This command creates a file named script.yml in your local directory. Open the file for editing and add the target URL.

Please refer to [AWS Machine Learning Blog](https://aws.amazon.com/blogs/machine-learning/load-test-and-optimize-an-amazon-sagemaker-endpoint-using-automatic-scaling/) for more details.

Next, you can run the load testing 

```
slsart invoke --stage <your-unique-stage-name>
```

To remove the deployment use

```
slsart remove --stage <your-unique-stage-name>
```
