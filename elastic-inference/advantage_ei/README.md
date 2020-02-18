# Elastic Inference Advantage Test

Attaching an accelerator dynamically to a deployment instance may sound limiting in terms of increasing the latency of response. Use the following set of instructions to verify that there is no increase in latency although the EI accelerator is network attached and not connected through PCIe bus.

For this EI Benchmark we will deploy the model to a `p2.xlarge` EC2 instance using tensorflow serving and compare it with a deployment on an `EI attached t3.xlarge` (you can choose a lower spec instance) instance.


## EC2 GPU Instance

Open a terminal and login to your EC2 GPU p2.xlarge instance. Make sure you used a Deep Learning AMI.
```
ssh -i somename.pem ubuntu@"Public DNS IPv4 address"
```
Pull the tf-serving-gpu docker image.
```
docker pull tensorflow/serving:latest-gpu
```
Download the TF model `ssd_resnet50_v1_coco`, 
```
curl -O https://s3-us-west-2.amazonaws.com/aws-tf-serving-ei-example/ssd_resnet.zip
```
extract it and store it in the folder `$PWD/tmp/`
Start the TF-serving service
```
CUDA_VISIBLE_DEVICES=0 nvidia-docker run -d -p 8500:8500 --mount type=bind,source=$PWD/tmp/ssd_resnet50_v1_coco/,target=/models/ssd -e MODEL_NAME=ssd -t tensorflow/serving:latest-gpu &
```
You can view the GPU usage by typing
```
nvidia-smi

+-----------------------------------------------------------------------------+
| NVIDIA-SMI 384.130                Driver Version: 384.130                   |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|===============================+======================+======================|
|   0  Tesla K80           On   | 00000000:00:1E.0 Off |                    0 |
| N/A   36C    P0    71W / 149W |    127MiB / 11439MiB |      0%      Default |
+-------------------------------+----------------------+----------------------+
                                                                               
+-----------------------------------------------------------------------------+
| Processes:                                                       GPU Memory |
|  GPU       PID   Type   Process name                             Usage      |
|=============================================================================|
|    0      2384      C   tensorflow_model_server                      116MiB |
+-----------------------------------------------------------------------------+
```
Download a query image `3dogs.jpg`
```
curl -O https://raw.githubusercontent.com/awslabs/mxnet-model-server/master/docs/images/3dogs.jpg
```

Activate the tensorflow virtual environment that has tensorflow serving installed and query the service using the client code `ssd_client.py` in this repo
```
source activate tensorflow_p36
python ssd_client.py --image=3dogs.jpg  --server=localhost:8500
```
The output shows the inference latency. Feel free to modify and play around with the client code. 


## EC2 CPU Instance + EI accelerator

Launch an EC2 CPU instance like `t3.xlarge` with a Deep Learning AMI so that the virtual environments come pre-packaged.
Attach an EI accelerator when configuring the instance.
Open a terminal and login to your EC2 CPU instance. Make sure you used a Deep Learning AMI.
```
ssh -i somename.pem ubuntu@"Public DNS IPv4 address"
```
Next, activate the `amazonei_tensorflow_p36` virtual environment
```
source activate amazonei_tensorflow_p36
```
Download the TF model `ssd_resnet50_v1_coco`, 
```
curl -O https://s3-us-west-2.amazonaws.com/aws-tf-serving-ei-example/ssd_resnet.zip
```
extract it and store it in the folder `$PWD/tmp/`
Download a query image `3dogs.jpg`
```
curl -O https://raw.githubusercontent.com/awslabs/mxnet-model-server/master/docs/images/3dogs.jpg
```
Next, start the TF-serving service (in the background)
```
amazonei_tensorflow_model_server --model_name=ssdresnet --model_base_path=$PWD/tmp/ssd_resnet50_v1_coco --port=9000
source activate amazonei_tensorflow_p36 &
```
Query the service using the `ssd_resnet_client.py` client code provided
```
python ssd_ei_client.py --server=localhost:9000 --image 3dogs.jpg
```
The output shows the inference latency.

## Conclusion

From the above comparison you should be able to see that the inference latency for EI+CPU EC2 instance has no difference with the inference latency using a GPU instance, thus reducing the deployment cost significantly.
