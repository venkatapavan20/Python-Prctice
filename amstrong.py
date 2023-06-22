num = int(input("Please give a number: "))
s= 0 
temp = num
length= len(str(num)) 
while temp > 0:
    number = temp % 10
    s = s+ number ** length
    temp =temp//10 
if num == s:
    print("Is an Armstrong number")
else:
    print("Is not an Armstrong number")