import csv
import sys
from datetime import datetime

def read_file(_path):
    f = open(_path, 'r', encoding='utf-8')
    content = []
    for row in csv.reader(f):
        content.append(row)
    f.close()
    return content

def print_file(content):
    for row in content:
        print(f"{row[0]:15}{row[1]:30}{row[2]:15}{row[3]:15}{row[4]:15}{row[5]:15}{row[6]:50}")

def write_file(_path, content):
    f = open(_path, 'w', encoding='utf-8', newline='')
    writer = csv.writer(f)
    writer.writerows(content)
    print("Luu noi dung thanh cong")
    f.close()

def add_acount(content):
    ma_dinh_danh = input("Nhap ma dinh danh: ")
    for row in content:
        if row[0] == ma_dinh_danh:
            print("Ma dinh danh da ton tai")
            sys.exit()
    else:
        ho_ten = input("Nhap ho ten: ")
        usname = input("Nhap username: ")
        pw = input("Nhap password: ")
        gioi_tinh = input("Nhap gioi tinh: ")
        bo_phan = input("Nhap bo phan: ")
        ngay_tao = datetime.now()
        tai_khoan = [ma_dinh_danh, ho_ten, usname, pw, gioi_tinh, bo_phan, ngay_tao]
        content.append(tai_khoan)
        print("Them thanh cong")
    return content

def update_account(content):
    ma_dinh_danh = input('Nhap ma dinh danh: ')
    for row in content:
        if row[0] == ma_dinh_danh:
            ho_ten = row[1]
            username = row[2]
            _pass = row[3]
            gioi_tinh = row[4]
            bo_phan = row[5]
            ngay_tao = row[6]
            while True:
                n = input("Vui long chon thong tin muon doi (1: ho ten, 2: username, 3: password, 4: gioi tinh, 5: bo_phan, 6: ngay tao): ")
                if n == '1':
                    ho_ten = input("Nhap ten moi: ")
                    continue

                elif n == '2':
                    username = input("Nhap username moi: ")
                    continue

                elif n == '3':
                    _pass = input("Nhap password moi: ")
                    continue

                elif n == '4':
                    gioi_tinh = input("Nhap gioi tinh moi: ")
                    continue

                elif n == '5':
                    bo_phan = input("Nhap bo phan moi: ")
                    continue

                elif n == '6':
                    ngay_tao = datetime.now()
                    continue
                else:
                    break
            row[1], row[2], row[3], row[4], row[5], row[6] = ho_ten, username, _pass, gioi_tinh, bo_phan, ngay_tao
            print("Cap nhap thanh cong")
            break

    else:
        print("Ma dinh danh khong ton tai")
    return content

def delete_account(content):
    ma_dinh_danh = input("Nhap ma dinh danh can xoa: ")
    for row in content:
        if ma_dinh_danh == row[0]:
            content.remove(row)
            print("Xoa thanh cong")
            break
    else:
        print("Khong ton tai ma dinh danh")
    return content

def thong_ke(content):
    bo_phan = input("Nhap bo phan: ")
    lst = []
    for row in content:
        if bo_phan == row[5]:
            lst.append(row)
    return lst