items = ["apple", "banana", "apple", "orange", "banana", "apple"]

item_counts = {}

for x in items:
    if x in item_counts:
        item_counts[x] += 1
    else:
        item_counts[x] = 1    

print(item_counts)