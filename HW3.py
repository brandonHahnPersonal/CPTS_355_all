# Name: Brandon Hahn
# Assignment: CPTS 355 HW3
#possibly connected to github?

from ast import Pass


bTest = {'task1': {'John': 5, 'Rae': 10, 'Kelly': 8, 'Alex': 11}, 'task2': {'Rae': 4, 'Alex': 2, 'Aaron': 15}, 'task3': {'Kelly': 5, 'Alex': 1, 'Ethan': 12, 'Helen': 10}}
input2 = {'task1': {'Mark': 5, 'Kelly': 10, 'Alex': 15}, 'task2': {'Mark': 2, 'Alex': 2, 'Rae': 10, 'Aaron': 10}, 'task4': {'Helen': 16}}
twoSummed = bTest.copy() #copy the first input dictionary

for key2, inputTuple2 in input2.items(): #iterate through entire input2 dictionary
   if key2 not in twoSummed:
      twoSummed[key2] = inputTuple2 #If the second dictionary contains a key that is not in the first one, add the keyvalue into the return dict
   else:
      Pass
Pass




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
   twoSummed = sprint1.copy()

   #for key1, inputTuple1 in sprint1.items(): #iterate through entire input dict

   

   return twoSummed