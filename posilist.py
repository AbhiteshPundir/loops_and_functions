lst = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
    lst[i]=int(input())
    if lst[i]>0:
        print(lst[i],end=",")

