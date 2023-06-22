def Sum(n):
    
    s = 0
    for i in str(n): 
      s =s + int(i)      
    return s
   
n =int(input("Enter:")) 
print(Sum(n))