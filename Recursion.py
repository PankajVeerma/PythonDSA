#N natural number
def fun1(n):
    if n>0:
       fun1(n-1)
       print(n,end=" ")
fun1(9)  
print()     
#N natural number in reverse Order
def fun2(n):
    if n>0: 
       print(n,end=" ")
       fun2(n-1)
      
fun2(9)
print()       
#N Odd natural number 
def fun3(n):
    if n>0: 
      
       fun3(n-1)
       print(2*n-1,end=" ")
fun3(9)       
print()
#N Odd natural number in reverse order
def fun4(n):
    if n>0: 
       print(2*n-1,end=" ")
       fun4(n-1)
      
fun4(9)       
print()
#N Even natural number 
def fun5(n):
    if n>0: 
      
       fun5(n-1)
       print(2*n,end=" ")
fun5(9)       
print()
#N Even natural number in reverse order
def fun6(n):
    if n>0: 
       print(2*n,end=" ")
       fun6(n-1)
      
fun6(9)       
print()

#Sum of n natural Number
def fun7(n):
    if n==0:
        return 1
    return n + fun7(n-1)
      
print(fun7(5))
print()
#Sum of n odd natural Number
def fun8(n):
    if n==1:
      return 1
    return 2*n-1 + fun8(n-1)
      
print(fun8(5))
print()

#Sum of n even natural Number
def fun9(n):
    if n==1:
      return 2
    return 2*n + fun9(n-1)
      
print(fun9(5))
print()
#factorial of  Number
def fun10(n):
    if n==0:
      return 1
    return n * fun10(n-1)
      
print(fun10(5))
print()
#sum of first n natural   Number
def fun11(n):
    if n==1:
      return 1
    return n*n + fun11(n-1)
      
print(fun11(5))
print()