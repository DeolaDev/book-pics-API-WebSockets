#This lambda function is triggered when a web socket connection is closed 
# The coneection Id is purged from the database

import boto3

api_client = boto3.client('apigatewaymanagementapi', endpoint_url='MY_API_GATEWAY_WEBSOCKET_URL')
dynamodb_client = boto3.resource("dynamodb")
connectionId_table = dynamodb_client.Table("bookPics-ConnectionIDs")

def lambda_handler(event, context):
    connection_id = event['requestContext']['connectionId']
   
    # remove entry from dynamodb
    connectionId_table.delete_item(
        Key = {
            "connection_id" : connection_id
        }
    )
  
    return {
        'statusCode': 200
        
    }
    