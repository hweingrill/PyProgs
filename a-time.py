import time

#https://lernenpython.com/time/

#time.struct_time(tm_year=2018, tm_mon=12, tm_mday=27, 
#                    tm_hour=6, tm_min=35, tm_sec=17, 
#                    tm_wday=3, tm_yday=361, tm_isdst=0)

# seconds passed since epoch
seconds = 1545925769.9618232
local_time = time.ctime(seconds)
print("Local time:", local_time)
input()
print("\nDieser wird sofort gedruckt.")
time.sleep(0.2)
print("This is printed after 2.4 seconds.")

result = time.localtime(1545925769)
print("result:", result)
print("\nyear:", result.tm_year)
print("tm_hour:", result.tm_hour)

seconds = 1545925769
# returns struct_time
t = time.localtime(seconds)
print("t1: ", t)
# returns seconds from struct_time
s = time.mktime(t)
print("\s:", seconds)
print('\n localtime-tuple')
named_tuple = time.localtime() # get struct_time
time_string = time.strftime("%d/%m/%Y, %H:%M:%S, Woche: %W", named_tuple)
print(named_tuple)
print(time_string)

print()
time_string = "03 March, 2022"
result = time.strptime(time_string, "%d %B, %Y")
print(result)
