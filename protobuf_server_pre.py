# pre implementing protobufs

import sample_payload_pb2
import random
import string
import socket
import sys
import struct
from time import ctime

BUFSIZ = 1024 # bufsize = max receivable at once

def random_string_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

def random_int_generator():
    return random.randint(0, 999999)

'''
# populate payload values
payload = sample_payload_pb2.SamplePayload()
payload.userName = 'myName'
payload.userAge = 100
payload.randomString = random_string_generator()
payload.randomInt = random_int_generator()
'''
SERVER_ADDRESS = ('', 9999)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind(SERVER_ADDRESS)

while True:

    print("Listening")

    message, client_address = server_socket.recvfrom(BUFSIZ)
    if not message:
        break
    print("Received: " + message + " from: " + str(client_address))
    # server_socket.send("Accepted: " + message + " at " + ctime())
    server_socket.sendto('[%s] %s' % (ctime(), message), client_address)

server_socket.close()
