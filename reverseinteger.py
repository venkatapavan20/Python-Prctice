num=int(input("Enter number:"))
reverse=0
while(num>0):
    n=num%10
    reverse=(reverse*10)+n
    num=num//10
print(reverse)