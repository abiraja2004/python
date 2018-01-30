class Person:
    def __init__(self, first, last, age):
        self.firstname = first
        self.lastname = last
        self.age = age
    def __str__(self):
        return self.firstname + " " + self.lastname




class Student(Person):
    def __init__(self, first, last, age):
        super().__init__(first, last, age)


class Professor(Person):

    def __init__(self, first, last, age):
        super().__init__(first, last, age)


class Grade(Person):
    def __init__(self,first,last,age,grade):
        super().__init__(first,last,age)
        self.grades=grade
    def __str__(self):
        return super().__str__()+","+self.grades



class System(Person):
    def __init__(self,first,last,age,univ,course):
        super().__init__(first,last,age)
        self.university=univ
        self.courses=course

    def __str__(self):
        return super().__str__()+", university is "+self.university+", and major courses is : "+self.courses


__age1=int(input('enter the age of student'))#private variable

x = Person("bhav", "veer", 36)
y = Student("avinash", "poluru", __age1)
z=Professor("bhav","veer",23)
p=Grade("saidub","dosa",23,"A")
q=System("saidud","dosapati",23,'UMKC','CS')

print(x)
print(y)
print(z)
print(p)
print(q)
