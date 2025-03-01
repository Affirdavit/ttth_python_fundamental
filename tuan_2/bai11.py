animal_name = ['cho', 'meo', 'huou', 'khi', 'ga', 'cop', 'cho', 'meo', 'cho']
n = input("Nhap ten dong vat: ")
count = 0
for i in animal_name:
    if i == n:
        count += 1
if count > 0:
    print(f"Found {count} times")
else:
    print("Not found")