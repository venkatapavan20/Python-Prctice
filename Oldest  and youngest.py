A=int(input("A:"))
B=int(input("B:"))
C=int(input("C:"))
if A > B:
    if A > C: 
        oldest = A 
    else: 
        oldest = C 
else: 
        if B > C:
            oldest = B
        else: 
            oldest = C 
if A < B: 
    if A < C: 
        youngest = A 
    else: 
        youngest = C 
else: 
    if B < C: 
        youngest = B
    else: 
        youngest = C
print ("Oldest person's age is", oldest) 
print ("Youngest person's age is", youngest)