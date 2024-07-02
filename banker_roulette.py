import random
persons=[x for x in input("Enter everybody's name seperated by comma:").split(",")]
name=random.choice(persons)
print(f"Among the {persons}\nThe bill has to be paid by {name}")