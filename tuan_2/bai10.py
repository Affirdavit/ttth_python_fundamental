import statistics
'''
Viết chương trình cho phép người dùng nhập dữ liệu đưa vào list A các số.
Thực hiện:
- In ra 2 phần tử đầu tiên;
- In ra 2 phần tử cuối cùng;
- Cho biết list A gồm bao nhiêu phần tử;
- Cho biết tổng của các phần tử có trong A;
- Tìm giá trị của phần tử lớn nhất;
- Tìm giá trị của phần tử bé nhất;
- Tính trung bình cộng của các phần tử;
- Sắp xếp list theo thứ tự tăng dần;
- Sắp xếp list theo thứ tự giảm dần;'''
A = []
n = eval(input("Nhap du lieu: "))
for i in n:
    A.append(i)
# 2 phan tu dau tien
print(A[:2])
# 2 phan tu cuoi cung
print(A[-2:])
# List A gom bao nhieu phan tu
print(f"List A co {len(A)} phan tu")
# Tong cua cac phan tu co trong A
print(f"Tong cua cac phan tu co trong A la {sum(A)}")
# Gia tri cua phan tu lon nhat
print(f"Gia tri cua phan tu lon nhat la {max(A)}")
# Gia tri cua phan tu be nhat
print(f"Gia tri cua phan tu be nhat la {min(A)}")
# Trung binh cong cua cac phan tu
print(f"Trung binh cong: {statistics.mean(A)}")
# sap xep thu tu tang
print(sorted(A))
print(sorted(A, reverse=True))