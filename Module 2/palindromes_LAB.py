# write a palindrome detector

def isPalindrome(x):
    sanitised = string.lower().replace(" ", "").replace("\n", "") # second replace to handle newlines. there are other whitespaces that are unhandled here
    print(sanitised[::-1])
    if sanitised == sanitised[::-1]:
        print("> '" + string + "' is a palindrome!")
    else:
        print("> '" + string + "' is not a palindrome...")

string = input("> Enter your string: ")

# string = '''ten
# animals
# i slam in
# a
# net'''

isPalindrome(string)