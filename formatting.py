#string formatting

person={'name': 'Sneha','age':19}
'''sentence=f"My name is {person['name']} and I am {person['age']} years old"
print(sentence)
tag='/h1'
text='body'
line='<{0}>{1}<{0}>'.format(tag,text)
print(line)
sentence='My name is {0} and I am {1} years old'.format(person['name'],person['age'])
print(sentence)
sentence='My name is {0[name]} and I am {1[age]} years old'.format(person,person)
print(sentence)
sentence='My name is {0[name]} and I am {0[age]} years old'.format(person)
print(sentence)
l=['sneha',19]
sentence='My name is {0[0]} and I am {0[1]} years old'.format(l)
print(sentence)
sentence='My name is {name} and I am {age} years old'.format(name='Sneha',age=19)
print(sentence)
#most convienient
sentence='My name is {name} and I am {age} years old'.format(**person)
print(sentence)
class person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=person('Sneha',19)
sentence='My name is {0.name} and I am {0.age} years old'.format(p1)
print(sentence)
#number formatting
for i in range(1,11):
    #:02-indicates we need to print 2 numbers, 03 - 3 numbers
    value='The value is {:02}'.format(i) 
    print(value)'''
pi=3.14159265
value='The value of pi is {0:.2f}'.format(pi)
print(value)
value='1 km equals {:,.2f} decimetre'.format(100**2)
print(value)
#datetime formatting
import datetime
my_bdate=datetime.datetime(2000,8,9,11,00,00)
'''
print(my_bdate)
#August 08,2000,can look up the net for the formatting options
mine='{:%B %d, %Y}'.format(my_bdate)
print(mine)'''
#I was born on 8 August 2000,it was a...
mine='I was born on {0:%d %B %Y}, it was a {0:%A} and {0:%j} day of the year'.format(my_bdate)
print(mine) 
a='/'
print(type(a))