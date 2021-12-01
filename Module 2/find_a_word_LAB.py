# take two inputs, one being a word and another being any combination of characters (both ordered)
# determine if the first word is in the second

def find_a_word( word , string ):
    pos = 0
    index = 0
    for substr in word:
        catch = string[pos:]
        index += 1 # to keep track of where it went wrong, avoiding the issue .index(substr) raises with repeated characters
        pos = string.find(substr, pos)

        if pos == -1:
            return ("> Sorry - '" + word + "'" " is not hidden in " + "'" + string + "'." + 
                    "\n> We found " + "'" + word[:index - 1] + "', but we could not find '" + 
                    word[index - 1:] + "' in the remaining string, " + "'" + catch + "'.") 
        
    return ("> '" + word + "'" " is hidden in " + "'" + string + "'!")

print(find_a_word("donor","Nabucodonusur"))

#  also implemented a response indicating how much of the word was found, and what could not be found with the remaining string.