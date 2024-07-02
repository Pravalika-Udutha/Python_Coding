#deleting a variable
a=10
b=20
print("value of a and b",a,b)
del a
'''File "d:/python coding/deleting_variable.py", line 6, in <module>
    print("value of a and b after deleting the a",a,b)
NameError: name 'a' is not defined'''
print("value of a and b after deleting the a",a,b)