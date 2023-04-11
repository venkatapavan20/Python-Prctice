Marks=int(input("Enter Marks:"))
if Marks<25:
    print("F")
elif Marks in range(25,45):
    print("E")
elif Marks in range(45,50):
    print("D")
elif Marks in range(50,60):
    print("C")    
elif Marks in range(60,80):
    print("B")
else:
    Marks>80
    print("A")
