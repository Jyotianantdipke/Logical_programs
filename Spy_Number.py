#Spy Number
n=int(input("Enter Number: "))
sum1=0
product=1
for i in str(n):
    sum1+=int(i)
    product*=int(i)
print(n,"is Spy Number" if sum1==product else "Not Spy Number")
