## Testing out ProtoBufs in Python

Learning about ProtoBufs, so idea for this is to create a client & server where the client connects to a socket and sends messages, serialized by ProtoBufs, to a server. The payload would be modeled in JSON like:

`{
  'userName': 'alex',
  'userAge': 1000,
  'randomString': 'RANDOM_STRING',
  'randomInt': 124567890
}`

The client will send the payload, and the server will print the output to stdout.

Not sure how many of these are needed but I used the following tools:
- protobufs compiler (via brew on Mac)
- pip install google
- pip install protobufs
