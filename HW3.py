# Name: Brandon Hahn
# Assignment: CPTS 355 HW3
#possibly connected to github?


#FUNCTION DESCRIPTION: sprintLog
   #A funciton that takes a dictionary of users and returns a dictionary of tasks,
   #where each task is associated with the users who worked on the task.
   #First create a new dictionary.
   #Iterate the input dictionary, adding the values to the new dictionary

#INPUTS: dictionary of users with values as a dictionary of tasks
#OUTPUTS: dictionary of tasks with a dictionary of users as values
# from ast import Pass, While
# import string


def sprintLog (sprint):
   """This function takes a dictionary of users with associated hours, and returns a dictionary of tasks"""
   newDict = {}

   for key, inputTuple in sprint.items(): #iterate through entire input dict
      for tupleKey, tupleVal in inputTuple.items(): #iterate through the dict that is the value
         if len(newDict) == 0:
            newDict.setdefault(tupleKey,{})#if the dict is empty, automatically add the value
         elif tupleKey not in newDict:
            newDict[tupleKey] = {}   #if the key is not in the dict, put it in the new dict with an empty dict as the value
         
         newDict[tupleKey][key] = tupleVal   #add the original key as an inner key in the value of the new dict.
            #The value of the new inner key is set to the innermost value of the input dictionary
      
   return newDict



#FUNCTION DESCRIPTION: addSprints
   #A function that taks two dictionaries and combines them: pairing existing keys with values, or adding new key/value pairs

#INPUTS: Two dictionaries
#OUTPUTS: Dictionary
def addSprints(sprint1,sprint2):
   """This function takes two dictionary items and combines them: pairing existing keys with values, or adding new key/value pairs"""
   twoSummed = sprint1.copy() #copy the first input dictionary

   for key2, inputTuple2 in sprint2.items(): #iterate through entire input2 dictionary
      if key2 not in twoSummed:
         twoSummed[key2] = inputTuple2 #If the second dictionary contains a key that is not in the first one, add the keyvalue into the return dict
      elif key2 in twoSummed:
         for key1, inputTuple1 in twoSummed.items(): #iterate to find the matching keys
            if key2 == key1: #if the keys match, I need to search within the values for matching keys
               for inValsKey2, innerVal2 in inputTuple2.items():
                  if inValsKey2 not in inputTuple1:
                     inputTuple1.update({inValsKey2:innerVal2}) #update destroys
                  else:
                     for inValsKey1, innerVal1 in inputTuple1.items():
                        if inValsKey2 == inValsKey1:
                           inputTuple1[inValsKey1] = innerVal1 + innerVal2

   return twoSummed


#FUNCTION DESCRIPTION: addNLogs
   #Takes a list of dictionaries and returns dictionary of summed items

#INPUTS: list of dictionaries
#OUTPUTS: Dictionary
def addNLogs(logList):
   myOut = {}
   while len(logList) >0:
      a = logList.pop()
      a = sprintLog(a)
      myOut = addSprints(myOut,a)
   return myOut



#FUNCTION DESCRIPTION: lookupVal
   #Takes a list of dictionaries and key, traverses list from end and returns value associated with key if in list

#INPUTS: list of dictionaries and key
#OUTPUTS: Dictionary Value
def lookupVal(L,k):
   volatileList = L.copy()
   myOut = None
   while len(volatileList) >0:
      a = volatileList.pop()
      if k in a:
         myOut = a[k]
         volatileList = []

   return myOut



#FUNCTION DESCRIPTION: lookupVal2
   #Takes a list of tuples and key,
   #start at the end. If the key is not in the dict items value, then go to the dict element in the list denoted by the key
   #CONDITION: tuples are ordered by the first item
#INPUTS: list of tuples and key
#OUTPUTS: Dictionary Value
def lookupVal2(L,k):
   volatileList = L.copy()
   if len(L) == 0:
      return None
   lastDictInList = volatileList.pop()
   lastDictVals = lastDictInList[1]
   if k in lastDictVals:
      myOut = lastDictVals.get(k)
      return myOut
   else:
      while len(volatileList) > lastDictInList[0] + 1:
         dummyVar = volatileList.pop() # I want to pop elements off the volatile list until the list length is in correspondence with the tuple index item

   return lookupVal2(volatileList,k)


#FUNCTION DESCRIPTION: unzip
   #takes a list of 3 inputs (L) and returns a tuple of lists where each list includes the first, second, or third element from each tuple respectively
#INPUTS: list of tuples
#OUTPUTS: tuple of lists
def unzip(L):
   myTuple = ([],[],[])
   volatileList = L.copy()
   L1 = []
   L2 = []
   L3 = []
   while len(volatileList) > 0:
      variableTuple = volatileList.pop()
      L1.append(variableTuple[0])
      L2.append(variableTuple[1])
      L3.append(variableTuple[2])

   while len(myTuple[0]) < len(L[0]) +1:
      myTuple[0].append(L1.pop())
      myTuple[1].append(L2.pop())
      myTuple[2].append(L3.pop())
   return myTuple



#FUNCTION DESCRIPTION: iteFile
   #an iterator that represents the sequence of words read from a text file. The iterator is initialized with the name of the file and
   #returns the next word from the file for each call to __next__(). The iterator ignores empty lines and end of line characters.

#CONSTRUCTOR: takes input file
#METHODS: __next__() prints the next word, starting at the beginning of file
class iterFile():

   def __init__(self,iterableFile):
      brandonFile = open(iterableFile,'r') # open file for reading default is read, but 'r' specifies

   def __next__(self):
      pass

   def __iter__(self):
      pass
   

















   #    self.brandonString = brandonFile.read()
   #    brandonFile.close()
   #    self.strCopy = self.brandonString

   # def __next__(self):
   #    #iterate through self.string to until space character
   #    returnString = ""
   #    self.stringIndex = len(self.brandonString) - len(self.strCopy) #index begins at zero, when copy shrinks, the index grows
   #    z = (self.brandonString[self.stringIndex:])
   #    if len(self.strCopy) >0:
   #       for a in z:
   #          self.strCopy = self.strCopy[1:] #slice the head off the copy string
   #          if a == '\n':
   #             a = ' '

   #          if (a == ' '):
   #             return returnString
   #          returnString += a

   #          if a == z:   #terminating condition
   #             return returnString
   
   # def __iter__(self):
   #    for numItems in self.strCopy:
   #       yield self.__next__()
