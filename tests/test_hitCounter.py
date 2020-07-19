import unittest
from Lambda import hitCounter
#import fetchFromDb from hitCounter.py 
#import updateDb from hitCounter.py
from moto import mock_dynamodb
import boto3


@mock_dynamodb
def test_fetchFromDb():
    dynamodb = boto3.resource('dynamodbTest')
    table = dynamodb.create_table(
    TableName='webPageHits-prodTest',
    KeySchema=[
        {
            'AttributeName': 'page_id',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'hits',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'page_id',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'hits',
            'AttributeType': 'N'
        },
    ]
    )
    table.update_item(
       	Key={
                'page_id': '1'
            },
    	UpdateExpression='SET hits = :val1',
    	ExpressionAttributeValues={
        	':val1': lastCount + 1
    	}
    )
    print(table.item_count)
    answer = fetchFromDb()
    assert answer == 1

def test_updateDB():
    sampleValue = 1
    updateDb(sampleValue)
    answer = fetchFromDb()
    assert answer == sampleValue + 1

if __name__ == '__main__':
    unittest.main()