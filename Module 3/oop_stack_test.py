from oop_stack import Stack

class PrintStack(Stack):
    def __init__(self, name = "unnamed stack"):
        Stack.__init__(self)
        self.__stackName = str(name) # object instanciation now has another parameter
    
    def push(self, var):
        Stack.push(self, var)
        print(">", var, "has been pushed to", self.__stackName)
    
    def pop(self):
        var = Stack.pop(self)
        print(">", var, "has been popped from", self.__stackName)
        return var

    def poppush(self, destination):
        var = Stack.pop(self)
        Stack.push(destination, var)
        print(">", var, "has been popped from", self.__stackName, "and pushed to", destination.__stackName)

obj_1 = PrintStack("obj_1")
obj_2 = PrintStack("obj_2")

obj_2.push("coin")
obj_2.poppush(obj_1) # pops the "coin" from obj_2 and pushes it into obj_1
obj_1.pop() # proof that it worked