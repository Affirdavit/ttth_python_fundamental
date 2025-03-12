from math import factorial
def main():
    n = int(input("Nhap: "))
    for n in range(0, n + 1):
        for k in range(0, n + 1):
            val = tim_c(n, k)
            print(f"{val}", end='\t')
        print('\n')

def tim_c(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))

if __name__ == '__main__':
    main()