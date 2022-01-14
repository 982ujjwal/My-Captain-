n=int(input("Enter Till how many terms do you need Fibonacci Series:  "))
i=0
a=0
b=1

while i<=n:
    
    print(i)
    
    a=b
    b=i
    i=a+b
    