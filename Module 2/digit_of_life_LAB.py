# take a number (as a string), add its digits together, then add those digits together

def dol(x):

    if type(x) == int:
        x = str(x)

    if type(x) == float:
        x = str(x).replace(".","")

    if not x.isdigit():
        return "> Your input must be a digit"
    else:
        while len(x) > 1:
            x = str(sum([int(i) for i in list(x)]))
        return x[0]





