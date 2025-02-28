n = int(input("Nhap so nguyen n: "))
# Tong cac so le <= n
sum1 = 0
sum_chan = 0
for i in range(n+1):
    if i % 2 == 1:
        sum1 += i
    else:
        sum_chan += i
print("tong cac so le <= n", sum1)
# Tong cac so chan <= n
print("tong cac so chan", sum_chan)
# Tich cac so tu 1 den n
tich_1 = 1
tich_2 = 1
for i in range(1, n + 1):
    tich_1 = tich_1 * i
    if i % 3 == 0:
        tich_2 = tich_2 * i
print("tich cac so tu 1 den n",tich_1)
# Tich cac so chia het cho 3 <= n
print("tich cac so chia het cho 3", tich_2)
