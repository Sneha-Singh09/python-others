#def hey():
#    message='hi'
#    def fun():
#        print(message)
#    return fun
#y=hey()
#print(y.__name__)
#---------------------------------------
def add(x,y):
       return  x + y
def subtract(x,y):
       return  x - y
def multiply(x,y):
       return x * y
def divide(x,y):
       return x/y
def square(x,y):
    return x**y
def remainder(x,y):
    return x%y
class Calci:
   def display():
        print('CALCULATOR')
        i=int(input())
        k=input()
        j=int(input())
        if(k=='+'):
            print(f'{i} {k} {j}= {add(i,j)}')
        if(k=='-'):
            print(f'{i} {k} {j}= {subtract(i,j)}')
        if(k=='*'):
            print(f'{i} {k} {j}= {multiply(i,j)}')
        if(k=='/'):
            print(f'{i} {k} {j}= {divide(i,j)}')
        if(k=='**'):
            print(f'{i} {k} {j}= {square(i,j)}')
        if(k=='%'):
            print(f'{i} {k} {j}= {remainder(i,j)}')
d=Calci
d.display()
print("to continue press 1")
cont=input()
if cont=='1':
      d.display()




        
    
    

