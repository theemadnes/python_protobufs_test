# pre implementing protobufs

import sample_payload_pb2
import random
import string
import socket
import sys
import struct

BUFSIZ = 1024 # bufsize = max receivable at once

SERVER_ADDRESS = ('localhost', 9999)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# client_socket.connect(address)

messages = ["one", "two", "three", "four"]
reply = ''

for s in messages:

    client_socket.sendto(s, SERVER_ADDRESS)
    reply, server_address = client_socket.recvfrom(BUFSIZ)

    if not reply:
        break

    print(reply + " from: " + str(server_address))
