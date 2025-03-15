path = 'files/QueHuong.txt'
from libs.module_support import *
import sys

while True:
    print("CHUONG TRINH THAO TAC VOI TAP TIN")
    print("1. Doc noi dung")
    print("2. Viet them")
    print("3. Thong ke")
    n = input("Vui long chon chuc nang: ")
    if n == '1':
        content = read_file(path)
        print(content)
        print(type(content))
    elif n == '2':
        write_file(path)
        print("Hoan thanh chuc nang")
    elif n == '3':
        num_line, num_word, num_char = stat(path)
        print(f"So dong {num_line}")
        print(f"So tu {num_word}")
        print(f"So ki tu {num_char}")
    else:
        print("Ket thuc chuong trinh")
        sys.exit()
