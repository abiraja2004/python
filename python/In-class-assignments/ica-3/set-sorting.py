set1=[]
while(0==0):
    inp = input('Enter Y to input N to exit')
    if inp.__eq__('N'):
        break
    else:
        course = input('please enter the input string')
        set1.append(course)
set1.sort()
len1=len(set1)
count=1
for y in set1:
    if(count==len1):
        print(y)
    else:
        print(y,end=",")
        count=count+1

