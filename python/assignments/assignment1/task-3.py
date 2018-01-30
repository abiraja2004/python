

x = int(input("Enter starting range: "))
y = int(input("Enter ending range: "))

for i in range(x,y):
    if(i%5==0) and (i%2==0):
        print(i)
        print("")