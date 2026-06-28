
#/////////////////////////////////////
#Examples they have in Lesson 46-50 Methods
#/////////////////////////////////////

#how to discover built in methods on ur own
mylist = [1,2,3]
help(mylist.insert) #help will tell u how the built-in method works

#creating methods

def say_hello():
    print("hello!!!")

say_hello()

def say_hello(name='Default'): #if the name isn't provided in the parenthesis, it'll assign name as 'Default' automatically
    print(f'Hello {name}!!!')

say_hello('Jose')
say_hello() #will print Hello Default!!!

def add_num(num1,num2): #parameters don't specify data type so make sure to convert the data into the type u want within the method
    return int(num1)+int(num2)

result = add_num('20','70')
print(result)

#/////////////////////////////////////
#Examples they have in Lesson 51. Logic w/ Functions
#/////////////////////////////////////

def even_check_list(num_list):
    even_list = []

    for nums in num_list:
        if nums % 2 == 0:
            even_list.append(nums)
        else:
            pass
    return even_list

mylist = [3,5,2,442,28328]

print(even_check_list(mylist))

#/////////////////////////////////////
#Examples they have in Lesson 52. Tuple Unpacking w/ Functions
#/////////////////////////////////////

work_hours = [('Abby', 100), ('Billy', 200), ('Cassie',800)]

def employee_award(list):
    max = 0
    month = ''

    for name,hours in list:
        if hours > max:
            max = hours
            month = name
        else:
            pass

    return(month, max)

names,hours = employee_award(work_hours) #can do tuple unpacking in function calling
print(names)

#/////////////////////////////////////
#Examples they have in Lesson 53. Interactions w/ Python Functions
#/////////////////////////////////////

from random import shuffle
def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

def player_guess():
    guess = ''

    while guess not in ['0', '1', '2']:
        guess = input("Pick a number: 0,1, or 2 ")

    return int(guess)

def check_guess(mylist, guess):
    if mylist[guess] == 'O':
        print("Correct")
    else:
        print("Wrong guess!")
        print(mylist)


mylist = [' ', 'O', ' ']

shuffle_list(mylist)
player_index = player_guess()
check_guess(mylist, player_index)


#/////////////////////////////////////
#Examples they have in Lesson 55. *args and **kwargs
#/////////////////////////////////////

#*args allows any number of parameters to be entered and will treat all values entered as a tuple
def myfunc(*args):
    return sum(args) * 0.05

print(myfunc(1,5,634))

#**kwargs builds a dictionary of key value pairs
def myfunc(**kwargs):
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print('I did not find any fruit here')

myfunc(fruit='apple')

#combination of args and kwargs

def myfunc(*args, **kwargs):
    print('I would like {} {}'.format(args[0], kwargs['food']))

myfunc(10,31,353,32,fruit='orange',food='eggs',animal='dog') #everything here has to be in the same order described in the method (first args, then kwargs)


#/////////////////////
# Functions Practice Problems
#/////////////////////

#Warmup

#Lesser of Two Evens
def lesser_of_two_evens(num1,num2):
    if num1 % 2 == 0:
        if num2 % 2 == 0:
            if num1 > num2:
                return num2
            else:
                return num1
        else:
            if num1 > num2:
                return num1
            else:
                return num2
    else:
        if num1 > num2:
            return num1
        else:
            return num2

#Animal Crackers
def animal_crackers(animalString):
    words = animalString.split(" ")
    letter1 = words[0][0:1]
    letter2 = words[1][0:1]

    if (letter1 == letter2):
        return True
    else:
        return False

#Makes Twenty

def makes_twenty(num1,num2):
    if num1 == 20 or num2 == 20:
        return True
    else:
        if int(num1)+int(num2) == 20:
            return True
        else:
            return False

#Level 1

#Old Macdonald
def old_macdonald(string):
    new_string = ''
    i=0
    for letter in string:
        if i == 0 or i == 3:
            new_string = new_string + letter.upper()
            i += 1
        else:
            new_string = new_string + letter
            i += 1

    return new_string

