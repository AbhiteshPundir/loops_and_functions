lst= []
 
n = int(input("Enter number of elements : "))
 
for i in range(0, n):
    ele = int(input())
    lst.append(ele) # adding the element

for j in lst:
    if j>=0:
        print(j, end=" ")
