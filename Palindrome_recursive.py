n=int(input("Enter number:"))

temp=n

rev=0
while n>0:
    r=n%10
    rev=(rev*10)+r
    n=n//10

if temp==rev:
    print("number is palindrome")
else:
    print("Not palindrome")