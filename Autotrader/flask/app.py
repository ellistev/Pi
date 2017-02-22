from flask import Flask, request
from flask_restful import Resource, Api
from json import dumps
import boto3
import base64
import datetime
import hashlib
import hmac
import json
import urllib, cStringIO
from PIL import Image

app = Flask(__name__)
api = Api(app)


class Category(Resource):
    def get(self, photoUrl):
        client = boto3.client('rekognition')
        photohelperurl = 'http://az413908.vo.msecnd.net'
        underscore = '_'

        file = cStringIO.StringIO(urllib.urlopen(photohelperurl + underscore + photoUrl).read())
        img = Image.open(file)

        #with open('/datadrive/prepared_photos_lite/ford_fiesta/ford_fiesta_5031.jpg', 'rb') as source_image:
        #    source_bytes = source_image.read()

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
        return {'category': formatted_text} #[i[0] for i in query.cursor.fetchall()]}


class MakeModel(Resource):
    def get(self, photoUrl):
        #conn = e.connect()
        #query = conn.execute("select * from salaries where Department='%s'" % department_name.upper())
        # Query the result and get cursor.Dumping that data to a JSON is looked by extension
        result = {'makemodels': photoUrl} #[dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return result
        # We can have PUT,DELETE,POST here. But in our API GET implementation is sufficient


api.add_resource(Category, '/category/<string:photoUrl>')
api.add_resource(MakeModel, '/makemodel/<string:photoUrl>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)


import boto3
import base64
import datetime
import hashlib
import hmac
import json



print('Response body:\n{}'.format(formatted_text))

