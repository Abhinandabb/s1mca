num=int(input("enter the number of fibonacci numbers to generate:"))
a=0
b=1
fibo=[a]

for i in range(1,num):
    a,b=b,a+b
    fibo.append(a)
print(fibo)    
