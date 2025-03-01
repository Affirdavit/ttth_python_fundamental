or_lst=[1,5,8,-1,2,6,0,-8,-6,11,19,21,3]
new_list = []
for i in or_lst:
    new_list.append(i + 2)
new_list_2 = [num for num in or_lst if num >= 0]
new_list_3 = [num if num >= 0 else 0 for num in or_lst]
print(new_list)
print(new_list_2)
print(new_list_3)