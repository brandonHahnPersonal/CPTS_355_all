#PROGRAM NAME: HW4
#AUTHOR: Brandon Hahn
#DATE COMPLETED: 3/30/2022
#DESCRIPTION: This is a python file that holds the methods created for
    #postscript part 1 in CPTS 355

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
    if(len(opstack)>= 1):
        topPopped = opstack.pop() # leverage the python list built in 'pop' method in helper
        return topPopped

    else:
        Error_000_message = 'ERROR 000: POP PERFORMED ON EMPTY LIST'
        print()
        print(Error_000_message)
        print()
        return None;


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
    if(len(dictstack)>=1):
        dictionaryPopValue = dictstack.pop()
        return dictionaryPopValue

    else:
        return None
    # dictPop pops the top dictionary from the dictionary stack.

def dictPush(d):
    #dictPush pushes the dictionary ???d??? to the dictstack.
    #Note that, your interpreter will call dictPush only when Postscript
    #???begin??? operator is called. ???begin??? should pop the empty dictionary from
    #the opstack and push it onto the dictstack by calling dictPush.
    dictstack.append(d)
    return None

def define(name, value):
    #add name:value pair to the top dictionary in the dictionary stack.
    #Keep the '/' in the name constant.
    #Your psDef function should pop the name and value from operand stack and
    #call the ???define??? function.
    newDictItem = {name: value}
    dictPush(newDictItem)
    return None

def lookup(name):
    # return the value associated with name
    # What is your design decision about what to do when there is no definition for ???name???? If ???name??? is not defined, your program should not break, but should give an appropriate error message.
    trueName = '/' + name
    for item in dictstack:
        if trueName in item:
            returnVal =  item.get(trueName) #actual items have the / in front.
            return returnVal

    # if there is no definition for 'name', then throw an error message:
    Error_001_message = 'ERROR 001: THERE IS NO DEFINITION FOR ' + trueName 
    print()
    print(Error_001_message)
    print()
    return None;



#--------------------------- 10% -------------------------------------
# Arithmetic and comparison operators: add, sub, mul, div, mod, eq, lt, gt
# Make sure to check the operand stack has the correct number of parameters
# and types of the parameters are correct.
def add():
    a = opPop()
    b = opPop()
    if (((type(a) == float) | (type(a) == int)) and ((type(b) == float) | (type(b) == int))): # if the variables are addable
        result = a + b
        opPush(result)
    else: # if they are not of type num, restore the opstack
        opPush(b)
        opPush(a)
    
    return None

def sub():
    a = opPop()
    b = opPop()
    if (((type(a) == float) | (type(a) == int)) and ((type(b) == float) | (type(b) == int))):
        result = b - a
        opPush(result)
    else:
        opPush(b)
        opPush(a)
    
    return None

def mul():
    a = opPop()
    b = opPop()
    if (((type(a) == float) | (type(a) == int)) and ((type(b) == float) | (type(b) == int))):
        result = a * b
        opPush(result)
    else:
        opPush(b)
        opPush(a)
    
    return None

def div():
    a = opPop()
    b = opPop()
    if (((type(a) == float) | (type(a) == int)) and ((type(b) == float) | (type(b) == int))):
        result = b/a #division operation
        opPush(result)
    else:
        opPush(b)
        opPush(a)
    
    return None

def mod():
    a = opPop()
    b = opPop()
    if (((type(a) == float) | (type(a) == int)) and ((type(b) == float) | (type(b) == int))):
       result = b % a #python built in modulus
       opPush(result)
    else:
        opPush(b)
        opPush(a)
    
    return None


def eq():
    a = opPop()
    b = opPop()
    if (a == b):
       result = True
    else:
        result = False
    
    opPush(result) # results are stored on the opstack
    return None

def lt():
    a = opPop()
    b = opPop()
    if (a > b):
       result = True
    else:
        result = False
    
    opPush(result)
    return None

def gt():
    a = opPop()
    b = opPop()
    if (a < b):
       result = True
    else:
        result = False
    
    opPush(result)
    return None

#--------------------------- 15% -------------------------------------
# String operators: define the string operators length, get, getinterval, put
def length():
    a = opPop()
    if (type(a) == str):
       index = 0
       stringCopy = ""
       while index < len(a):
          char = a[index]
          if ((char != ')') & (char != '(')):            
            stringCopy = stringCopy + char # reverses string, but OK since only care about length
        
          index = index + 1;

       result = len(stringCopy)
       opPush(result)
    else:
        opPush(a)
    
    return None

def get():
    indexer = opPop()
    a = opPop()
    if (type(a) == str ): # & (isinstance(indexer, int))
       index = 0
       stringCopy = ""
       while index < len(a):
          char = a[index]
          if ((char != ')') & (char != '(')):      
            stringCopy = stringCopy + char # reverses string, but OK since only care about length
        
          index = index + 1;

       index2 = 0
       while index2 < len(stringCopy):
          char = stringCopy[index2]
          if (index2 == indexer): 
            result = char
        
          index2 = index2 + 1;

       opPush(ord(result)) #convert char to ascii value to pass test
    else:
        opPush(a)
        opPush(indexer)
    
    return None

