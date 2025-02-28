# Kiem tra so nguyen to
n = int(input("Nhap so n: "))
for i in range(2, n):
    if n % 1 == 0 and n % n == 0:
        if n % i == 0:
            print(f"{n} khong phai la so nguyen to")
            break
else:
    print(f"{n} la so nguyen to")