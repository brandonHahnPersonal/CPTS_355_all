#BRANDON HAHN CPTS 355 HW 3
import unittest
from HW3 import *

class HW3SampleTests(unittest.TestCase):
    def setUp(self):
        # sprintLog inputs
        self.log1 = {'John': {'task1': 5}, 'Rae': {'task1': 10, 'task2': 4}, 'Kelly': {'task1': 8, 'task3': 5}, 'Alex': {'task1': 11, 'task2': 2, 'task3': 1}, 'Aaron': {'task2': 15}, 'Ethan':{'task3': 12}, 'Helen': {'task3': 10}}
        self.log2 = {'Mark': {'task1': 5, 'task2': 2}, 'Kelly': {'task1': 10}, 'Alex': {'task1': 15, 'task2': 2}, 'Rae': {'task2': 10}, 'Aaron': {'task2': 10}, 'Helen': {'task4': 16}}
        self.log3 = {'Aaron': {'task5': 15, 'task6': 8}, 'Rae': {'task5': 20}, 'Helen': {'task6': 16}}
        self.log4 = {'Alex': {'task6': 15}, 'Kelly': {'task5': 20}, 'Helen': {'task6': 10}}
        self.log5 = {'Brandon': {'task1': 15, 'task2' : 40}, 'blur': {'bing': 20}, 'bang': {'yieee': 10}}
        self.log6 = {}

        # addSprints inputs/outputs
        self.sprint1 = {'task1': {'John': 5, 'Rae': 10, 'Kelly': 8, 'Alex': 11}, 'task2': {'Rae': 4, 'Alex': 2, 'Aaron': 15}, 'task3': {'Kelly': 5, 'Alex': 1, 'Ethan': 12, 'Helen': 10}}
        self.sprint2 = {'task1': {'Mark': 5, 'Kelly': 10, 'Alex': 15}, 'task2': {'Mark': 2, 'Alex': 2, 'Rae': 10, 'Aaron': 10}, 'task4': {'Helen': 16}}
        self.sprint3 = {'FrontEnd': {'Brandon': 19, 'Colin': 6, 'Minh': 19}, 'BackEnd': {'Colin': 40,}, 'Poster': {'Zainab': 16}, 'Video': {'Kayla': 12}}
        self.sprint4 = {'task1': {'Brandon': 15}, 'task2': {'Brandon': 40}, 'bing': {'blur': 20}, 'yieee': {'bang': 10}}
        self.addedSprints = {'task1': {'John': 5, 'Rae': 10, 'Kelly': 18, 'Alex': 26, 'Mark': 5}, 'task2': {'Rae': 14, 'Alex': 4, 'Aaron': 25, 'Mark': 2}, 'task3': {'Kelly': 5, 'Alex': 1, 'Ethan': 12, 'Helen': 10}, 'task4': {'Helen': 16}}
        self.addedSprints2 = {'task1': {'John': 5, 'Rae': 10, 'Kelly': 18, 'Alex': 26, 'Mark': 5}, 'task2': {'Rae': 14, 'Alex': 4, 'Aaron': 25, 'Mark': 2}, 'task3': {'Kelly': 5, 'Alex': 1, 'Ethan': 12, 'Helen': 10}, 'FrontEnd': {'Brandon': 19, 'Colin': 6, 'Minh': 19}, 'BackEnd': {'Colin': 40}, 'Poster': {'Zainab': 16}, 'Video': {'Kayla': 12}}
        self.addedSprints3 = {'task1': {'Brandon': 30}, 'task2': {'Brandon': 80}, 'bing': {'blur': 40}, 'yieee': {'bang': 20}}
        # addNLogs input/output
        self.logList = [self.log1,self.log2,self.log3,self.log4]
        self.myloglist = [self.log5,self.log5]
        self.sprintSummary = {'task1': {'John': 5, 'Rae': 10, 'Kelly': 18, 'Alex': 26, 'Mark': 5}, 'task2': {'Rae': 14, 'Alex': 4, 'Aaron': 25, 'Mark': 2}, 'task3': {'Kelly': 5, 'Alex': 1, 'Ethan': 12, 'Helen': 10}, 'task4': {'Helen': 16}, 'task5': {'Aaron': 15, 'Rae': 20, 'Kelly': 20}, 'task6': {'Aaron': 8, 'Helen': 26, 'Alex': 15}}
        self.mysummary = {'task1': {'Brandon': 30}, 'task2': {'Brandon': 80}, 'bing': {'blur': 40}, 'yieee': {'bang': 20}}
        #lookupVal inputs
        self.lookupList = [{"x":1,"y":True,"z":"found"},{"x":2},{"y":False}]
        self.lookupList1 = [{"item 1":1,"item 2":False,"item 3":4,},{"x":2},{"y":False}]
        self.lookup2List = [(0,{"x":0,"y":True,"z":"zero"}), (0,{"x":1}), (1,{"y":False}), (1,{"x":3, "z":"three"}), (2,{})]
        # iterFile output
        self.filetokens = ["CptS","355","Assignment","3","-","Python","Warmup","This","is","a","text","test","file","for","CptS","355","-","Assignment","3","-","Python","Warmup","With","some","repeated","text","for","CptS","355","-","Assignment","3","-","Python","Warmup","."]
        self.histogram = [('-', 5), ('3', 3), ('355', 3), ('Assignment', 3), ('CptS', 3), ('Python', 3), ('Warmup', 3), ('for', 2), ('text', 2), ('.', 1), ('This', 1), ('With', 1), ('a', 1), ('file', 1), ('is', 1), ('repeated', 1), ('some', 1), ('test', 1)]
        self.zipList = [(1,"a",{1:"a"}),(2,"b",{2:"b"}),(3,"c",{3:"c"}),(4,"d",{4:"d"})]
        self.unzipped = ([1, 2, 3, 4], ['a', 'b', 'c', 'd'], [{1: 'a'}, {2: 'b'}, {3: 'c'}, {4: 'd'}])
        self.zipList1 = [(5,"o",{}),(2,"b",{2:"b"}),(3,"c",{3:"c"}),(4,"d",{4:"d"})]
        self.unzipped1 = ([5, 2, 3, 4], ['o', 'b', 'c', 'd'], [{}, {2:'b'}, {3:'c'}, {4:'d'}])

        self.histCorrect = [('-', 5), ('CptS', 3), ('355', 3), ('Assignment', 3), ('3', 3), ('Python', 3), ('Warmup', 3), ('text', 2), ('for', 2), ('This', 1), ('is', 1), ('a', 1), ('test', 1), ('file', 1), ('With', 1),('some', 1),('repeated', 1),('.', 1),]

    def test_sprintLog(self):
        self.assertDictEqual(sprintLog(self.log1),self.sprint1)
        self.assertDictEqual(sprintLog(self.log2),self.sprint2)
        self.assertDictEqual(sprintLog(self.log5),self.sprint4)
        self.assertDictEqual(sprintLog(self.log5),self.sprint4)
        self.assertDictEqual(sprintLog(self.log6),{})

    def test_addSprints(self):
        self.assertDictEqual(addSprints(self.sprint1,self.sprint2),self.addedSprints)
        self.assertDictEqual(addSprints(self.sprint1,self.sprint3),self.addedSprints2)
        self.assertDictEqual(addSprints(self.sprint4,self.sprint4),self.addedSprints3)
        self.assertDictEqual(addSprints(self.sprint4,{}),self.sprint4)
        self.assertDictEqual(addSprints({},{}),{})

    def test_addNLogs(self):
        self.assertDictEqual(addNLogs(self.logList),self.sprintSummary)
        self.assertDictEqual(addNLogs([]),{})
        self.assertDictEqual(addNLogs(self.myloglist),self.mysummary)


    def test_lookupVal(self):
        self.assertEqual(lookupVal(self.lookupList,"x"),2)
        self.assertEqual(lookupVal(self.lookupList,"y"),False)
        self.assertEqual(lookupVal(self.lookupList,"z"),"found")
        self.assertEqual(lookupVal(self.lookupList,"t"),None)
        self.assertEqual(lookupVal(self.lookupList1,"item 1"),1)
        self.assertEqual(lookupVal(self.lookupList1,"item 2"),False)

    def test_lookupVal2(self):
        self.assertEqual(lookupVal2(self.lookup2List,"x"),1)
        self.assertEqual(lookupVal2(self.lookup2List,"y"),False)
        self.assertEqual(lookupVal2(self.lookup2List,"z"),"zero")
        self.assertEqual(lookupVal2(self.lookup2List,"t"),None)


    def test_unzip(self):
        self.assertEqual(unzip(self.zipList),self.unzipped)
        self.assertEqual(unzip(self.zipList1),self.unzipped1)

    def test_numPaths(self):
        self.assertEqual(numPaths(10,3,[(2,2),(7,1)]),27)
        self.assertEqual(numPaths(2, 2, []), 2)
        self.assertEqual(numPaths(2, 2, [(1, 1)]), 0)
        self.assertEqual(numPaths(3, 3, [(2, 1), (1, 2)]), 0)
        self.assertEqual(numPaths(3, 3, []), 6)
        self.assertEqual(numPaths(4, 4, []), 20)
        self.assertEqual(numPaths(5, 5, []), 70)
        self.assertEqual(numPaths(6, 6, []), 252)
        self.assertEqual(numPaths(7, 7, []), 924)
        self.assertEqual(numPaths(8, 8, []), 3432)
        self.assertEqual(numPaths(6, 6, [(1,1)]), 0) # going larger than this causes it to take very long

        pass

    def test_iterFile(self):
        mywords = iterFile("testfile.txt")
        self.assertEqual(mywords.__next__(),"CptS")
        self.assertEqual(mywords.__next__(),"355")
        self.assertEqual(mywords.__next__(),"Assignment")
        restofFile = []
        for word in mywords:
            restofFile.append(word)
        self.assertEqual(restofFile,self.filetokens[3:])

    def test_wordHistogram(self):
        a = wordHistogram("testfile.txt")
        self.assertEqual(a,self.histCorrect)

if __name__ == '__main__':
    unittest.main()

