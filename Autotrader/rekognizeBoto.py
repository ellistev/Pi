import boto3
import base64
import datetime
import hashlib
import hmac
import json

client = boto3.client('rekognition')

with open('/datadrive/prepared_photos_lite/ford_fiesta/ford_fiesta_10.jpg', 'rb') as source_image:
    source_bytes = base64.b64encode(source_image.read())

response = client.detect_labels(
    Image={
        'Bytes': source_bytes
    },
    MaxLabels=10,
    MinConfidence=0.5
)

formatted_text = json.dumps(json.loads(response.text), indent=4, sort_keys=True)

print('Response code: {}\n'.format(response.status_code))
print('Response body:\n{}'.format(formatted_text))
