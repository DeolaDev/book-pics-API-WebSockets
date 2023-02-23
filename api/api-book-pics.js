//Web based API to format messages received using the TWILIO API before the data is fed to the Book-pics App
exports.handler = async function (context, event, callback) {
  const client = context.getTwilioClient();
  const gallery = [];
  const messages = await client.messages.list({
    to: context.MY_TWILIO_PHONE_NUM,
  });
  const response = new Twilio.Response();

  // Setting the CORS headers to allow for an error-free HTTP request
  response.appendHeader("Access-Control-Allow-Origin", "*");
  response.appendHeader("Access-Control-Allow-Methods", "OPTIONS, POST, GET");
  response.appendHeader("Content-Type", "application/json");

  //loop through messages and add attached pictures to the gallery array
  for (const message of messages) {
    const pics = await message.media().list();
    for (const pic of pics) {
      gallery.push({
        src: "https://api.twilio.com" + pic.uri.replace(".json", ""), // return pic uri with no extension
        description: message.body,
        alt: message.body,
        thumbnailWidth: "150px",
      });
    }
  }

  // Set the response body to the gallery, so that an array of gallery of pictures submitted in JSON format is returned
  response.setBody(gallery);

  return callback(null, response);
};
