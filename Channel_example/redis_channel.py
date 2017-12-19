"""Test Redis channels.
"""
import time
import redis


r = redis.StrictRedis(host='localhost', port=6379, db=0)
#p = r.pubsub(ignore_subscribe_messages=True)
p = r.pubsub(ignore_subscribe_messages=False)
p.subscribe('my-channel')
print(p.get_message())  # hides the subscribe message and returns None

try:
    while True:
        message = p.get_message()
        if message:
            print(message)
            print(message['data'])
        time.sleep(0.001)  # be nice to the system :)
except KeyboardInterrupt:
    p.close()