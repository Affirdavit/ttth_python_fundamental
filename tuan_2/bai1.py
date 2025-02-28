# Countdown from n to 1 (n > 0 ) in 2 ways:
n = int(input("Nhap so nguyen n: "))
# Solution 1
for i in range(n):
    print(n-i)

#Solution 2
while n >= 1:
    print(n)
    n -= 1