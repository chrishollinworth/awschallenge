from decimal import Decimal
import json
import boto3


def load_phonenumbers(phonenumbers, local):
    if local is True:
        dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
    else:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('PhoneNumbers')
    for phonenumber in phonenumbers:
        number = phonenumber['phonenumber']
        name = phonenumber['name']
        print("Adding phonenumber:", number, name)
        table.put_item(Item=phonenumber)


if __name__ == '__main__':
    with open("phonenumberdata.json") as json_file:
        phonenumber_list = json.load(json_file, parse_float=Decimal)
    load_phonenumbers(phonenumber_list, False)