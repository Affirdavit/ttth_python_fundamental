import sys
path = 'files/diem.csv'
from libs.module_support import *
while True:
    print("CHUONG TRINH THAO TAC VOI TAP TIN")
    print("1. XEM noi dung")
    print("2. Them ket qua moi")
    print("3. Cap nhap ket qua")
    print("4. Xoa ket qua")
    print("5. Thong ke hoc sinh rot mon")
    print("6. Tinh DTB")
    n = input("Vui long chon chuc nang: ")
    if n == '1':
        content = read_file(path)
        print_file(content)
    elif n == '2':
        pass
    elif n == '3':
        pass
    elif n == '4':
        pass
    elif n =='5':
        content = read_file(path)
        tieu_de = content.pop(0)
        ket_qua = search_fail(content)
        print(f" Co {len(ket_qua)} ket qua dc tim thay")
        if len(ket_qua) > 0:
            ket_qua.insert(0, tieu_de)
            print_file(ket_qua)
    
    elif n == '6':
        content = read_file(path)
        tieu_de = content.pop(0)
        ma_mon = set()
        for row in content:
            ma_mon.add(row[2])
        ma_mon_sorted = sorted(ma_mon)
        print("{:30}{:15}".format("Ma Mon", "Diem Trung Binh"))
        for n in ma_mon_sorted:
            dtb = avg_score(n, content)
            print("{:30}{:15}".format(n, dtb))
    else:
        print("Ket thuc chuong trinh")
        sys.exit()