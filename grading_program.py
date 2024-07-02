#assigning grade values to the students using dictonary
student_details={}
items_number=int(input("Enter the no.of items that needs to added:"))
for i in range(1,items_number+1):
    print(f"Enter student{i} details")
    keys_input=(input("Enter the key:"))
    values_input=int(input("Enter the value:"))
    student_details[keys_input]=values_input
student_marks={}
for x in student_details:
    marks=student_details[x]
    if marks>90:
        student_marks[x]='A+'
    elif marks>80:
        student_marks[x]='A'
    elif marks>70:
        student_marks[x]='B+'
    elif marks>60:
        student_marks[x]='B'
    elif marks>50:
        student_marks[x]='C'
    elif marks>40:
        student_marks[x]='D'
    else:
        student_marks[x]='F'
print(student_marks)
