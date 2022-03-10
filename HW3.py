# Name: Brandon Hahn
# Assignment: CPTS 355 HW3
#possibly connected to github?

#Create a funciton that takes a dictionary of users and returns a dictionary of tasks, where each task is associated with the users who worked on the task.
#First create a new dictionary.
#Iterate the input dictionary, adding the values to the new dictionary

#inputs: dictionary of users
#outputs: dictionary of tasks

def sprintLog (sprint):
   """This function takes a dictionary of users with associated hours, and returns a dictionary of tasks"""
   newDict = {}

   for a, b in sprint.items():
      for c, d in b.items():
         print(c,"what is going on", d)

