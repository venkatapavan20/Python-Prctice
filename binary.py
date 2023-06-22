n = int(input("Enter number : "))
while(n>0):
    i=n%10
    if (i!=0 and i!=1):
        print("This is not binary")
        break
    n=n//10
    if n==0:
        print("This is binary") 