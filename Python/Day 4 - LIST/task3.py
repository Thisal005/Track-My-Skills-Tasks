lst = [52, 45, 52, 11, 1, 23, 74, 10, 11, 52]

lst.sort()

unique = [lst[0]]

for i in range(1, len(lst)):
    if lst[i] != lst[i - 1]:
        unique.append(lst[i])

lst.clear()
lst = list(unique)

print(lst)