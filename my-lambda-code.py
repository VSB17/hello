import json
import boto3

sqs = boto3.client('sqs')
queue_url = 'YOUR_SQS_QUEUE_URL'  # Replace with your SQS queue URL

def lambda_handler(event, context):
    try:
        # Extract data from the API Gateway event
        data = json.loads(event['body'])

        # Send message to SQS
        response = sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=json.dumps(data)
        )

        return {
            'statusCode': 200,
            'body': json.dumps('Message sent to SQS successfully!')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }
