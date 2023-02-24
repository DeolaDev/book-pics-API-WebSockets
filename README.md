# This is an updated version of my single page 'Book Pictures' application

In version one and this, users can send a text to my TWILIO number with a picture of their favourite book and have it displayed on the webpage.

This version builds on that by implementing a solution to automatically refresh the page when a new message is sent to my TWILIO number

## For this, in addition to implementing and consuming APIs, I also implemented and used DynamoDB, web hooks and web sockets to allow my front-end to automatically reload when a new picture message is received

# IMPLEMENTATION PLAN

- A Web socket hosted on AWS API Gateway with a $connect and $disconnect route.
- When a client connects to the web socket, the $connect route triggers the associated Lambda function
- The connect Lambda function takes the connectionId of the client and stores it in a DynamoDB table
- When a client disconnects from the web socket, the $disconnect route triggers the associated Lambda function
- The disconnect Lambda function removes the connectionId of the client from the DynamoDB table (This is to keep track of all connected clients)
- Also created a webhook configured in my HTTP API Gateway
- This webhook is triggered when a new message is sent to my Twilio phone number
- The webhook in turn triggers another Lambda function called messageBroadcast
- This messageBroadcast Lambda function sends a "New data available" message to all connected clients
- When a client receives the message, it updates the front end and loads the new image automatically

# THE EVENT FLOW

- Twilio receives a message sent to my Twilio phone number.
- Twilio sends an HTTP request to the webhook configured in my HTTP API Gateway.
- The HTTP API Gateway forwards the request to my broadcast function.
- The broadcast function retrieves all active connection IDs from the database.
- The broadcast function sends a message to each active connection ID using the Amazon API Gateway Management API.
- The clients receive the message and execute a fetch command to the Twilio API to retrieve the updated data.
- The Twilio API returns the updated data to the client.
- The Vue.js app displays the updated data on the frontend.

\*\* Hosted with Netlify -> https://book-pics-v2.netlify.app/

### Video Demo shows my phone screen sending picture messages, and my Vue.Js app receiving and displaying a "New data is available" message and then loads and displays the new picture on the page automatically.
