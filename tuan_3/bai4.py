def main():
    while True:
        n = int(input("Nhap so luong phan tu trong day Fibonacci: "))
        if n > 0:
            break
    if n == 1:
        print("Day Fibonacci la [0]")
    elif n == 2:
        print("Day Fibonacci la [0, 1]")
    else:
        fib(n)

def fib(n):
    lst = [0, 1]
    for i in range(2, n):
        lst.append(lst[i - 2] + lst[i - 1])
    print(f"Day Fibonacci la {lst}, so luong la {len(lst)}")

if __name__ == '__main__':
    main()