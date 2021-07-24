#Niven Number
n=int(input("Enter Number: "))
sum1=0
for i in str(n):
    sum1+=int(i)

print(n,"is niven Number" if n/sum1==0 else "Not niven Number")

