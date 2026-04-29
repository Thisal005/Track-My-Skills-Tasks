# Reverse a list without using the built-in reverse() method or slicing.

List = [1, 2, 3, 4, 5]
rList = []

for x in range(len(List)):
    #rList.append(List[len(List) - 1 - x])
    rList.insert(0, List[x])

List.reverse()
print(List)
print(rList)