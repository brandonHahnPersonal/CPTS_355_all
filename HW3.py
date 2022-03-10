# Name: Brandon Hahn
# Assignment: CPTS 355 HW3
#possibly connected to github?

#Create a funciton that takes a dictionary of users and returns a dictionary of tasks, where each task is associated with the users who worked on the task.
#First create a new dictionary.
#Iterate the input dictionary, adding the values to the new dictionary

#inputs: dictionary of users
#outputs: dictionary of tasks
bTest = {'John': {'task1': 5}, 'Rae': {'task1': 10, 'task2': 4}, 'Kelly': {'task1': 8, 'task3': 5}, 'Alex': {'task1': 11, 'task2': 2, 'task3': 1}, 'Aaron': {'task2': 15}, 'Ethan':{'task3': 12}, 'Helen': {'task3': 10}}
for a, b in bTest.items():
   for c, d in b.items():
      print(c,"what is going on", d)

def sprintLog (sprint):
   """This function takes a dictionary of users with associated hours, and returns a dictionary of tasks"""
   newDict = {}

   for a, b in sprint.items():
      for c, d in b.items():
         print(c,"what is going on", d)

