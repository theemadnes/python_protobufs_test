import sample_payload_pb2
import string
import socket
import sys
from time import ctime

BUFSIZ = 1024 # bufsize = max receivable at once

SERVER_ADDRESS = ('', 9999)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(SERVER_ADDRESS)

while True:

    print("Listening")

    message, client_address = server_socket.recvfrom(BUFSIZ)
    if not message:
        break
    # convert message from seralized string to pb message
    print("Raw input received: " + message)
    sample_payload = sample_payload_pb2.SamplePayload()
    sample_payload.ParseFromString(message)
    print("Received: " + str(sample_payload) + " from: " + str(client_address))
    # server_socket.send("Accepted: " + message + " at " + ctime())
    server_socket.sendto('[%s] %s' % (ctime(), str(sample_payload)), client_address)

    # clear the protobuf conversion object
    # message_converted_to_protobuf = None

server_socket.close()
