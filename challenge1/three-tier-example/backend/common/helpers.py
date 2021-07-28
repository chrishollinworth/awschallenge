import json
import os

import boto3

REGION = os.environ.get('REGION', 'us-east-1')
DOMAIN_NAME = os.environ.get("DOMAIN_NAME", "*")
AWS_ENVIRONMENT = os.environ.get('AWSENV', 'AWS')

def check_request(message,allowed_method):
    """
    Returns 400 if message does not validate with correct HTTP Method
    """
    if ('pathParameters' not in message or
            message['httpMethod'] != allowed_method):
        
        return jsonresponse('msg\': \'Bad Request',400) 
        
def get_dynamodb_table(table_name):
    if AWS_ENVIRONMENT == 'AWS_SAM_LOCAL':
        dynamodb_table = boto3.resource(
            'dynamodb',
            endpoint_url='http://dynamodb:8000'
        )
    else:
        dynamodb_table = boto3.resource(
            'dynamodb',
            region_name=REGION
        )

    return dynamodb_table.Table(table_name)

def jsonresponse(message, status_code=200):
    """
    Return a properly formatted response for AWS Lambda proxy integration
    including CORS
    """
    return {
        "statusCode": status_code,
        "headers": {
            "Access-Control-Allow-Headers": "Content-Type,X-Amz-Date,Authorization,X-Api-Key,x-requested-with",
            "Access-Control-Allow-Origin": "{}".format(DOMAIN_NAME),
            "Access-Control-Allow-Methods": "POST,GET,OPTIONS"
        },
        "body": json.dumps(message)
    }
