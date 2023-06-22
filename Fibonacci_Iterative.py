num=int(input("enter number:"))

a=0
b=1

for i in range(0,num):
    if i<=1:
        print(i)
    else:
        result=a+b
        a=b
        b=result
        print(result)