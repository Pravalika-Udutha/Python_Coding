#cloning of a variable and memory location
a=10
b=a
print("id of a ",id(a),"id of a ",id(b),sep='\n')
b=10
print("after assigning same value to b id of a ",id(a),"id of b ",id(b),sep='\n')
b=9
print("after assigning diffrent value to b id of a ",id(a),"id of a ",id(b),sep='\n')