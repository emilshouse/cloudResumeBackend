import pytest
import os
from moto import mock_dynamodb2
import boto3

# Dummy environment variables. 
os.environ['AWS_ACCESS_KEY_ID'] = 'testing'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'testing'
os.environ['AWS_SECURITY_TOKEN'] = 'testing'
os.environ['AWS_SESSION_TOKEN'] = 'testing'

def fetchFromDb(table):
    response = table.get_item(
	    Key={
    		    'page_id':'1'
            }
    )
    
    hit = response['Item']['hits']
    return hit

@mock_dynamodb2
def test_fetchFromDb():
    dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    table = dynamodb.create_table(
    TableName='webPageHits-prodTest',
    KeySchema=[
        {
            'AttributeName': 'page_id',
            'KeyType': 'HASH'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'page_id',
            'AttributeType': 'S'
        }
    ]
    )
    table.update_item(
        Key={
                'page_id': '1'
            },
        UpdateExpression='SET hits = :val1',
	ExpressionAttributeValues={
        	':val1': 1
    	 }
     )
    print( table.item_count)
    answer = fetchFromDb(table)
    assert answer == 1, "Should be 1"

