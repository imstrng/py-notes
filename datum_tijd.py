import datetime
import time

stamp = "{:%Y-%m-%d %H:%M:%S}".format(datetime.datetime.today())
print(stamp)
print(int(time.time()))