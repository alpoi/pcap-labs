# ask user for input file's name (path)
# reads the file (if possible) and counts all Latin letters (lower/upper treated as equal)
# prints a histogram in alphabetical order
# second lab: print from largest to smallest
# save to file with original name, appended by .hist

from os import strerror
from io import StringIO # using this to change stdout to our .hist file
import sys

count = {}
# srcname = input("> Enter path to source file: ")
srcname = "samplefile.txt"
try:
    src = open(srcname, 'r')
    char = '.'
    while char != '':
        char = src.read(1).upper()
        if not char.isalpha():
            pass
        elif char not in count.keys():
            count[char] = 1
        else:
            count[char] += 1
        # print(char, end='')
    src.close()

except IOError as exc:
    print("> Cannot open source file: ", strerror(exc.errno))
    exit(exc.errno)
    
# count = dict( sorted( count.items() ) )
count = dict( sorted( count.items(), key = lambda x: x[1], reverse = True ) ) # items() gives a tuple (key, value), then lambda function used to sort by value

catch = StringIO() # create StringIO object for in-memory text stream
sys.stdout = catch # use this to catch stdout

for key in count.keys():
    print(key + " (" + str(count[key]) + ")", "\t", end='')
    [print("\u2588", end='') for i in range(count[key])]
    print("")

sys.stdout = sys.__stdout__ # restore stdout to the default (our terminal)

try:
    hist = open(srcname + '.hist', 'w', encoding="UTF-8") # encoded so it saves the \u2588 without freaking out
    hist.write(catch.getvalue()) # writes what was printed while we used catch in place of stdout
    hist.close()
except IOError as exc:
    print("> Cannot open destination file: ", strerror(exc.errno))
    exit(exc.errno)