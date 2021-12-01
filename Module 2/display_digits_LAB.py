# build a seven-segment display, like on an alarm clock
# it should take any non-negative integer and output what a clock would show

# display is a list of dictionaries relating digits to their corresponding display on each row (i.e. display[0] contains the dictionary for the 1st row, and so on)

display = [ {
        '1' : "#",
        '2' : "###",
        '3' : "###",
        '4' : "# #",
        '5' : "###",
        '6' : "###",
        '7' : "###",
        '8' : "###",
        '9' : "###",
        '0' : "###"
        } ,

{
        '1' : '#',
        '2' : '  #',
        '3' : '  #',
        '4' : '# #',
        '5' : '#  ',
        '6' : '#  ',
        '7' : '  #',
        '8' : '# #',
        '9' : '# #',
        '0' : '# #'
        } ,

{
        '1' : '#',
        '2' : '###',
        '3' : '###',
        '4' : '###',
        '5' : '###',
        '6' : '###',
        '7' : '  #',
        '8' : '###',
        '9' : '###',
        '0' : '# #'
        } ,

{
        '1' : '#',
        '2' : '#  ',
        '3' : '  #',
        '4' : '  #',
        '5' : '  #',
        '6' : '# #',
        '7' : '  #',
        '8' : '# #',
        '9' : '  #',
        '0' : '# #'
        } ,

{
        '1' : '#',
        '2' : '###',
        '3' : '###',
        '4' : '  #',
        '5' : '###',
        '6' : '###',
        '7' : '  #',
        '8' : '###',
        '9' : '###',
        '0' : '###'
        } ]


def digitise():
    while True:
        try:
            num = int(input("> Enter a number to digitise: ")) # returns ValueError if the input string is not an integer
            char_list = list(str(num))
            for i in range(5):
                for char in char_list:
                    print(display[i][char].replace( "#" , "\u2588" ), end = ' ') # replace because hashes look gross
                print(" ")
            break
        except ValueError:
            print("> You must enter an integer. Try again!")


digitise()