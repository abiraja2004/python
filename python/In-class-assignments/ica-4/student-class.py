class student():
    student_count = 0
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        student.student_count = student.student_count + 1
    def total_students(self):
        print('total count is : ', student.student_count)
    def student_details(self):
        print('name : ', self.name)
        print('age : ', self.age)
        print('sex : ', self.sex)
class transfer_student(student):
    def __init__(self,name, age, sex):
        student.__init__(self,name,age,sex)
    def get_details(self):
        print('name : ', self.name)
        print('age : ', self.age)
        print('sex : ', self.sex)
student1 = student('rajesh', '22', 'male')
student1.student_details()
student1.total_students()
no = input('enter number of students')
no = int(no)
for i in range(no):
    n = input('enter name of student')
    a = int(input('enter age of student'))
    se = input('enter sex of student')
    student2 = student(n,a,se)
    student2.student_details()
    student2.total_students()
trans = transfer_student('bhavesh','22','male')
trans.get_details()