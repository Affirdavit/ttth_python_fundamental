import calendar
day, month, year = input("Nhap ngay thang nam: ").split('/')
date = calendar.weekday(int(year), int(month), int(day))
print(date)
print(calendar.day_name[date])