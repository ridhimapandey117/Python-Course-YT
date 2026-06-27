
#/////////////////////////////////////
#Examples they have in Lesson 39. If, Elif, Else Statements
#/////////////////////////////////////

mylist = [1,2,3,4,5,6,7,8,9,10]
for flamingo in mylist:
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

#pass: does nothing at all; placeholder to avoid syntax error

x = [1,2,3]
for item in x:
    pass

print ('end of my script')

#/////////////////////////////////////
#Examples they have in Lesson 42. Useful Operators
#/////////////////////////////////////

#///
#range
mylist = [1,2,3]

for num in range(3,10):
    print(num)
    #starts at 3 and goes all the way up to, not-including, 10; similar to substring

#step sizes are also there but range can be used without it
for num in range(0,11,2):
    print(num)

print(range(0,11,2)) #will just print out range(0,11,2)
print(list(range(0,11,2))) #prints normally but numbers are in list format

#ennumerate; does an index count of whatever in tuple form
index_count = 0
word = 'abcde'
for item in enumerate(word):
    print(item)

#can apply tuple unpacking
for i,l in enumerate(word):
    print(i)

#///
#zip; zips together two lists, can also apply tuple unpacking (doesn't have to include just two lists)

#if lists are uneven, it'll print the result amount of the smallest list size
#Example: list1 size is 3, list2 size is 5, and list3 size is 9, when using zip, 3 results will print
mylist1 = [1,2,3]
mylist2 = ['a','b','c']
mylist3 = [100,200,300]
for i,l,n in zip(mylist1,mylist2,mylist3):
    print(i)
    print(l)
    print(n)
    print("\n")

#///
#in-operator; checks if a value is in a list,dictionary (works for iterable types like int and str)
print('x' in [1,2,3])

mylist = [3,4,6,2,63,856,53454]
print(3 in mylist)

#///
#dictionary
print('my' in {'my':373})
d = {'my':373}

print(345 in d.values()) #if u want to specifically look for values; .keys() is for keys

#///
#min (minimum); finds min value
mylist = [10,20,30,40,100]
print(min(mylist))

#///
#max (maximum(; finds max value
print(max(mylist))

#///
#random library
from random import shuffle
mylist = [1,2,3,4,5,6,7]
shuffle(mylist) #shuffles nums around randomly; can be called many times
print(mylist)

from random import randint
randint(0,100) #grabs random integer from this range, inclusive (like math.random but easier)

#///
#input (like Scanner) but it'll convert the input into string
pi = input("Enter a number here: ")
print(pi)

#to convert it back, do float() or int()

#/////////////////////////////////////
#Examples they have in Lesson 43. List Comprehensions
#/////////////////////////////////////

#append will append an iterable object into the list
mylist = []
mystring = 'hello'

for letter in mystring:
    mylist.append(letter)

#or

mylist = [letter for letter in mystring]

#you can perform operations with the shortcut method

mylist = [num**2 for num in range(0,11)]
print(mylist)

#can also if statements
mylist = [x for x in range(0,11) if x%2==0] #will include numbers in 0,11 ONLY IF they're divisible by 2 in mylist
print(mylist)

#can use for loops
celcius = [0,10,20,30]
fahrenheit = [((9/5)*temp + 32) for temp in celcius]
print(fahrenheit)

fahrenheit = []
for temp in celcius:
    fahrenheit.append(((9/5)*temp + 32))
print(fahrenheit)

#can do nested loops
#reg nested loop
mylist = []
for x in [2,4,6]:
    for y in [100,200,300]:
        mylist.append(x*y)
print(mylist)

#oneliner for nested loop
mylist = [x*y for x in [2,4,6] for y in [100,200,300]]
print(mylist)










