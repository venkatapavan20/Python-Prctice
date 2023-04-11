#A student will not be allowed to sit in exam if his/her attendence is less than 75%.
#Take following input from user
#Number of classes held
#Number of classes attended.
#And print
#percentage of class attended
#Is student is allowed to sit in exam or not.

classes_held=int(input("No.of classes held:"))
Classes_attended=int(input("No.of.classes attended:"))
if not Classes_attended > classes_held:
    print("not match")
elif Classes_attended/classes_held>=(75/100) and not Classes_attended > classes_held :
        print(f"Percentage of attends:{Classes_attended/classes_held*100}")
        print("The student is allowed to sit in exam",)
else:
        print(f"Percentage of attends:{Classes_attended/classes_held*100}")
        print("The student is allowed to not sit in exam")




