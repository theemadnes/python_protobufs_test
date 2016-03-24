import sample_payload_pb2
import random
import string

def random_string_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

def random_int_generator():
    return random.randint(0, 999999)

# populate payload values
payload = sample_payload_pb2.SamplePayload()
payload.userName = 'myName'
payload.userAge = 100
payload.randomString = random_string_generator()
payload.randomInt = random_int_generator()
