import sys
path = 'files/madinhdanh.csv'
from libs.module_support import *
while True:
    print("CHUONG TRINH THAO TAC VOI TAP TIN")
    print("1. XEM noi dung")
    print("2. Them nhan vien moi")
    print("3. Cap nhap thong tin")
    print("4. Xoa nhan vien")
    print("5. Thong ke nhan vien trong bo phan")
    n = input("Vui long chon chuc nang: ")
    if n == '1':
        content = read_file(path)
        print_file(content)
    elif n == '2':
        content = read_file(path)
        new_acc = add_acount(content)
        write_file(path, new_acc)
    elif n == '3':
        content = read_file(path)
        new_content = update_account(content)
        write_file(path, new_content)
    elif n == '4':
        content = read_file(path)
        new_content = delete_account(content)
        write_file(path, new_content)
    elif n =='5':
        content = read_file(path)
        tieu_de = content.pop(0)
        result = thong_ke(content)
        print(f"Co {len(result)} ket qua duoc tim thay")
        if len(result) > 0:
            result.insert(0, tieu_de)
            print_file(result)
    else:
        print("Ket thuc chuong trinh")
        sys.exit()