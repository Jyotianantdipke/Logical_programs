#palindrome number

# First Method
n=int(input("Enter no: "))
m=n
p=''
while n>0:
    mod=n%10
    p+=str(mod)
    n=n//10
print('palindrome' if m==int(p) else 'not palindrome')
 
  
  
# Second Method
n=int(input("Enter no: "))
m=str(n)
k=m[::-1]
print('palindrome' if m==k else 'not palindrome')
