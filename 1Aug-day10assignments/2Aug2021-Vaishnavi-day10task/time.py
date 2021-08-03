import time
current_time=time.localtime()
# print(current_time)
current_clock_time=time.strftime("%H:%M:%S",current_time)
print(current_clock_time)