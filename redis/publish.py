import time, redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)
          
for i in range(10):
    r.publish('ch1', 'some data '+str(i))
    time.sleep(0.4)
print('done')