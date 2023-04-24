num=int(input("Enter the numbers:"))
r=0
while(num>0):
    n=num%10
    r=(r*10)+n
    num=num//10
print(r)

