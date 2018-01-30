string = input('enter the sentence')
list = string.split()
print(list)
ln = len(list)
for i in range(ln):
    list[i] = list[i].strip(',')
    list[i] = list[i].strip('.')
list2 = []
print(list)
for i in range(ln):
    if list[i] not in list2:
        list2.append(list[i])
print(sorted(list2))
