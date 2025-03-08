def main():
    danh_ba={ '0989741258':'Johnny','0903852147':'Katherine','0903712712':'Johnny'}
    try:
        while True:
            n = int(input("Chon chuc nang: "))
            if n >= 1 and n <= 4:
                break
            else:
                print("Tac vu sai")
                return 1
        if n == 1:
            for keys, values in danh_ba.items():
                print(values, keys)
        elif n == 2:
            new_name = input("Nhap ten moi: ")
            sdt = input("Nhap so dien thoai can cap nhap ten: ")
            if sdt in danh_ba:
                danh_ba[sdt] = new_name
            print(new_name, sdt)
        elif n == 3:
            sdt_moi = input("Nhap so dien thoai moi: ")
            danh_ba[sdt_moi] = input("Nhap ten cho sdt moi")
        elif n == 4:
            sdt_xoa = input("Nhap sdt can xoa")
            if sdt_xoa in danh_ba:
                danh_ba.pop(sdt_xoa)
    except ValueError:
        print("Chon chuc nang tu 1 den 4")


if __name__ == "__main__":
    main()