###Strong number
n=int(input("Enter Number: "))
m=n
sum1=0
while n>0:
    mod=n%10
    s=1
    for i in range(1,mod+1):
        s=s*i   
    sum1+=s
    n=n//10
print(sum1)        
print('Strong number' if sum1==m else 'Not Strong number' )
    
    

