#arithmetic operators
#8+6- add
#8-6-sub
#8*6-mul
#8/6-div
#8//6-floor div- rounds off value removing decimal
#8%6-modulus
#8**6-exponent
#abs- removes negative sign
#round-round offs round(no.,how many places)
"""print(abs(-5))
print(round(5.789,2))
print(8/3)"""
#comparison operators
#< -- less than
#> -- greater than
#<= --less than or equal to
#>= --greater than or equal to
#== -- equal
#!= --not equal
#is:checks if id's are same,in a list if all the components are same but variables are not equal then we get false
#to check id use print(id(variable name))
#if we set the variables equal to string but they are not strings 
#and if we add them then we get a concatenated value so we need to cast the values
n1='100'
n2='200'
n1=int(n1)
n2=int(n2)
def add():
    print(n1+n2)
#boolean operators
#and
#or
#not--changes the boolean value
#false values
#1.false
#2.none
#3.zero of any numeric type
#empty sequence:eg eg [],'',()
#empty mapping:{}