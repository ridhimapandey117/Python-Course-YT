#Simple Arthemetic
print(49+51)

#Printing
# Lines that start with hashtags are comments
# Write your code below that prints out "Hello World"
# Make sure your spacing and capitalization matches.
print("Hello World")

#String indexing
# Write your string index below
# Start with 'Hello World'
# and make sure to match spaces and capitalization exactly
print("Hello World"[8])

#String Splicing
print('tinker'[1:4])

#////////////////////////////////////////
#Examples they have in Lesson 24. Print Formatting With Strings
#////////////////////////////////////////

print("The {g} {a} {f}".format(f = "fox", a = "brown", g = "agile"))

#rounding
result = 100/777
print("The result was {r:.2f}".format(r = result))

#f-strings
name = "jose"
age = 86
print(f"{name} is {age} years old")

#Coding Exercise 5: Print Formatting
print("Python {r}".format(r = "rules!"))

#/////////////////////////////////////
#Examples they have in Lesson 26. Lists
#/////////////////////////////////////
my_list = [1,2,3]
print(len(my_list))

myList = ['one', 'two', 'three']
print(myList[0]) #getting one value from list
print(myList[1:]) #getting values starting from element 1 and onwards

another_list = ['four', 'five']
print(myList + another_list) #can combine lists just like that

my_list[0] = 'ALL CAPS'
print(my_list) #can replace values

myList.append('six') #adds value to the end of the list
print(myList)

myList.pop() #will take out value at last index

#/////////////////////////////////////
#Examples they have in Lesson 28: Dictionaries
#/////////////////////////////////////

my_dict = {'key1':'value1','key2':'value2'}
print(my_dict['key1'])

d = {'k1': 123, 'k2':[0,1,2],'k3':{'insideKey': 100}}
print(d['k3']['insideKey'])
print(d['k2'][2])

letter = "c"
print(letter.upper()) #makes uppercase
print(letter.lower()) #makes lowercase

#/////////////////////////////////////
#Examples they have in Lesson 30: Tuples
#/////////////////////////////////////

t = (1,2,3)

t = ('one', 2)
print(t[0])

t = ('a', 'a', 'b')
print(t.count('a')) #counts how many times 'a' appears in the tuple
print(t.index('a')) #returns the first time 'a' appears

#CANNOT CHANGE THE VALUES IN THE TUPLES

#/////////////////////////////////////
#Examples they have in Lesson 31: Sets
#/////////////////////////////////////

#List but nothing can be repeated

myset = set()
myset.add(1)
myset.add(2)
myset.add(2) #will not show this again
print(myset)

mylist = [1,1,1,1,1,1,2,2,2,2,2,3,3,3]
print(set(mylist)) #prunes all repeats in the list

#/////////////////////////////////////
#Examples they have in Lesson 39. If, Elif, Else Statements
#/////////////////////////////////////

hungry = True

if (hungry):
    print('FEED ME')
else:
    print("I'm full")

loc = 'Bank'
if loc == 'Auto Shop':
    print('Cars are cool!')
elif (loc == 'Bank'):
    print('Money is cool!')
else:
    print('I do not know much.')
