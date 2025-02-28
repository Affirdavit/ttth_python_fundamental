s = input("Input string: ")
# Requirement 1: print until ' ' blank is found. Print the index
for i in s:
    print(i)
    if i == ' ':
        print(s.index(i))
        break

# Requirement 2: print but skip ' ' blank
for i in s:
    if i != ' ':
        print(i, end="")
print("")
# Requirement 3:
if 'a' in s:
    print("Found")
else:
    print("Not found")