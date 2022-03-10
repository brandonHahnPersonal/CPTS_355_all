# Name: Brandon Hahn
# Assignment: CPTS 355 HW3
#possibly connected to github?

#Create a funciton that takes a dictionary of users and returns a dictionary of tasks, where each task is associated with the users who worked on the task.
#First divide keys and values.
#
#inputs: dictionary of users
#outputs: dictionary of tasks
bTest = {'John': {'task1': 5}, 'Rae': {'task1': 10, 'task2': 4}, 'Kelly': {'task1': 8, 'task3': 5}, 'Alex': {'task1': 11, 'task2': 2, 'task3': 1}, 'Aaron': {'task2': 15}, 'Ethan':{'task3': 12}, 'Helen': {'task3': 10}}
myKey = bTest.keys() #This puts the keys into a list.
myVals = bTest.values() #This puts the values into a list of dicts
print("Keys = ", myKey)
print("values = ", myVals)
nameArray = []
valArray = []
for a, b in bTest.items():
   nameArray.append(a)
   valArray.append(b)
   print(a)

for a in valArray:
   print(a)
#valArray.append(''.join(b))

name1 = nameArray.pop()

val1 = valArray.pop() #pops a tuple off. I want
print(val1)
mystr = ''.join(val1)

def sprintLog (sprint):
   """This function takes a dictionary of users with associated hours, and returns a dictionary of tasks"""
   myKey = sprint.keys() #This puts the keys into a list.
   myValue = sprint.values() #This puts the values (tuples) into a list of tuples
   print("Keys = ", myKey)
   print("values = ", myValue)
