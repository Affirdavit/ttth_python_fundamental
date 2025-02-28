x = int(input("X: "))
y = int(input("Y: "))

tong = 0
for i in range(x,y+1):
    tong = tong + i**2
print("Tong binh phuong cac so:", tong)