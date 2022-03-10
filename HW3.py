# Name: Brandon Hahn
# Assignment: CPTS 355 HW3
#possibly connected to github?

#Create a funciton that takes a dictionary of users and returns a dictionary of tasks, where each task is associated with the users who worked on the task.
#First create a new dictionary.
#Iterate the input dictionary, adding the values to the new dictionary

#inputs: dictionary of users with values as a dictionary of tasks
#outputs: dictionary of tasks with a dictionary of users as values
#from email.policy import default


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

