
#VARIABLES-local,enclosing,global,built-in-we can't use built in func and variable
#putting paranthesis means that we have to execute a function
#first class functions allow us to treat functions like any other objects
#eg- we can pass functions as variables to another function,can return functions and can assign functions to variables
'''closures allow us to take advantage of first class functions and return inner functions which has access to variable 
local to scope in which they are created '''
#closure-closes over a free variable from its environment
'''import logging
logging.basicConfig(filename='example.log', level=logging.INFO)

def logger(func):
    def log_func(*args):
        logging.info('Running {} with arguments {}'.format(func.__name__,args))
        print(func(*args))
    return log_func
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
add_logger=logger(add)
sub_logger=logger(sub)
add_logger(10,12)
sub_logger(18,11)'''
#DECORATOR
def decorator(og_fun):
    def wrap_deco():
        return og_fun()
    return wrap_deco()
@decorator
def why():
    print("why are we doing this")
    print("It allows us to add functionality to existing func,we can make changes in") 
    print("the wrapper func or decorator func instead of og_fun")
#display=decorator(why)--this line is euivalent to @decorator write anyone of them 
#display()
#if we have returned the inner func then later assign the outer func to a variable and
# again execute the varaible then it would  give none cause we are not returning avalue we have already executed the statement
#and don't need a variable 