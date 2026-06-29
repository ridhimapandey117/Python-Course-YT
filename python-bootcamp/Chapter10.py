#/////////////////////////////////////
#Errors and Exception Handling
#/////////////////////////////////////

#try: block of code that will be attempted (which may be prone to an error)

#except: This block will execute when the try block experiences an error

#finally: The final block that will always be executed, regardless of an error

try:
    #want to attempt this code, but it may have an error
    result = 10 + 10

except:
    print("Hey it looks like you aren't adding correctly!")

finally:
    print("Add went well!")
    print(result)

#When running below situation, we get "I always run" since no error has occured with our testfile
#If we replace 'w' with 'r', we'll get the OSError statement ALONGSIDE the finally statement since finally will always run no matter what

try:
    f = open('testfile', 'w')
    f.write("Write a test line")
except TypeError: #Except block will only execute if a TypeError occurs
    print("There was a type error!")

except OSError:
    print("Hey you have an OS Error")

finally:
    print("I always run")


def ask_for_int():

    while True: #True meaning while an exception error is still happening
        try:
            result = int(input("Please provide number: "))
        except:
            print("Whoops! That is not a number")
            continue
        else: #You can also pair else statements with except
            print("Yes, thanks!!!")
            break
        finally:
            print("End of try/except/finally")


#/////////////////////////////////////
#Errors and Exception Problems
#/////////////////////////////////////

#Problem 1
try:
    for i in ['a', 'b', 'c']:
        print(i**2)
except:
    print("An error occured!")

#Problem 2
x = 5
y = 0

try:
    z = x/y
except ZeroDivisionError:
    print("Oops, looks like a Zero Division Error occured!")
finally:
    print("All done!")

#Problem 3
def ask():
    while True:
        try:
            num = int(input("Input an integer: "))
        except:
            print("An error occured. Please try again!")
            continue
        else:
            print(f"Thank you, your number squared is: {num**2}")
            break

ask()