#Master Yoda //
def master_yoda(string):
    i = 0
    the_list = string.split(" ")


    for letters in the_list:
        i += 1

    new_list = []

    i = i - 1

    while (i != 0):
        for letters in the_list:
            new_list.append(the_list[i])
            i -= 1

    return ' '.join(new_list)

#Almost There
def almost_there(n):
    if n-100 <= 10 or 100-n <= 10 or n-200 <= 10 or 200-n <= 10:
        return True
    else:
        return False

#Level 2

#Find 33
def has_33(nums):
    pass

#Paper Doll
def paper_doll(text):
    wordlist = []
    for letter in text:
       wordlist.append(letter)
    word = ''
    i = 0

    for letter in wordlist:
        word += wordlist[i]
        word += wordlist[i]
        word += wordlist[i]
        i += 1


    return word

#BlackJack
def blackjack(num1,num2,num3):
    numlist = [num1, num2, num3]
    sumnumbers = num1 + num2 + num3
    if (sumnumbers <= 21):
        return sumnumbers
    else:
        i = 1
        for number in numlist:
            if number == 11:
                return sumnumbers - 10
            elif number != 11 and i != 3:
                continue
                i += 1
            else:
                return 'BUST'

#Summer of 69
def summer_69(arr):

    actual = 0
    skip = False

    for number in arr:
        if number == 6:
            skip = True
        elif number == 9 and skip:
            skip = False
        elif not skip:
            actual += number

    return actual

#Challenging Problems

#Spy Game
def spy_game(nums):
    spy = ''
    str_nums = str(nums)

    for number in str_nums:
        if number == '0' or number == '7':
            spy += number
            continue
        else:
            continue

    if spy == '007':
        return True
    else:
        return False

#Count Primes
def count_primes(num):
    count = 0

    for number in range(2, num + 1):
        for divisor in range(2, int(number ** 0.5) + 1):
            if number % divisor == 0:
                break
        else:
            count += 1

    return count


#/////////////////////////////////////
#Examples they have in Lesson 61. Lambda Expressions Map and Filter
#/////////////////////////////////////

def square(num):
    return num**2

# You can use map() to quickly iterate through lists if u want to apply a function to all values
my_nums = [1,2,3,4,5]
for item in map(square, my_nums):
    print(item)

print(list(map(square, my_nums)))
#Don't put parenthesis on functions when using map since map will run the function anyway

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

#Often will use lambda with map and filter
list(map(lambda num: num **2, mynums))

#coverting check even into a lambda expression
print(list((filter(lambda num : num % 2 == 0, mynums))))


print(list(map(lambda string : string[::-1], names)))

#/////////////////////////////////////
#Methods and Functions Homework
#/////////////////////////////////////

#Volume of a sphere
def vol(rad):
    return float((4/3)*3.14*(rad**3))

#range checker
def ran_check(num, low, high):
    if low <= num and num <= high:
        return True
    else:
        return False

#Case counter
def up_low(s):
    uppercase = 0
    lowercase = 0
    for letter in s:
        if letter.isupper():
            uppercase += 1
            continue
        elif letter.islower():
            lowercase += 1
            continue
        else:
            continue

    print(f"No. of Uppercase characters: {uppercase}")
    print(f"No. of Lowercase characters: {lowercase}")

#List
def unique_list(lst):
    return list(set(lst))

#Multiply
def multiply(numbers):
    product = 1

    for number in numbers:
        product *= number
        continue
    return product

#Palindrome checker
def palindrome(s):
    s = s.replace(' ', '')
    if s == s[::-1]:
        return True
    else:
        return False

#HARD: Check for pangram
import string
def ispangram(str1, alphabet=string.ascii_lowercase):
    con_str1 = set(str1.replace(" ", "").lower())
    alphabet = set(alphabet)
    return con_str1 == alphabet


