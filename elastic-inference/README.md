
# Elastic Inference

Elastic Inference (EI) service allows you to flexibly add a right sized GPU accelerator to your deployment instances for model inference workloads that need the use of GPUs.

The following topics are covered:

- [Verify advantage of Elastic Inference](advantage_ei) This repo details a series of steps you can try out to verify how elastic inference, although network attached on demand, gives the same latency performance that a GPU instance gives while allowing right sizing and reducing cost of deployment.
- [MXNet with EI](mxnet_ei) Contains code that demonstrates how to enable and use Amazon Elastic Inference with our predefined SageMaker MXNet containers.
- [ONNX Deployment with EI](mxnet_onnx_eia) Amazon EI provides support for Apache MXNet, TensorFlow and ONNX models. The Open Neural Network Exchange (ONNX) is an open standard format for deep learning models that enables interoperability between deep learning frameworks such as Apache MXNet, Caffe2, Microsoft Cognitive Toolkit(CNTK), PyTorch and more. This means that you can use any of these frameworks to train the model, export these pretrained models in ONNX format and then import them in MXNet for inference.