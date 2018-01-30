print('choose one of the cars:')
list = ('benz', 'chevy', 'toyota', 'crizzler')
for i in range(len(list)):
    print(i+1, list[i])
opt = input('enter the option like (1 for benz): ')
opt = int(opt)
print(opt, list[opt-1])

def charged(a):
    op = a
    car_charge = 0
    print('choose type of petrol:\n 1.regular \n 2.unleaded \n 3.diesel')
    petrol = int(input('choose the option'))
    global pet
    while petrol in range(1, 2, 3):
        if petrol == 1:
            pet = 2
        elif petrol == 2:
            pet = 3
        elif petrol == 3:
            pet = 4
    miles = int(input('enter the number of miles'))
    if a == 1:
        car_charge = 20
    elif a == 2:
        car_charge = 25
    elif a == 3:
        car_charge = 30
    elif a == 4:
        car_charge = 40
    days = int(input('enter the number of days'))
    car_charge = int(car_charge)
    charge = (days*car_charge)+(miles*pet)
    print('you will be charged ',charge)
charged(opt)
