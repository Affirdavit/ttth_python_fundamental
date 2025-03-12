import math
from functools import reduce
def main():
    lst = []
    while True:
        n = input("Nhap phan tu: ")
        lst.append(int(n))
        cont = input("Nhan 1 de tiep tuc, nhan bat ki de dung su dung: ")
        if cont != '1':
            break
    new_map = list(map(lambda n: n * 2, lst))
    new_filter = list(filter(lambda x: prime(x), lst))
    new_reduce = reduce(lambda x, y: x * y, lst)
    print(f"Map list moi la {new_map}")
    print(f"Filter list moi la {new_filter}")
    print(f"Reduce list moi la {new_reduce}")

def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    main()