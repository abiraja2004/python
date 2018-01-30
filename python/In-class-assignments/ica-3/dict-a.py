list=[]


while(0==0):
 inp = input('Enter Y to input N to exit')
 if inp.__eq__('N'):
     break
 else:
  dict1 = {}
  course = input('please enter the course name')
  lastgpa = int(input('please enter last gpa'))
  currentgpa = int(input('please enter current gpa'))
  dict1['course']=course
  dict1['lastgpa']=lastgpa
  dict1['currentgpa'] = currentgpa
  list.append(dict1)


result=[]

for value in list:
    dict2 = {}
    dict2['course'] = value['course']
    dict2['lastgpa+currentgpa']=(value['lastgpa']+value['currentgpa'])/2
    result.append(dict2)

for value in result:
    print(value)

