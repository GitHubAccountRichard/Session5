sum = 0
for i in range(1,101): #the end of range is excluded
    sum = sum + i
print(sum)

#lets print the multiplication table until 10

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} X {j} = {i*j}")
    print()
