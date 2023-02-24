#This lambda function is triggered when a web socket connection is established. 
# For each connection, the connectionID is extracted and stored in DynamoDB to be used by my messageBroadcast function when a message needs to be sent to all connected clients
# The disconnect function would remove a closed connection's id

import boto3

api_client = boto3.client('apigatewaymanagementapi', endpoint_url='API_GATEWAY_WEBSOCKET_URL')
dynamodb_client = boto3.resource("dynamodb")
connectionId_table = dynamodb_client.Table("bookPics-ConnectionIDs")

def lambda_handler(event, context):
    connection_id = event['requestContext']['connectionId']
   
    
    # add entry to dynamodb
    connectionId_table.put_item(
        Item = {
            "connection_id" : connection_id
        }
    )
    
    return {
        'statusCode': 200,
        
    }