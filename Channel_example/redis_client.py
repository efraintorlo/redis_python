import redis
import time 
import datetime as dt 

r = redis.StrictRedis(host='localhost', port=6379, db=0)

r.publish('my-channel', dt.datetime.now().time())

#p.get_message()