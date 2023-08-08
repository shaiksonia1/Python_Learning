def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return(n * factorial(n - 1))
    
n=1;

print("Number: ",n)
print("factorial: ",factorial(n))


# Fibonacci
def Fibonacci(num):
  if num <= 1:
    return num
  else:
    return (Fibonacci(num - 1) + Fibonacci(num - 2))


for num in range(5):
  print(Fibonacci(num),end=',')




harry={}
print(type(harry))