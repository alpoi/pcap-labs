# write a cipher that shifts characters by a user specified value between 1 ... 25 inclusive
# preserve case and leave non-alphabetical characters unchanged
# ord('A') = 65
# ord('Z') = 90
# ord('a') = 97
# ord('z') = 122

def cipher():
    text = input("> Enter your message: ")
    while True:

        # error handling begins

        try:       
            shift = int(input("> Enter a shift value from 0 to 25: "))
        except ValueError:
            print( "> You did not enter an integer. Try again!" )
            continue
        if not (0 <= shift <= 25):
            print( "> Your shift value, " + str(shift) + ", is not in the required 0-25 range. Try again!" )
            continue

        # error handling ends

        cipher = ''
        for char in text:
            if not char.isalpha():
                cipher+= char
                continue
            if char.isupper():
                code = ord(char) + shift
                if code > ord('Z'):
                    code -= 25
                cipher += chr(code)
            elif char.islower():
                code = ord(char) + shift
                if code > ord('z'):
                    code -= 25
                cipher += chr(code)
        print(cipher)
        break

cipher()



