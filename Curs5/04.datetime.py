from datetime import datetime
import time

start_datetime = datetime.now()
print(start_datetime)

start_time = time.time()
print(start_time) # Nr de secunde la 1 ianuarie 1970

time.sleep(5)

stop_datetime = datetime.now()
print(stop_datetime)

stop_time = time.time()
print(stop_time) # Nr de secunde la 1 ianuarie 1970

print()

print("delta datetime", stop_datetime - start_datetime )
print("delta time", stop_time -  start_time)

