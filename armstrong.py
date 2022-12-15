#armstrong number
#1*1*1+ 5*5*5+3*3*3=153
#is an armstrong number
n = int(input("enter number: "))
s = n
b = len(str(n))
sum1 = 0
while n != 0:
    r = n % 10
    sum1 = sum1+(r**b)
    n = n//10
if s == sum1:
    print("The given number", s, "is armstrong number")
else:
    print("The given number", s, "is not armstrong number")

 