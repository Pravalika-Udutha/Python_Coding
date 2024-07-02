#multiple assignment and finding the memory address
#assigning same value to different variables at same time
a=b=c=d=5
print("values of variables",a,b,c,d,sep='\n')
print("address of variables",id(a),id(b),id(c),id(d),sep='\n')
#assigning different values to variables at same time
a,b,c,d=10,20,30,40
print("values of variables",a,b,c,d,sep='\n')
print("address of variables",id(a),id(b),id(c),id(d),sep='\n')