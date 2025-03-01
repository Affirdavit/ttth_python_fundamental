can = {
    0: "Canh",
    1: "Tan",
    2: "Nham",
    3: "Quy",
    4: "Giap",
    5: "At",
    6: "Binh",
    7: "Dinh",
    8: "Mau",
    9: "Ky",
}
chi = {
    0: "Than",
    1: "Dau",
    2: "Tuat",
    3: "Hoi",
    4: "Ty",
    5: "Suu",
    6: "Dan",
    7: "Mao",
    8: "Thin",
    9: "Ty.",
    10: "Ngo",
    11: "Mui",
}
nam = int(input("Nhap so nam tuong ung: "))
can_du = nam % 10
chi_du = nam % 12
print(f"{can[can_du]} {chi[chi_du]}")