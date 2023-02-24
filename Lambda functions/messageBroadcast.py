#This lambda function is invoked when a new message is sent to my Twilio phone number, 
# and Twilio sends an HTTP request to the webhook configured in my HTTP API Gateway
# This broadcast function then retrieves all active connection IDs from the database.
# and sends a message to each active connection ID 
# to execute a fetch command to the Twilio API to retrieve the updated data.

import json
import boto3

api_client = boto3.client('apigatewaymanagementapi', endpoint_url='MY_API_GATEWAY_WEBSOCKET_URL')
dynamodb_client = boto3.resource("dynamodb")
connectionId_table = dynamodb_client.Table("bookPics-ConnectionIDs")
connection_ids = connectionId_table.scan()['Items']

def lambda_handler(event, context):
    data = {'message': 'New data is available'}
   
    for connection_id in connection_ids:
        try:
            api_client.post_to_connection(Data=json.dumps(data), ConnectionId=connection_id['connection_id'])
        except:
            pass
  
    return {
        'statusCode': 200,
        'body': 'Data sent successfully'
    }