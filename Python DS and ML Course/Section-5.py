'''
- NumPy is a linear algebra library for python
- Almost all libraries rely on NumPy

- Numpy arrays can either be a 1d array or 2d array (vector and matrices respectfully)
'''

my_list = [1,2,3]

import numpy as np
print(np.array(my_list))
ingo in mylist:
print(flamingo)

# Filtering values in list
for num in mylist:
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd number: {num}')

#/////////////////////////////////////
#Examples they have in Lesson 40. For Loops
#/////////////////////////////////////

list_sum = 0

for num in mylist:
    list_sum += num
    print(list_sum)

# using strings in for loops (each iteration is a character in the string)
for letter in 'whole':
    print(letter)

tup = (1,2,3,4)
for item in tup:
    print(item)

#tuple unpacking: Duplicate the structure of the tuples and "unpack" the contents (by printing them out separately)
mylist = [(1,2), (3,4), (5,6),(7,8)]
print(len(mylist))

for a,b in mylist:
    print(a)
    print(b)

print()

#my own thing applying tuple unpacking

name_age_job = [("Jimmy", 49, "Accountant"), ("Samantha", 28, "Civil Lawyer"), ("Satvik", 36, "VFX animator")]

print("Names of New Hires:")
for a,b,c in name_age_job:
    print(a)

#iteration thru dictionary
#will automatically print the keys
d = {'k1':1, 'k2':2, 'k3':3}
for item in d:
    print(item)

#to iterate items
for a,b in d.items():
    print(b)

#doing .items will convert the dictionary layout to that of a tuple one, application of tuple unpacking possible


#/////////////////////////////////////
#Examples they have in Lesson 41. While Loops
#/////////////////////////////////////

x = 0
while x < 5:
    print(f'The current value of x is {x}')
    x += 1
else:
    print('X is not less than 5')

#break: breaks out of the current closest enclosing loop

x = 0
while x < 5:
    print(x)
    x += 1
    if x == 2:
        break

#continue: goes to the top of the closest enclosing loop

mystring = 'Sammy'
for letter in mystring:
    if letter == 'a':
        continue
    print(letter)

def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'EVEN'
    else:
        return mystring[0]

names = ['Samantha', 'Jose', "Garrett", "Lindsay"]
print(list(map(splicer, names)))

#filter function; returns items that meet the requirement of the filter
def check_even(num):
    return num%2 == 0

mynums = [1,2,3,4,5,6] #Using filter function to only select the even numbers here
print(list(filter(check_even,mynums))) #The function used in filter() needs to return a boolean

#Lambda Expressions (not every method can be translated into one
def square(num): return num ** 2
square = lambda num: num ** 2 #lambda expression functions like statement above
square(2)
