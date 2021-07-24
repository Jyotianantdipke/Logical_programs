##perfect Number
n=int(input("Enter Number: "))
flag='Not perfect square'
for i in range(n//2):
    if i*i==n:
        flag=f"Perfect Square of {i} "
        break
print(flag)
