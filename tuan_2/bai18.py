s = []
while True:
    new = input("Input a new word, stop when inputting a 'stop': ")
    if new.lower() == 'stop':
        break
    s.append(new)
s  = set(s)
sorted_s = sorted(s)
print(f"The sequence has {len(s)} variables")

print(sorted_s)