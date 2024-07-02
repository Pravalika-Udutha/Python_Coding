actual_map=[]
for i in range(3):
    row=[]
    for j in range(3):
        row.append(input())
    actual_map.append(row)
position=int(input("Enter the position where you want to hide money:"))
second=position%10
first=position//10
actual_map[first-1][second-1]='x'
for i in range(3):
    for j in range(3):
        print(actual_map[i][j],end=" ")
    print()