def getinterval():
    intervalEnd = opPop()
    intervalStart = opPop()
    a = opPop()
    if (type(a) == str ): # & (isinstance(indexer, int))
       index = 0
       stringCopy = ""
       while index < len(a):
          char = a[index]
          if ((char != ')') & (char != '(')):      
            stringCopy = stringCopy + char # reverses string, but OK since only care about length
        
          index = index + 1;

            
       index2 = 0 # at this point the parenthesis are removed
       returnString = "("
       while index2 < len(stringCopy):
          char = stringCopy[index2]
          if (index2 >= intervalStart):
            if (index2 < intervalEnd): 
                returnString += char
        
          index2 = index2 + 1;

       opPush(returnString+")") #add closing paranthesis
    else:
        opPush(a)
        opPush(intervalStart)
        opPush(intervalEnd)

    
    return None

def put():
    inputChar = opPop()
    destination = opPop()
    a = opPop()
    if (type(a) == str ): # & (isinstance(indexer, int))
       index = 0
       stringCopy = ""
       while index < len(a):
          char = a[index]
          if ((char != ')') & (char != '(')):      
            stringCopy = stringCopy + char # reverses string, but OK since only care about length
        
          index = index + 1;

            
       index2 = 0 # at this point the parenthesis are removed
       returnString = "("
       while index2 < len(stringCopy):
          char = stringCopy[index2]
          if (index2 == destination):
            returnString += chr(inputChar)

          else:
              returnString += char
        
          index2 = index2 + 1;

       opPush(returnString+")") #add closing paranthesis
    else:
        opPush(a)
        opPush(destination)
        opPush(inputChar)

    
    return None

#--------------------------- 25% -------------------------------------
# Define the stack manipulation and print operators: dup, copy, pop, clear, exch, roll, stack
def dup():
    inputVal = opPop()
    opPush(inputVal)
    opPush(inputVal)

    return None

def copy(): #copy the opstack?
    element = 0
    stopPoint = len(opstack)
    while (element < stopPoint):
        opPush(opstack[element])
        element += 1
    
    return None

def pop():
    opPop();

    return None

def clear():
    element = 0
    stopPoint = len(opstack)
    while (element < stopPoint):
        opPop()
        element += 1
    
    return None

def exch():
    a = opPop()
    b = opPop()

    opPush(a)
    opPush(b)

    return None

def roll():
    #get parameters from opstack
    if (len(opstack)>2): 
        i = opPop()
        n = opPop()

        if(i < len(opstack)):
            if (n <2):
                None
            elif (n ==2):
                whileCount = 0;
                while(whileCount < i):
                    exch()
                    whileCount += 1
            else:
                #peel off elements I am going to shift
                index =1
                manipList = []
                while(index <= n):
                    manipList.append(opstack[-index])
                    index += 1

                manipList.reverse()

                #elements that are being rolled get popped from the otstack
                popper = 0 
                while(popper < n):
                    opstack.pop()
                    popper += 1
                
                #perform rolling
                newCount = 0
                while(newCount < i):
                    lastElem = manipList[-1]
                    manipList.insert(0,lastElem) #put at beginning
                    manipList.pop() # remove last element
                    newCount += 1

                tempList = opstack + manipList
                opstack.clear()

                #recreate the opstack with correct values
                finalCount = 0
                while(finalCount < len(tempList)):
                    opPush(tempList[finalCount])
                    finalCount += 1
        
        else:
            opPush(n)
            opPush(i)

    return None


def stack():
    count = 1
    while(count < len(opstack)+1):
        print(opstack[-count])
        count += 1

    return None

#--------------------------- 20% -------------------------------------
# Define the dictionary manipulation operators: psDict, begin, end, psDef
# name the function for the def operator psDef because def is reserved in Python. Similarly, call the function for dict operator as psDict.
# Note: The psDef operator will pop the value and name from the opstack and call your own "define" operator (pass those values as parameters).
# Note that psDef()won't have any parameters.

#pops the initial size of the dictionary from the stack, and pushes a brand-new empty dictionary onto the operand stack
def psDict():    
    if(len(opstack) > 0):
        opPop();
    opPush({}) #empty dictionary is pushed onto the stack
    return None

#begin operator pops a dictionary from the top of the operand stack and pushes it on the dictionary stack
def begin():
    if(len(opstack) > 0):
        top = opPop()
        if(type(top) == dict):
            dictPush(top)
        else:
            opPush(top)
    return None

#pop the top dictionary from the dictionary stack and  discard it
def end():
    if(len(dictstack) > 0):
        dictPop()
       
    return None

def psDef():
    #pop 2 from op stack, call define to put a tuple onto dict stack
    tempValue = opPop();
    tempName = opPop();
    define(tempName,tempValue)
    pass