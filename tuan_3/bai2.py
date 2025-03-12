def main():
    while True:
        a = int(input("Nhap so nguyen duong a: "))
        b = int(input("Nhap so nguyen duong b: "))
        if a > 0 and b > 0:
            break
    if friend(a, b):
        print(f"{a} va {b} la 2 so than thiet")
    else:
        print(f"{a} va {b} khong phai so than thiet")

def friend(a, b):
    uoc_a = []
    uoc_b = []
    for i in range(1, a):
        if a % i == 0:
            uoc_a.append(i)
    for i in range(1, b):
        if b % i == 0:
            uoc_b.append(i)
    if sum(uoc_a) == b and sum(uoc_b) == a:
        return True
    else:
        return False

if __name__ == '__main__':
    main()