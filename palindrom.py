n = int(input("please give a number : "))
r=0
temp = n
while temp!=0:
    r = r*10 + temp%10     
    temp=temp//10
if r==n:
    print("number is palindrom")
else:
    print("number is not palindrom")