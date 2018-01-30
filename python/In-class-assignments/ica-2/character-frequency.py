str = 'jdjdokpwsuyhubx'
l = len(str)
list = [str]
for i in range(l):
    count = 0
    for j in range(l):
        if list[0][i] == list[0][j]:
            count = count+1
    print(count,list[0][i])