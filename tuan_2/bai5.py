n = int(input("Nhap so bang cuu chuong: "))
for i in range(2, n+1):
    print(f"Bang cuu chuong {i}")
    for j in range(1, 10):
        print(f"{i} * {j} = {i * j}")