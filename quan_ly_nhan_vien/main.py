import sys
path = 'files/madinhdanh.csv'
from libs.module_support import *
while True:
    print("CHUONG TRINH THAO TAC VOI TAP TIN")
    print("1. Doc noi dung")
    print("2. Viet them")
    print("3. Thong ke")
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
        pass
    else:
        print("Ket thuc chuong trinh")
        sys.exit()