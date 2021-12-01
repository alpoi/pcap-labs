# write a program that takes three arguments. it should take an input and check if it's in the given range. 
# it should prompt the user when the string entered is not an integer, and ask them again.
# it should prompt the user when the string is not in the range
# if the input is valid, it should return it as such

def read_int(prompt, min, max):
    while True:
        try:
            num = int(input(prompt))

            if min > max:
                min, max = max, min
                print("> 'min' was larger than 'max', so they were swapped.")

            assert min <= num <= max
            return num
        except ValueError:
            print("> Error: wrong input, try again!")
        except AssertionError:
            print("> Error: the value is not within the permitted range, [" + str(min) + "," + str(max) + "].")


v = read_int("> Enter an integer from -10 to 10: ", -10, 10)
print("> The number is: ", v)

# in the lab instruction, function layout was specified to take prompt as an input
# but the only part of the prompt that should change are the range values,
# so I think it might be better if the prompt is within the function, since we can then put the range in the prompt 


def better_read_int(min, max):
    while True:
        try:
            min, max = int(min), int(max) # raises ValueError if not possible
            if min > max:
                min, max = max, min
                print("> 'min' was larger than 'max', so they were swapped.")
            break
        except ValueError:
            return("> The values for min and max must be integers! \n> Your minimum had " + str(type(min)) + "\n> Your maximum had " + str(type(max)))
            
    while True:
        try:
            num = int(input("> Enter an integer value in the range [" + str(min) + "," + str(max) + "]: "))
            assert min <= num <= max
            return("> " + str(num) + " is in the given range, [" + str(min) + "," + str(max) + "]!")
        except ValueError:
            print("> Error: wrong input, try again!")
        except AssertionError:
            print("> Error: " + str(num) + " is not within the permitted range, [" + str(min) + "," + str(max) + "].")
        except BaseException as exc: # Just incase
            print(exc)
            

print(better_read_int("lemon",-12)) # tells the invoker that their minimum was a string instead of an integer