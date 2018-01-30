str = input('enter a string with numbers and letters ')
l = len(str)
count1 = 0
count2 = 0
for i in range(l):
    if str[i].isalpha()== True:
        count1 = count1+1
    elif str[i].isdigit()== True:
        count2 = count2+1
print('letters: ',count1,'numbers: ',count2)
