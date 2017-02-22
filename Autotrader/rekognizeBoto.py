import boto3
import base64
import datetime
import hashlib
import hmac
import json

client = boto3.client('rekognition')

with open('/datadrive/prepared_photos_lite/ford_fiesta/ford_fiesta_4.jpg', 'rb') as source_image:
    source_bytes = source_image.read()

response = client.detect_labels(
    Image={
        'Bytes': source_bytes
    },
    MaxLabels=10,
    MinConfidence=0.5
)

#jsonResponse = json.load(response)
labels = response["Labels"]
formatted_text = json.dumps(labels, indent=4, sort_keys=True)

print('Response body:\n{}'.format(formatted_text))
