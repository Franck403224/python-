# 5conditionals.py

# 5.1 If ... else

a = 20
b = 40

c=10
d=40

# 5.1.1 Print "Yes" if a is equal to b, otherwise print "No".
# TODO: Write your code below

a = 20
b = 40

if a == b:
    print("Yes")
else:
    print("No")



# 5.1.2 Print "1" if a is equal to b, print "2" if a is greater than b, otherwise print "3".
# TODO: Write your code below

a = 20
b = 40

if a == b:
    print("1")
elif a > b:
    print("2")
else:
    print("3")



# 5.1.3 Print "Hello" if a is equal to b, and c is equal to d.
# TODO: Write your code below

if a == b and c == d:
   print("hello")
  


# 5.1.4 Print "Hello" if a is equal to b, or if c is equal to d.
# TODO: Write your code below

if a == b or c == d:
   print("hello")


# 5.2 Write a program that checks whether an input number is odd or even. Print whether the input number is odd or even
# HINT:
# even numbers can be divided by 2 with no remainder. when odd numbers are divided by 2 there is a remainder.
# eg. 42 is even because 42/2 = 21 and has no remainder
# eg. example, 33 is odd because 33/3 = 16.5 is not a whole number.
# we can use the module operator (%) in python to get the remainder after a division.
# eg. 5%2 = 1 since 5 divided by 2 has a remainder 1. So 5 is odd
# eg. 6%2 = 0 since 6 divided by 2 has a remainder 0. So 6 is even.

#number to check
number = int(input('Enter a number'))

# TODO: write your code below
if number % 2 == 0:
   print('even number')
else:
   print('Odd number')