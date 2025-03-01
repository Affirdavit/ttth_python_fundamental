import random
while True:
    n = int(input("Nhap so tu 0-99: "))
    if n >= 0 and n <= 99:
        break
    else:
        print("So trong khoang tu 0 - 99")
lucky_number = random.randint(0, 99)
if n == lucky_number:
    print("You won")
else:
    print("Bad luck")