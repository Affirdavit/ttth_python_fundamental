def main():
    u_0 = int(input("Nhap so hang dau tien: "))
    d = int(input("Nhap cong sai: "))
    n = int(input("Nhap so luong can xuat ra: "))
    cap_so_cong(u_0, d, n)

def cap_so_cong(u_0, d, n):
    lst = [u_0]
    for i in range(1, n):
        lst.append(u_0 + (i * d))
    print(f"Day cap so cong la {lst}")

if __name__ == '__main__':
    main()