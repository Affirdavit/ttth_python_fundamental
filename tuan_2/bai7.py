# Tim so hoan hao
n = int(input("Nhap so nguyen N: "))
if n > 0:
    uoc = []
    for i in range(1, n):
        if n % i == 0:
            uoc.append(i)
    print("Tap hop uoc cua {} la {}".format(n, uoc))
    if sum(uoc) == n:
        print(f"{n} la so hoan hao")
    else:
        print(f"{n} khong phai so hoan hao")
else:
    print("N phai la so nguyen duong")