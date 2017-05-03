import time, redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)
p = r.pubsub()
p.subscribe('ch1', 'ch2')

while True:
    message = p.get_message()
    if message:
        print(message)
    time.sleep(0.001)  # be nice to the system :)
