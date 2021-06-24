#           BASIC OPERATORS

#                   Arithmetic
a = 21
b = 10
c = 0 # Would be better if declare this first
c = a + b
print ("Line 1 - Value of c is ", c)
c = a - b
print ("Line 2 - Value of c is ", c )
c = a * b
print ("Line 3 - Value of c is ", c)
c = a / b
print ("Line 4 - Value of c is ", c )
c = a % b
print ("Line 5 - Value of c is ", c)
a = 2
b = 3
c = a**b
print ("Line 6 - Value of c is ", c)
a = 10
b = 4
c = a//b 
print ("Line 7 - Value of c is ", c)


#                Comparison (==, !=, <, >, <=, >=)
a = 22
b = 5
if ( a == b ):
 print ("Line 1 - a is equal to b")
else:
    print ("Line 1 - a is not equal to b")
if ( a != b ):
    print ("Line 2 - a is not equal to b")
else:
    print ("Line 2 - a is equal to b")
if ( a < b ):
    print ("Line 3 - a is less than b" )
else:
    print ("Line 3 - a is not less than b")
if ( a > b ):
    print ("Line 4 - a is greater than b")
else:
    print ("Line 4 - a is not greater than b")

a,b=b,a     #values of a and b SWAPPED. a becomes 10, b becomes 22
print(a)
print(b)
if ( a <= b ):
    print ("Line 5 - a is either less than or equal to b")
else:
    print ("Line 5 - a is neither less than nor equal to b")
if ( b >= a ):
    print ("Line 6 - b is either greater than or equal to b")
else:
    print ("Line 6 - b is neither greater than nor equal to b")
print("\n\n")


#               Assignment Operator
a = 21
b = 10
c = 0
c = a + b
print ("Line 1 - Value of c is ", c)
c += a
print ("Line 2 - Value of c is ", c )
c *= b
print ("Line 3 - Value of c is ", c )
c /= a
print ("Line 4 - Value of c is ", c )
c = 2
c %= a
print ("Line 5 - Value of c is ", c)
c **= a
print ("Line 6 - Value of c is ", c)
c //= a
print ("Line 7 - Value of c is ", c, "\n\n")


#               Python Bitwise Operator
a = 60 # 60 = 0011 1100
b = 13 # 13 = 0000 1101
bin(a); bin(b)
print ('a = ',a,':',bin(a),' ||  b = ',b,':',bin(b))
c = 0
c = a & b; # 12 = 0000 1100
print ("result of AND is ", c,':',bin(c))
c = a | b; # 61 = 0011 1101
print ("result of OR is ", c,':',bin(c))
c = a ^ b; # 49 = 0011 0001
print ("result of EXOR is ", c,':',bin(c))
c = ~a; # -61 = 1100 0011
print ("result of COMPLEMENT is ", c,':',bin(c))
c = a << 2; # 240 = 1111 0000
print ("result of LEFT SHIFT is ", c,':',bin(c))
c = a >> 2; # 15 = 0000 1111
print ("result of RIGHT SHIFT is ", c,':',bin(c))
print("\n\n")


#                   Logical Operator
a = 10
b = 20
list = [1, 2, 3, 4, 5 ]
if ( a in list ):
    print ("Line 1 - a is available in the given list")
else:
    print ("Line 1 - a is not available in the given list")
if ( b not in list ):
    print ("Line 2 - b is not available in the given list")
else:
    print ("Line 2 - b is available in the given list")
c=b/a
if ( c in list ):
    print ("Line 3 - a is available in the given list")
else:
    print ("Line 3 - a is not available in the given list")


#               Python Identity Operator
#           Refers to Memory Location of a Variable
a = 20
b = 20
print ('Line 1','a=',a,':',id(a), 'b=',b,':',id(b))
if ( a is b ):
    print ("Line 2 - a and b have same identity")
else:
    print ("Line 2 - a and b do not have same identity")
if ( id(a) == id(b) ):
    print ("Line 3 - a and b have same identity")
else:
    print ("Line 3 - a and b do not have same identity")
b = 30
print ('Line 4','a=',a,':',id(a), 'b=',b,':',id(b))
if ( a is not b ):
    print ("Line 5 - a and b do not have same identity")
else:
    print ("Line 5 - a and b have same identity")
print("\n\n")

x = ["Ani", "Budi", "Cici"]
y = "Cici"
z = "Dodi"
print(y in x)               # True or False
print(z in x) 

x = ["Ani", "Budi", "Cici"]
y = "Cici"
z = "Dodi"
print(y not in x)           # True or False
print(z not in x)


# Python Operator Precedence
a = 20
b = 10
c = 15
d = 5
print ("a:%d b:%d c:%d d:%d" % (a,b,c,d ))
e = (a + b) * c / d                         # (30 * 15 ) / 5
print ("Value of (a + b) * c / d is ", e)
e = ((a + b) * c) / d                       # (30 * 15 ) / 5
print ("Value of ((a + b) * c) / d is ", e)
e = (a + b) * (c / d)                       # (30) * (15/5)
print ("Value of (a + b) * (c / d) is ", e)
e = a + (b * c) / d                         # 20 + (150/5)
print ("Value of a + (b * c) / d is ", e)
bilangan = (5 % 3 ** 2) + (3 + 2 * 2) * (4 - 2) 
print(bilangan)


# Membership Operator
x = 8 
y = 50
x >10 and y >10

x = 8 
y = 8 
x > 10 or y >10

i = True
j = False
i = not i
i
