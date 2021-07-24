##fibonacci series
n=int(input("Enter number: "))
fib_series=[0,1]
for i in range(2,n+1):
    fib_series.append(fib_series[i-1]+fib_series[i-2])
print(fib_series)
