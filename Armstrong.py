#armstrong 
n=int(input("Enter Number: "))
sum1=0
m=len(str(n))
for i in str(n):
    sum1+=int(i)**m
print("Armstrong" if sum1==n else "Not")
