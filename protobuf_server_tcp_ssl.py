import sample_payload_pb2
import string
import socket
import sys
from time import ctime
import ssl

BUFSIZ = 1024 # bufsize = max receivable at once

SERVER_ADDRESS = ('', 9999)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
wrapped_server_socket = ssl.wrap_socket(server_socket, ssl_version=ssl.PROTOCOL_TLSv1, ciphers="ADH-AES256-SHA")
wrapped_server_socket.bind(SERVER_ADDRESS)
wrapped_server_socket.listen(5)

while True:

    print("Listening for secure TCP session")

    client_socket, client_address = wrapped_server_socket.accept() # allow connection
    print("Secure connection established from: " + str(client_address))

    # pass off to client socket
    while True:

        message = client_socket.recv(BUFSIZ)
        if not message:
            break
        # convert message from seralized string to pb message
        print("Raw input received: " + message)
        sample_payload = sample_payload_pb2.SamplePayload()
        sample_payload.ParseFromString(message)
        print("Received: " + str(sample_payload) + " from: " + str(client_address))
        # server_socket.send("Accepted: " + message + " at " + ctime())
        client_socket.send('[%s] %s' % (ctime(), str(sample_payload)))
    client_socket.close()

wrapped_server_socket.close()
