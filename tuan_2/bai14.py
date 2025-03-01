import calendar
day, month, year = input("Nhap ngay thang nam: ").split('/')
print(calendar.weekday(int(year), int(month), int(day)))
date = calendar.weekday(int(year), int(month), int(day))
print(calendar.day_name[date])