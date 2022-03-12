# Name: Brandon Hahn
# Assignment: CPTS 355 HW3

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
   """Combines dictionaries in list into 1 dictionary while summing the values of overlapping keys"""

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
   """Performs a lookup based on key input and dictionary"""

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
   """Looking up a value based on the keys of the dictionary input. Very confusing. Uses dict pairs as steps to correct value."""

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
"""Perfrms the opposite of the zip operation: giving a tuple of lists for the first, second, and third elements in input list"""

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





#FUNCTION DESCRIPTION: numPaths
   # takes in table dimmensions and list of blocked out squares, uses recursion to traverse table and find number of paths
#INPUTS: tuple containing dimensions and list of blocks
#OUTPUTS: number of valid paths
def numPaths(m,n,blocks):
   """This function finds the # of paths moving down and right through a table with variable size and blocks in the path."""

   headNode = (1,1)
   if headNode in blocks:
      return 0 # there is a block in the top left corner. No paths to finish!
   
   if m == 1:
      if n == 1:
         return 1 # condition of 1x1 input table
   
   return numPathHelper(1,1,blocks,m,n)

def numPathHelper(D,R,blocks,m,n):
   leftTrace = 0
   rightTrace = 0

   if (R,D) in blocks: # if I have hit a block somehow, get out
      return 0

   leftNode = (D+1,R)
   rightNode = (D,R+1)
   if(((leftNode[0]<=n) and (leftNode not in blocks))and((rightNode[1]<=m) and (rightNode not in blocks))): # if I can create both nodes
      leftTrace = numPathHelper(D+1,R,blocks,m,n)
   
   if(((leftNode[0]<=n) and (leftNode not in blocks))): # if I can create left node
      leftTrace = numPathHelper(D+1,R,blocks,m,n)

   if(((rightNode[1]<=m) and (rightNode not in blocks))): # if I can create right node
      rightTrace = numPathHelper(D,R+1,blocks,m,n)

   if (D == n) and (R == m):
      return 1    #trace is at the finish line
   else:
      return leftTrace + rightTrace # summing condition to combine downpaths with right paths
   



#FUNCTION DESCRIPTION: iteFile
   #an iterator that represents the sequence of words read from a text file. The iterator is initialized with the name of the file and
   #returns the next word from the file for each call to __next__(). The iterator ignores empty lines and end of line characters.

#CONSTRUCTOR: takes input file
#METHODS: __next__() prints the next word, starting at the beginning of file
class iterFile():

   def __init__(self,iterableFile):
      self.inputFile = iterableFile #string item
      self.brandonFile = open(self.inputFile,'r') # open file for reading. default is read, but 'r' specifies
      self.stringIndex = 0
      self.lazyGet = iter(self.getNext())

   def getNext(self):
     for realRow in self.brandonFile: # for each row
         #iterate through self.string to until space character
         returnString = ""
         #self.stringIndex = len(realRow) - len(self.volatileLine) #index begins at zero, when copy shrinks, the index grows
         if len(realRow) >0:
            for a in realRow:
               self.stringIndex = self.stringIndex +1 #increment the indexer
               if a == '\n':
                  self.stringIndex = 0 # if reach the end of line: reset the index
                  a = ' '

               if a != ' ':
                  returnString += a
               elif (a == ' '):
                  yield returnString
                  returnString = ""               

               if self.stringIndex == len(realRow):    #this is the terminating condition that allows the very last character in the file to be read
                  yield returnString      

   def __next__(self):
      return self.lazyGet.__next__() # call next on the current iterable item

   def __iter__(self):
      for element in self.lazyGet:
         yield element
      self.brandonFile.close()   #once finished iterating through the file: close the file


#FUNCTION DESCRIPTION: wordHistogram
#INPUTS: an iterator representing a sequence of words
#OUTPUTS: lsit of tuples where each tuple contains a unique word and the number of times it apepared
def wordHistogram(words):
   """This function takes a file containing words, and returns a list of tuples containing the word appearance count"""

   histFile = open(words)
   wordStack = ""
   wordDictionary = {}
   histReturn = []
   for row in histFile:
      for char in row:
         if char == " "  or char == '\n' or char == row:         
            if wordStack not in wordDictionary:
               print(wordStack)
               wordDictionary[wordStack] = 1
            elif wordStack in wordDictionary:
               wordDictionary[wordStack] = wordDictionary[wordStack] + 1
            
            wordStack = ""
         else:
            wordStack = wordStack+char
            if char == row[-1]: # if I reach the very last element
               if wordStack not in wordDictionary:
                  print(wordStack)
                  wordDictionary[wordStack] = 1
               elif wordStack in wordDictionary:
                  wordDictionary[wordStack] = wordDictionary[wordStack] + 1
               
   for item in wordDictionary:
      histReturn.append((item, wordDictionary[item]))
   
   histReturn.sort(reverse = True , key = lambda x: x[1])
   return histReturn

