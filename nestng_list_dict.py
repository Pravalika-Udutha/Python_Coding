#adding new entry to the list as dictionary
dict_list=[]
def add_new_student(name,roll_no,age,course):
    new_student={}
    new_student['name']=name
    new_student['roll_no']=roll_no
    new_student['age']=age
    new_student['course']=course
    dict_list.append(new_student)

input_values=int(input("Enter the no.of values in list:"))
for i in range(input_values):
    print(f"The details of person{i}")
    name=input("Enter the name:")
    roll_no=int(input("Enter the roll no:"))
    age=int(input("Enter the age:"))
    course=input("Enter the course:")
    add_new_student(name,roll_no,age,course)
print(dict_list)