#from datetime import date
import datetime
import time

local_time = time.ctime()
print(type(local_time))
print(local_time)
print()
result = time.localtime()
print("result:", result)
print("\nyear:", result.tm_year)
print("tm_hour:", result.tm_hour)
print("Jahrestag:", result.tm_yday)
print("Sommerzeit:", result.tm_isdst)        # Sommerzeit
print("Wo-Tag:   ", result.tm_wday)

sa = time.mktime(result)
print("s: ", sa)
#time.sleep(5.0)
result = time.localtime()
sb = time.mktime(result)
print("s: ", sb)
print(sb - sa, ' Sekunden vergangen')
#----------------------------------------------------
named_tuple = time.localtime() # get struct_time
time_string = time.strftime("%Y.%m.%d, %H:%M:%S", named_tuple)
print(time_string)
today = datetime.datetime.today()
print('aus datetime: ',today)

