import time
import calendar

timestamp = time.time()
print ("当前时间戳为:", timestamp)

localtime = time.localtime(timestamp)
print ("本地时间为 :", localtime)
print ("本地时间年份为 :", localtime.tm_year)

# 格式化成2020-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))


print("="*30)

cal = calendar.month(2023,7)
print('以下打印2023年7月的日历')
print(cal)
