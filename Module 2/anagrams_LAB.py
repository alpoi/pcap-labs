# write an anagram detector

def areAnagrams(first, second):
    first_san = list(first.lower().replace(" ", "").replace("\n", "")).sort() # turns both into lists then sorts them
    second_san = list(second.lower().replace(" ", "").replace("\n", "")).sort()
    if first_san == second_san:
        print("> '" + first + "' and '" + second + "' are anagrams!")
    else:
        print("> '" + first + "' and '" + second + "' are not anagrams...")

first = input("> Enter your first string: ")
second = input("> Enter your second string: ")

areAnagrams(first, second)