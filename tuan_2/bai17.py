import sys
tu_dien={'one':['số 1','con số 1'],'father':['cha','bố']}
try:
    while True:
        n = int(input("Chon chuc nang: "))
        if n in range(1, 5):
            break
        else:
            print("Tac vu sai")
            sys.exit()
    
    if n == 1:
        for key, value in tu_dien.items():
            print(key, value)
    
    elif n == 2:
        tieng_anh = input("Nhap tu tieng anh can cap nhap: ")
        if tieng_anh in tu_dien:
            nghia_moi = input("Nhap nghia moi: ")
            tu_dien[tieng_anh].append(nghia_moi)
        print(tieng_anh, tu_dien[tieng_anh])

    elif n == 3:
        tu_moi = input("Nhap tu tieng anh moi: ")
        if tu_moi in tu_dien:
            print("Tu da co. Nhap lai tu khac")
        else:
            nghia_tu_moi = input("Nhap nghia cua tu moi: ").split(",")
            tu_dien[tu_moi] = [item.strip() for item in nghia_tu_moi]
        print(tu_moi, tu_dien[tu_moi])
    
    else:
        tu_xoa = input("Nhap tu can xoa: ")
        if tu_xoa in tu_dien:
            tu_dien.pop(tu_xoa)
            print(tu_dien)
        else:
            print("Khong co tu xoa trong tu dien")

except ValueError:
    print("Tac vu sai")