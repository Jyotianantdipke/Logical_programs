#Reverse of a number
n=int(input("Enter no: "))  
p=''                        # takes one empty string for appending the numbers in reverse manner
while n>0:
    mod=n%10
    p+=str(mod)             # remainder is appended at last in a string p
    n=n//10
print(p)                    # here we got a reverse number
