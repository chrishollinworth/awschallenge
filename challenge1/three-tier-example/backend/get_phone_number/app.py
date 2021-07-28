import json
import os

import botocore
from boto3.dynamodb.conditions import Key
from helpers import check_request, get_dynamodb_table, jsonresponse

TABLE_NAME = os.environ.get('TABLE', 'PhoneNumbers')
def lambda_handler(message, context):

    try:
        check_request(message,'GET')

        table = get_dynamodb_table(TABLE_NAME)
        phonenumber = message['pathParameters']['id']

        response = table.query(
            KeyConditionExpression=Key('phonenumber').eq(phonenumber)
        )

        return jsonresponse(response['Items'], 200)

    except botocore.exceptions.ClientError as error:
        return jsonresponse(error, 500) 
