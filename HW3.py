# Name: Brandon Hahn
# Assignment: CPTS 355 HW3
#possibly connected to github?


#FUNCTION DESCRIPTION:
   #A funciton that takes a dictionary of users and returns a dictionary of tasks,
   #where each task is associated with the users who worked on the task.
   #First create a new dictionary.
   #Iterate the input dictionary, adding the values to the new dictionary

#INPUTS: dictionary of users with values as a dictionary of tasks
#OUTPUTS: dictionary of tasks with a dictionary of users as values


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



#FUNCTION DESCRIPTION:
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


#FUNCTION DESCRIPTION:
   #Takes a list of dictionaries and returns dictionary of summed items
   #grab dict elements from the list, then call my dictionary adder

#INPUTS: list of dictionaries
#OUTPUTS: Dictionary
def addNLogs(logList):
   myOut = {}
   while len(logList) >0:
      a = logList.pop()
      a = sprintLog(a)
      myOut = addSprints(myOut,a)
   return myOut


dict1 = {'John': {'task1': 5}, 'Rae': {'task1': 10, 'task2': 4}, 'Kelly': {'task1': 8, 'task3': 5}, 'Alex': {'task1': 11, 'task2': 2, 'task3': 1}, 'Aaron': {'task2': 15}, 'Ethan':{'task3': 12}, 'Helen': {'task3': 10}}
dict2 = {'Mark': {'task1': 5, 'task2': 2}, 'Kelly': {'task1': 10}, 'Alex': {'task1': 15, 'task2': 2}, 'Rae': {'task2': 10}, 'Aaron': {'task2': 10}, 'Helen': {'task4': 16}}
dict3 = {'Aaron': {'task5': 15, 'task6': 8}, 'Rae': {'task5': 20}, 'Helen': {'task6': 16}}
dict4 = {'Alex': {'task6': 15}, 'Kelly': {'task5': 20}, 'Helen': {'task6': 10}}
bList = [dict1,dict2,dict3,dict4]
addNLogs(bList)
bCopy = bList
v1 = bCopy.pop()
v2 = bCopy.pop()
v3 = addSprints(v1,v2)



