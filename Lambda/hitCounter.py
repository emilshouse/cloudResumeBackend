import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('webPageHits-prod')

# def createItems():
#     table.put_item(
#         Item={
#             'page_id': '1',
#             'hits': 1
#         }
#     )

def fetchFromDb():
    response = table.get_item(
	    Key={
    		    'page_id': '1'
            }
    )
    
    hit = response['Item']['hits']
    print(hit)
    return hit

def updateDb(lastCount):
    table.update_item(
       	Key={
                'page_id': '1'
            },
    	UpdateExpression='SET hits = :val1',
    	ExpressionAttributeValues={
        	':val1': lastCount + 1
    	}
    )


def lambda_handler(event, context):
    # TODO implement
    firstHit = fetchFromDb()
    print(f'First hit value is {firstHit}.')
    # createItems()
    lastHit = fetchFromDb()
    resp = {
        "statusCode": 200,
        "headers": {
            "Access-Control-Allow-Origin": "*",
        },
        "body": lastHit
    }
    updateDb(lastHit)
    
    return resp