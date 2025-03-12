import sys
def main():
    tai_khoan={'user01':'abc@123'};
    while True:
        print("Chuong trinh tai khoan")
        print("1. Nhap username va password")
        print("2. Xem danh sach username va password")
        print("3. Cap nhap username va password")
        print("4. Xoa username va password")
        n = input("Vui long chon chuc nang: ")
        if n == '1':
            nhap_user(tai_khoan)
            print('\n')
        elif n == '2':
            xem_user(tai_khoan)
            print('\n')
        elif n == '3':
            cap_nhap_user(tai_khoan)
        elif n == '4':
            xoa_user(tai_khoan)
        else:
            print("Ket thuc chuong trinh")
            sys.exit()

def xem_user(tai_khoan):
    print("{:15} {:15}".format("Username", "Password"))
    for key, value in tai_khoan.items():
        print(f"{key:15} {value:15}")

def nhap_user(tai_khoan):
    nguoi_dung = input("Nhap username: ")
    while True:
        pw = input("Nhap password: ")
        if len(pw) >= 8:
            break
    tai_khoan[nguoi_dung] = pw

def cap_nhap_user(tai_khoan):
    nguoi_dung = input("Nhap username can cap nhap: ")
    pw_cu = input("Nhap password cu: ")
    if pw_cu == tai_khoan[nguoi_dung]:
        pw_moi = input("Nhap password moi: ")
        while True:
            pw_moi_confirm = input("Nhap password moi them lan nua: ")
            if pw_moi_confirm == pw_moi:
                tai_khoan[nguoi_dung] = pw_moi
                break
            else:
                print("Nhap sai password moi. Vui long thu lai")
    else:
        print("Nhap sai password cu. Vui long thu lai")

def xoa_user(tai_khoan):
    nguoi_dung = input("Nhap user can xoa: ")
    if nguoi_dung in tai_khoan:
        confirmation = input("Ban co chac chan muon xoa (Y/N): ")
        if confirmation.upper() == 'Y':
            del(tai_khoan[nguoi_dung])
        else:
            print("Ban da huy chuc nang")
    else:
        print("Khong co nguoi dung trong tai khoan")

if __name__ == '__main__':
    main()