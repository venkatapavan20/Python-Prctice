classes_held=int(input("No.of classes held:"))
Classes_attended=int(input("No.of.classes attended:"))
if not Classes_attended <= classes_held:
    print("not match")
elif Classes_attended <= classes_held:
    if Classes_attended/classes_held>=(75/100):
        print(f"Percentage of attends:{Classes_attended/classes_held*100}")
        print("The student is allowed to sit in exam")
    else:
        print(f"Percentage of attends:{Classes_attended/classes_held*100}")
        print("The student is allowed to not sit in exam")


