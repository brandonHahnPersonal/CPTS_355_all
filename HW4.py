#------------------------- 10% -------------------------------------
# The operand stack: define the operand stack and its operations

opstack = []  #assuming top of the stack is the end of the list

# Now define the helper functions to push and pop values on the opstack
# (i.e, add/remove elements to/from the end of the Python list)
# Remember that there is a Postscript operator called "pop" so we choose
# different names for these functions.
# Recall that `pass` in python is a no-op: replace it with your code.

def opPop():
    # opPop should return the popped value.
    # The pop() function should call opPop to pop the top value from the opstack, but it will ignore the popped value.
    topPopped = opstack.pop() # leverage the python list built in 'pop' method in helper
    return topPopped

def opPush(value):
    # opPush should not return a value
    # push() should call this to push a value onto the top of the stack.
    opstack.append(value) # leverage the python list built in 'append' method in helper
    # note the top of the stack is assumed to be the end of the list

#-------------------------- 20% -------------------------------------
# The dictionary stack: define the dictionary stack and its operations
dictstack = []  #assuming top of the stack is the end of the list

# now define functions to push and pop dictionaries on the dictstack, to
# define name, and to lookup a name

def dictPop():
    dictionaryPopValue = dictstack.pop()
    return dictionaryPopValue
    # dictPop pops the top dictionary from the dictionary stack.

def dictPush(d):
    #dictPush pushes the dictionary ‘d’ to the dictstack.
    #Note that, your interpreter will call dictPush only when Postscript
    #“begin” operator is called. “begin” should pop the empty dictionary from
    #the opstack and push it onto the dictstack by calling dictPush.
    dictstack.append(d)

def define(name, value):
    #add name:value pair to the top dictionary in the dictionary stack.
    #Keep the '/' in the name constant.
    #Your psDef function should pop the name and value from operand stack and
    #call the “define” function.
    newDictItem = {name: value}
    dictPush(newDictItem)

def lookup(name):
    # return the value associated with name
    # What is your design decision about what to do when there is no definition for “name”? If “name” is not defined, your program should not break, but should give an appropriate error message.
    trueName = '/' + name
    for item in dictstack:
        if trueName in item:
            returnVal =  item.get(trueName) #actual items have the / in front.
            return returnVal

    # if there is no definition for 'name', then throw an error message:
    Error_000_message = 'ERROR 000: THERE IS NO DEFINITION FOR ' + trueName 
    print()
    print(Error_000_message)
    print()
    return ();



#--------------------------- 10% -------------------------------------
# Arithmetic and comparison operators: add, sub, mul, div, mod, eq, lt, gt
# Make sure to check the operand stack has the correct number of parameters
# and types of the parameters are correct.
def add():
    a = opPop()
    b = opPop()
    if ((type(a) == float | int) and (type(b) == float) | (int):
        result = a + b
        opPush(result)
    else:
        opPush(b)
        opPush(a)
    
    return None

def sub():
    a = opPop()
    b = opPop()
    if ((type(a) == float | int) and (type(b) == float | int)):
        result = a - b
        opPush(result)
    else:
        opPush(b)
        opPush(a)
    
    return None

def mul():
    pass

def div():
    pass

def mod():
    pass

def eq():
    pass

def lt():
    pass

def gt():
    pass

#--------------------------- 15% -------------------------------------
# String operators: define the string operators length, get, getinterval, put
def length():
    pass

def get():
    pass

def getinterval():
    pass

def put():
    pass

#--------------------------- 25% -------------------------------------
# Define the stack manipulation and print operators: dup, copy, pop, clear, exch, roll, stack
def dup():
    pass

def copy():
    pass

def pop():
    pass

def clear():
    pass

def exch():
    pass

def roll():
    pass

def stack():
    pass

#--------------------------- 20% -------------------------------------
# Define the dictionary manipulation operators: psDict, begin, end, psDef
# name the function for the def operator psDef because def is reserved in Python. Similarly, call the function for dict operator as psDict.
# Note: The psDef operator will pop the value and name from the opstack and call your own "define" operator (pass those values as parameters).
# Note that psDef()won't have any parameters.

def psDict():
    pass

def begin():
    pass

def end():
    pass

def psDef():
    #pop 2 from op stack, call define to put a tuple onto dict stack
    tempValue = opPop();
    tempName = opPop();
    define(tempName,tempValue)
    pass