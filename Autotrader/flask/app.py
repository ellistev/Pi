from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
import boto3
import base64
import datetime
import hashlib
import hmac
import json
import urllib
from PIL import Image
from random import randrange, uniform
import numpy as np
import tensorflow as tf

app = Flask(__name__)
api = Api(app)

#imagePath = '/datadrive/prepared_photos/lexus_is_250/lexus_is_250_1674.jpg'
modelFullPath = '/datadrive/tmp/output_graph.pb'
labelsFullPath = '/datadrive/tmp/output_labels.txt'

def create_graph():
    """Creates a graph from saved GraphDef file and returns a saver."""
    # Creates graph from saved graph_def.pb.
    with tf.gfile.FastGFile(modelFullPath, 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')

def run_inference_on_image(imagePath):
    answer = None

    if not tf.gfile.Exists(imagePath):
        tf.logging.fatal('File does not exist %s', imagePath)
        return answer

    image_data = tf.gfile.FastGFile(imagePath, 'rb').read()

    # Creates graph from saved GraphDef.
    create_graph()

    with tf.Session() as sess:

        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
        predictions = sess.run(softmax_tensor,
                               {'DecodeJpeg/contents:0': image_data})
        predictions = np.squeeze(predictions)

        top_k = predictions.argsort()[-5:][::-1]  # Getting top 5 predictions
        f = open(labelsFullPath, 'rb')
        lines = f.readlines()
        labels = [str(w).replace("\n", "") for w in lines]
        for node_id in top_k:
            human_string = labels[node_id]
            score = predictions[node_id]
            print('%s (score = %.5f)' % (human_string, score))

        answer = labels[top_k[0]]
        return answer

class Category(Resource):
    def post(self):
        client = boto3.client('rekognition')
        photohelperurl = 'http://az413908.vo.msecnd.net'
        underscore = '_'
        data = request.data
        dataDict = json.loads(data)
        photoUrl = dataDict["photoUrl"]
        print(photoUrl)

        randomNameForFile = randrange(0, 9999999)
        imagePath = '/datadrive/uploadedPhotos/{0}.jpg'.format(randomNameForFile)
        source_image = urllib.urlopen(photohelperurl + "/" + photoUrl, imagePath)
        img = source_image.read()

        response = client.detect_labels(
            Image={
                'Bytes': img
            },
            MaxLabels=10,
            MinConfidence=0.5
        )

        # jsonResponse = json.load(response)
        labels = response["Labels"]
        formatted_text = json.dumps(labels, indent=4, sort_keys=True)

        mlResult = run_inference_on_image(imagePath)

        return {'mlResult': mlResult, 'category': labels} #[i[0] for i in query.cursor.fetchall()]}


class MakeModel(Resource):
    def post(self, photoUrl):
        #conn = e.connect()
        #query = conn.execute("select * from salaries where Department='%s'" % department_name.upper())
        # Query the result and get cursor.Dumping that data to a JSON is looked by extension
        result = {'makemodels': photoUrl} #[dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return result
        # We can have PUT,DELETE,POST here. But in our API GET implementation is sufficient


api.add_resource(Category, '/category')
api.add_resource(MakeModel, '/makemodel/<string:photoUrl>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)


