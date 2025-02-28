a, b = eval(input("Nhap so a, b: "))
uoc = []
if a < b:
    for i in range(1, a + 1):
        if a % i == 0:
            if b % i == 0:
                uoc.append(i)
else:
    for i in range(1, b + 1):
        if b % i == 0:
            if a % i == 0:
                uoc.append(i)

print("Uoc chung lon nhat:", max(uoc))