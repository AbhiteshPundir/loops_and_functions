length=int(input("Enter the no. of terms:"))
first = 0
second = 1
print(first, second, end=" ")
length -= 2
while length > 0:
    print(first, ",", second, sep="", end=",")
    temp = second
    second = first + second
    first = temp
    length -= 1
