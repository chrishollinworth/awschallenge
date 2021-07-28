import json

import boto3
import pytest
from backend.get_phone_numbers import app
from moto import mock_dynamodb2

TABLE_NAME = "PhoneNumbers"
REGION = 'us-east-1'


@pytest.fixture
def use_moto():
    @mock_dynamodb2
    def dynamodb_client():
        dynamodb = boto3.resource('dynamodb', region_name=REGION)

        # Create the table
        dynamodb.create_table(
            TableName=TABLE_NAME,
            KeySchema=[
                {
                    'AttributeName': 'phonenumber',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'name',
                    'KeyType': 'RANGE'
                },
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'phonenumber',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'name',
                    'AttributeType': 'S'
                },
            ],
            BillingMode='PAY_PER_REQUEST'
        )
        return dynamodb
    return dynamodb_client

@mock_dynamodb2
def test_handler_for_no_records(use_moto):
    use_moto()
    event = {}

    return_data = app.lambda_handler(event, "")
    assert return_data['statusCode'] == 200
    assert return_data['body'] == '[]'


@mock_dynamodb2
def test_handler_for_status_ok(use_moto):
    use_moto()
    table = boto3.resource('dynamodb', region_name=REGION).Table(TABLE_NAME)
    table.put_item(
        Item={
            'phonenumber': "011111111111",
            'name': "bob",
        }
    )

    event = {
 	"httpMethod": "GET",
    "pathParameters": '',
    }

    return_data = app.lambda_handler(event, "")
    body = json.loads(return_data['body'])

    assert return_data['statusCode'] == 200
    assert body[0]['phonenumber'] == '011111111111'
    assert body[0]['name'] == 'bob'
