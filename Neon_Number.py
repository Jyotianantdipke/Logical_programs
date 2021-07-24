

n=int(input("Enter Number: "))
m=n*n
sum1=0
for i in str(m):
    sum1+=int(i)

print(n,"is neon number" if sum1==n else "No Neon Number")
