import json
import boto3
import os
from botocore.exceptions import NoCredentialsError

s3_client = boto3.client('s3')
comprehend_client = boto3.client('comprehend')
sqs_client = boto3.client('sqs')

def lambda_handler(event, context):
    try:
        print("Received event:", json.dumps(event, indent=2))

        # Assuming your SQS message contains the S3 object key
        if 'Records' in event and event['Records']:
            s3_object_key = json.loads(event['Records'][0]['body'])['Records'][0]['s3']['object']['key']
            print("S3 Object Key:", s3_object_key)

            # ... rest of your code ...

            return {
                'statusCode': 200,
                'body': json.dumps('Text analysis completed and result saved to S3!')
            }
        else:
            return {
                'statusCode': 400,
                'body': json.dumps('Error: Invalid event structure. Missing or empty Records field.')
            }

    except NoCredentialsError:
        return {
            'statusCode': 500,
            'body': json.dumps('Error: AWS credentials not available.')
        }
