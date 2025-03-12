import sys
def main():
    goi_cuoc={'D3':[15000,3,3],'DT30':[30000,7,7],'M50':[50000,1.2,30]}
    while True:
        print("Chuc nang danh muc: ")
        print("1. Xem cac goi cuoc")
        print("2. Them goi cuoc moi vao he thong")
        print("3. Cap nhap lai thong tin goi cuoc thong qua ma goi")
        print("4. Tinh dung luong/ngay cua cac goi cuoc")
        n = input("Nhap chuc nang: ")
        if n == '1':
            xem_goi_cuoc(goi_cuoc)
            print('\n')

        elif n == '2':
            them_goi_cuoc(goi_cuoc)
            print('\n')

        elif n == '3':
            cap_nhap_goi(goi_cuoc)
            print('\n')
        
        elif n == '4':
            dung_luong_ngay(goi_cuoc)
        else:
            print("Ket thuc chuong trinh")
            sys.exit()

def xem_goi_cuoc(goi_cuoc):
    print("{:15} {:15} {:15} {:15}".format("Ma goi", "Gia", "Dung luong", "Thoi han"))
    for key, value in goi_cuoc.items():
        print(f"{key:15} {str(value[0]):15} {str(value[1]):15} {str(value[2]):15}")

def them_goi_cuoc(goi_cuoc):
    goi_moi = input("Nhap ma goi cuoc moi: ")
    gia_moi = input("Nhap gia moi: ")
    dung_luong = input("Nhap dung luong: ")
    ngay = input("Nhap so ngay: ")
    goi_cuoc[goi_moi] = [gia_moi, dung_luong, ngay]

def cap_nhap_goi(goi_cuoc):
    ma_goi = input("Nhap ma goi can cap nhap: ")
    if ma_goi in goi_cuoc.keys():
        thong_tin = input("Vui long chon thong tin can cap nhap (Dung luong, Gia, Ngay): ")
        if thong_tin == 'Dung luong':
            ma_goi[1] = input("Nhap dung luong moi: ")
        elif thong_tin == 'Gia':
            ma_goi[0] = input("Nhap gia moi: ")
        elif thong_tin == 'Ngay':
            ma_goi[2] = input("Nhap so ngay moi: ")
        else:
            print("Vui long chon dung dinh dang thong tin can thay doi")
    else:
        print("Khong cap nhap duoc. Ma khong ton tai")

def dung_luong_ngay(goi_cuoc):
    print("{:15} {:15}".format("Goi cuoc", "Dung luong ngay"))
    for key, value in goi_cuoc.items():
        print(f"{key:15} {value[1]/value[2]:15}")

if __name__ == '__main__':
    main()