import time
import calendar
# time = time.localtime()
# print('The year is: ', time.tm_year)
# print('The current month is: ', time.tm_mon)
# print('The day is: ', time.tm_mday)
# print('It is: ', time.tm_hour, time.tm_min, time.tm_sec)

date_hour = time.asctime(time.localtime(time.time()))
print('Local time: ', date_hour)

calendar = calendar.month(2023, 4)
print(calendar)