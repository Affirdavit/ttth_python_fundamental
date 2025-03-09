can = ("Canh", "Tan", "Nham", "Quy", "Giap", "At", "Binh", "Dinh", "Mau", "Ky")
chi = ("Than", "Dau", "Tuat", "Hoi", "Ty", "Suu", "Dan", "Mao", "Thin", "Ty.")
try:
    while True:
        nam = int(input("Nhap so nam tuong ung: "))
        if nam > 0:
            break
    print(f"{can[nam % 10]} {chi[nam % 12]}")
except ValueError:
        print("Value Error. Must be number")