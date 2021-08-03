import time
# %H-hours
# %M-months
# %S-Seconds
# %h- month(August)
# %m-month(08)
current_time=time.localtime()
current_clock_time=time.strftime("%Y-%m-%d %H:%M:%S ",current_time)
#print(current_time)
print(current_clock_time)