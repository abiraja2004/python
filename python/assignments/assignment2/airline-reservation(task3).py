class fligt():
    def __init__(self):
        self.name = 'default'
        self.f1 = 121
        self.f2 = 122
        self.f3 = 123

    def details(self):
        print('1.', self.f1)
        print('2.', self.f2)
        print('2.', self.f3)
        __f = input('enter the flight number')
        __f = int(__f)
        if __f == 121:
            self.name = 'american_airlines'
        elif __f == 122:
            self.name = 'british_airways'
        elif __f == 123:
            self.name = 'air_italia'
        return __f,self.name

class person():
    def __init__(self):
        self.name = name
        self.age = age
        self.num = num
    def details(self,name1,age1,num1):
        print('name: ',name1)
        print('age: ',age1)
        print('num: ',num1)
class employee(person):
    def __init__(self):
        super(employee, self).__init__()
    def e_details(self,name1,age1,num1):
        n1 = name1
        a1 = age1
        nu1 = num1
        p2 = person()
        print('employee details:')
        p2.details(n1, a1, nu1)

class customer(person):
    def __init__(self):
        super(customer, self).__init__()

    def c_details(self, name, age, num):
        self.n = name
        self.a = age
        self.nu = num
        p1 = person()
        print('customer details')
        p1.details(self.n,self.a,self.nu)
class fare():
    def __init__(self):
        self.fare = 0
    def calculator(self,fn):
        if fn == 121:
            return 1000
        elif fn == 122:
            return 2000
        elif fn == 123:
            return 3000
print('printing the flights available for u')
f = fligt()
a,b = f.details()
a = int(a)
name = input('enter customer name')
age = input('enter customer age')
num = input('enter phone number')
c = customer()
c.c_details(name,age,num)
e = employee()
e.e_details('raj', '23','99999999')
print('flight name : ',b)
fa = fare()
c = fa.calculator(a)
print('fare : ',c,'$')