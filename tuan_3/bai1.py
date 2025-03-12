def main():
    while True:
        h = float(input("Nhap chieu cao: "))
        w = float(input("Nhap can nang: "))
        if h > 0 and w > 0:
            break
    bmi = tinh_bmi(h, w)
    print(f"BMI: {bmi}")
    khuyen(bmi)

def tinh_bmi(h, w):
    return w / (h ** 2)

def khuyen(n):
    if n < 18:
        print("Gay")
    elif n > 25:
        print("Beo")
    else:
        print("OK")

if __name__ == '__main__':
    main()
