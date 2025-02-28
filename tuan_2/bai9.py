n = int(input("Nhap so N: "))
# List A & B: chua cac so chan va cac so le trong pham vi tu 0 den n
A = []
B = []
for i in range(n + 1):
    if i % 2 == 0:
        A.append(i)
    else:
        B.append(i)
print("List so chan:", A)
print("List so le:", B)
C = ["Bo", "Me", "Anh", "Toi", "Em"]
D = ["Ma sinh vien", "Ten Mon Hoc", 7.0]
print(C)
print(D)
E = []
s = input("Nhap chuoi: ")
for i in s:
    E.append(i)
print(E)
F = []

