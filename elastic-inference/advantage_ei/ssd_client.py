from __future__ import print_function

import grpc
import tensorflow as tf
from PIL import Image
import numpy as np
import time
import os
from tensorflow_serving.apis import predict_pb2
from tensorflow_serving.apis import prediction_service_pb2_grpc

tf.app.flags.DEFINE_string('server', 'localhost:9000',
                           'PredictionService host:port')
tf.app.flags.DEFINE_string('image', '', 'path to image in JPEG format')
FLAGS = tf.app.flags.FLAGS

coco_classes_txt = "https://raw.githubusercontent.com/amikelive/coco-labels/master/coco-labels-paper.txt"
local_coco_classes_txt = "/tmp/coco-labels-paper.txt"
# it's a file like object and works just like a file
os.system("curl -o %s -O %s"%(local_coco_classes_txt, coco_classes_txt))
NUM_PREDICTIONS = 20
with open(local_coco_classes_txt) as f:
  classes = ["No Class"] + [line.strip() for line in f.readlines()]


def main(_):
  channel = grpc.insecure_channel(FLAGS.server)
  stub = prediction_service_pb2_grpc.PredictionServiceStub(channel)

  # Send request
  with Image.open(FLAGS.image) as f:
    f.load()
    # See prediction_service.proto for gRPC request/response details.
    data = np.asarray(f)
    data = np.expand_dims(data, axis=0)

    request = predict_pb2.PredictRequest()
    request.model_spec.name = 'ssd'
    request.inputs['inputs'].CopyFrom(
        tf.contrib.util.make_tensor_proto(data, shape=data.shape))
    pred = None
    # Iterating over the predictions. The first inference request can take saveral seconds to complete
    for curpred in range(NUM_PREDICTIONS):
      if(curpred == 0):
        print("The first inference request loads the model into the accelerator and can take several seconds to complete. Please standby!")
      # Start the timer
      start = time.time()
      # This is where the inference actually happens
      ###pred = eia_predictor(ssd_resnet_input)
      result = stub.Predict(request, 60.0)  # 10 secs timeout
      print("Inference %d took %f seconds" % (curpred, time.time()-start))

    outputs = result.outputs
    detection_classes = outputs["detection_classes"]
    detection_classes = tf.make_ndarray(detection_classes)
    num_detections = int(tf.make_ndarray(outputs["num_detections"])[0])
    print("%d detection[s]" % (num_detections))
    class_label = [classes[int(x)]
                   for x in detection_classes[0][:num_detections]]
    print("SSD Prediction is ", class_label)


if __name__ == '__main__':
  tf.app.run()    