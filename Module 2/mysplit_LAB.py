# write function that behaves like split()
# should accept one string argument
# return list, divided by whitespaces
# empty string should give empty list

def mysplit(string, debug = False):
    user_string = string.strip()

    if debug == True:
        print("> user_string is '" , user_string , "'")

    split_list = [""]
    if user_string.isspace():
        return []

    for char in user_string:
        if char.isspace() and split_list[-1].isspace(): # multiple spaces in a row should be treated as a single space
            continue
        elif char.isspace() and not split_list[-1].isspace(): # begins a new word
            if debug == True: 
                print("> current word is" , split_list[-1] , "at" , char.index())
            split_list.append("")
        else:
            split_list[-1] += char
    return split_list




print(mysplit("To be or not to be, that is the question"))
print(mysplit("To be or not to be,that is the question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))
