num=int(input("Enter number:"))
def fibonacci(i):
    if i<=1:
        return i
    else:
        return fibonacci(i-1)+fibonacci(i-2)

for i in range(num):
    print(fibonacci(i))