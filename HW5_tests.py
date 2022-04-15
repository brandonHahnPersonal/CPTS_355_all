import sys
import io
import unittest
from HW5 import *

class HW5Tests(unittest.TestCase):
    def setUp(self):
        opstack = []

    def testOpPush(self):
        opstack.clear()
        opPush("(Hello)")
        self.assertEqual(opstack[-1],"(Hello)")
    
    def testOpPush2(self):
        opstack.clear()
        opPush(5)
        self.assertEqual(opstack[-1],5)
    
    def testOpPush3(self):
        opstack.clear()
        opPush(" ")
        self.assertEqual(opstack[-1]," ")

    def testOpPush4(self):
        opstack.clear()
        opPush(" ")
        opPush("'\'")
        self.assertEqual(opstack[-1],"'\'")

    ####################################################################################

    def testOpPop(self):
        opstack.clear()
        opPush(5)
        self.assertEqual(opPop(),5)

    def testOpPop2(self):
        opstack.clear()
        opPush(5)
        opPush(5)
        opPush(" ")

        self.assertEqual(opPop(),' ')        

    def testOpPop3(self):
        opstack.clear()
        opPush(None)
        self.assertEqual(opPop(),None)
    

    ####################################################################################

    def testDictPush(self):
        dictstack.clear()
        dictPush({})
        self.assertEqual(dictstack[-1],{})

    def testDictPush2(self):
        dictstack.clear()
        dictPush({1,2})
        self.assertEqual(dictstack[-1],{1,2})

    def testDictPush3(self):
        dictstack.clear()
        dictPush(' ')
        self.assertEqual(dictstack[-1],' ')


    ####################################################################################

    def testDictPop(self):
        dictstack.clear()
        dictPush({})
        dictPop()
        self.assertEqual(len(dictstack),0)

    def testDictPop2(self):
        dictstack.clear()
        dictPush({})
        dictPush({1,2})
        dictPop()
        dictPop()

        self.assertEqual(len(dictstack),0)

    def testDictPop3(self):
        dictstack.clear()
        dictPop()
        dictPop()
        self.assertEqual(len(dictstack),0)        

    ####################################################################################

    def testDefine(self):
        dictstack.clear()
        define("/a",1)
        self.assertEqual(len(dictstack),1)

    def testDefine2(self):
        dictstack.clear()
        define(0,0)
        self.assertEqual(len(dictstack),1)

    def testDefine3(self):
        dictstack.clear()
        define("/a",1)
        define(0,0)

        self.assertEqual(len(dictstack),2)


    ####################################################################################

    def testLookup(self):
        dictstack.clear()  
        
        opPush("/n1")       
        opPush("(TEST)")  
        psDef()
        
        opPush("/n1")       
        opPush("(hornswaggle)")  
        psDef()


        self.assertEqual(lookup("n1"),"(hornswaggle)")
        pass

    def testLookup2(self):
        dictstack.clear()  
        lookup("n1")
        pass

    def testLookup3(self):
        dictstack.clear()  
        opPush("(hornswaggle)")  
        opPush("/n1")     
        psDef()
  
        lookup("n1")
        pass


    ####################################################################################


    def testAdd(self):
        opstack.clear()     
        opPush(1.0)       
        opPush(2.0)       
        add()       
        self.assertEqual(opPop(),3)

    def testAdd2(self):
        opstack.clear()     
        opPush(3)
        opPush("(notanum)")
        add()       
        self.assertEqual(opPop(),"(notanum)")
        self.assertEqual(opPop(),3)

    def testAdd3(self):
        opstack.clear()     
        opPush(1000000000000000000000000000000)
        opPush(1)
        add()       
        self.assertEqual(opPop(),1000000000000000000000000000001)

    def testAdd4(self):
        opstack.clear()     
        opPush('b')
        opPush('a')
        add()       
        self.assertEqual(opPop(),'a')

    ####################################################################################

    def testSub(self):
        opstack.clear()
        opPush(3)
        opPush(2)
        sub()
        self.assertEqual(opPop(),1)

    def testSub2(self):
        opstack.clear()
        opPush(3.0)
        opPush(2.0)
        sub()
        self.assertEqual(opPop(),1.0)

    def testSub3(self):
        opstack.clear()
        opPush('a')
        opPush('2')
        sub()
        self.assertEqual(opPop(),'2')
    
    ####################################################################################

    def testMul(self):
        opstack.clear()
        opPush(3)
        opPush(2)
        mul()
        self.assertEqual(opPop(),6)

    def testMul2(self):
        opstack.clear()
        opPush(3.0)
        opPush(2.0)
        mul()
        self.assertEqual(opPop(),6.0)

    def testMul3(self):
        opstack.clear()
        opPush('a')
        opPush('b')
        mul()
        self.assertEqual(opPop(),'b')

    def testMul4(self):
        opstack.clear()
        opPush(0)
        opPush(15555)
        mul()
        self.assertEqual(opPop(),0)

    ####################################################################################

    def testDiv(self):
        opstack.clear()
        opPush(4)
        opPush(2)
        div()
        self.assertEqual(opPop(),2)

    def testDiv2(self):
        opstack.clear()
        opPush(4.0)
        opPush(2.0)
        div()
        self.assertEqual(opPop(),2.0)

    def testDiv3(self):
        opstack.clear()
        opPush('a')
        opPush(999)
        div()
        self.assertEqual(opPop(),999)

    def testDiv4(self):
        opstack.clear()
        opPush(0)
        opPush(999)
        div()
        self.assertEqual(opPop(),0.0)
    
    ####################################################################################

    def testMod(self):
        opstack.clear()
        opPush(3)
        opPush(2)
        mod()
        self.assertEqual(opPop(),1)

    def testMod2(self):
        opstack.clear()
        opPush(3.0)
        opPush(2.0)
        mod()
        self.assertEqual(opPop(),1.0)

    def testMod3(self):
        opstack.clear()
        opPush('a')
        opPush('2')
        mod()
        self.assertEqual(opPop(),'2')
    
    ####################################################################################

    def testEq2(self):
        opstack.clear()
        opPush(3)
        opPush(2)
        eq()
        self.assertEqual(opPop(),False)

    def testEq3(self):
        opstack.clear()
        opPush(3.0)
        opPush(2.0)
        eq()
        self.assertEqual(opPop(),False)

    def testEq4(self):
        opstack.clear()
        opPush(3)
        opPush(3)
        eq()
        self.assertEqual(opPop(),True)

    def testEq5(self):
        opstack.clear()
        opPush("str")
        opPush("str")
        eq()
        self.assertEqual(opPop(),True)
    ####################################################################################

    def testLt(self):
        opstack.clear()
        opPush(2)
        opPush(3)
        lt()
        self.assertEqual(opPop(),True)

    def testLt2(self):
        opstack.clear()
        opPush(2.0)
        opPush(3.0)
        lt()
        self.assertEqual(opPop(),True)

    def testLt3(self):
        opstack.clear()
        opPush("a")
        opPush("b")
        lt()
        self.assertEqual(opPop(),True)

    ####################################################################################

    def testGt2(self):
        opstack.clear()
        opPush(2)
        opPush(3)
        gt()
        self.assertEqual(opPop(),False)


    def testaGt3(self):
        opstack.clear()
        opPush(2.0)
        opPush(3.0)
        gt()
        self.assertEqual(opPop(),False)

    def testGt4(self):
        opstack.clear()
        opPush("a")
        opPush("b")
        gt()
        self.assertEqual(opPop(),False)


    ####################################################################################

    def testLength(self):
        opstack.clear()
        opPush("(Hello)")
        length()
        self.assertEqual(opPop(),5)

    def testLength2(self):
        opstack.clear()
        opPush(" ")
        length()
        self.assertEqual(opPop(),1)

    def testLength3(self):
        opstack.clear()
        opPush("()")
        length()
        self.assertEqual(opPop(),0)

    ####################################################################################

    def testGet(self):
        opstack.clear()
        opPush("(CptS355)")
        opPush(0)
        get()
        self.assertEqual(opPop(),ord('C'))

    def testGet2(self):
        opstack.clear()
        opPush("((((((CptS355))))))")
        opPush(0)
        get()
        self.assertEqual(opPop(),ord('C'))

    def testGet3(self):
        opstack.clear()
        opPush(" ")
        opPush(0)
        get()
        self.assertEqual(opPop(),ord(' '))

    ####################################################################################

    def testGetInterval(self):
        opstack.clear()
        opPush("(CptS355)")
        opPush(0)
        opPush(3)
        getinterval()
        self.assertEqual(opPop(),"(Cpt)")

    def testGetInterval2(self):
        opstack.clear()
        opPush("(CptS355)")
        opPush(0)
        opPush(7)
        getinterval()
        self.assertEqual(opPop(),"(CptS355)")

    def testGetInterval3(self):
        opstack.clear()
        opPush("(C)")
        opPush(0)
        opPush(3)
        getinterval()
        self.assertEqual(opPop(),"(C)")

    ####################################################################################

    def testPut(self):
        opstack.clear()
        opPush("(CptS355)")
        dup()
        opPush(0)
        opPush(48)
        put()
        self.assertEqual(opPop(),"(0ptS355)")

    def testPut2(self):
        opstack.clear()
        opPush("(CptS355)")
        dup()
        opPush(1)
        opPush(48)
        put()
        self.assertEqual(opPop(),"(C0tS355)")

    def testPut3(self):
        opstack.clear()
        opPush("(CptS355)")
        dup()
        opPush(0)
        opPush(65)
        put()
        self.assertEqual(opPop(),"(AptS355)")

    ####################################################################################

    def testDup(self):
        opstack.clear()
        opPush(3)
        dup()
        self.assertEqual(len(opstack),2)

    def testDup2(self):
        opstack.clear()
        opPush(3)
        dup()
        dup()
        dup()

        self.assertEqual(len(opstack),4)

    def testDup3(self):
        opstack.clear()
        dup()
        self.assertEqual(len(opstack),2)

    ####################################################################################

    def testCopy(self):
        opstack.clear()
        opPush(5)
        opPush(4)
        opPush(3)
        opPush(2)
        copy()
        self.assertEqual(len(opstack),8)

    def testCopy2(self):
        opstack.clear()
        copy()
        self.assertEqual(len(opstack),0)

    def testCopy3(self):
        opstack.clear()
        opPush(5.0)
        opPush(4)
        opPush('String')
        opPush(2)
        copy()
        self.assertEqual(len(opstack),8)

    ####################################################################################

    def testPop(self):
        opstack.clear()
        opPush(1)
        pop()
        self.assertEqual(len(opstack),0)

    def testPop2(self):
        opstack.clear()
        opPush("SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS")
        pop()
        self.assertEqual(len(opstack),0)

    def testPop3(self):
        opstack.clear()
        pop()
    
    ####################################################################################

    def testClear(self):
        opstack.clear()
        opPush(1)
        clear()
        self.assertEqual(len(opstack),0)

    def testClear2(self):
        opstack.clear()
        opPush(1)
        clear()
        clear()
        self.assertEqual(len(opstack),0)

    def testClear3(self):
        opstack.clear()
        opPush("1")
        clear()
        self.assertEqual(len(opstack),0)

    ####################################################################################

    def testExch(self):
        opstack.clear()
        opPush(1)
        opPush(2)
        exch()
        self.assertListEqual(opstack,[2,1])

    def testExch2(self):
        opstack.clear()
        opPush(1.0)
        opPush(2.0)
        exch()
        self.assertListEqual(opstack,[2,1])

    def testExch3(self):
        opstack.clear()
        opPush("1")
        opPush("2")
        opPush(1)
        opPush(2)
        exch()
        self.assertListEqual(opstack,["1","2",2,1])
    ####################################################################################

    def testRoll(self):
        opstack.clear()
        opPush(1)
        opPush(2)
        opPush(3)
        opPush(4)
        opPush(2)
        opPush(3)
        roll()
        self.assertListEqual(opstack,[1,2,4,3])

    def testRoll2(self):
        opstack.clear()
        opPush(1)
        opPush(2)
        opPush(3)
        opPush(4)
        opPush(3)
        opPush(1)
        roll()
        self.assertListEqual(opstack,[1,4,2,3])

    def testRoll3(self):
        opstack.clear()

        opPush(3)
        opPush(1)
        roll()      
    
    def testRoll4(self):
        opstack.clear()
        opPush(1)
        opPush(2)
        opPush(3)
        opPush(4)
        opPush(5)
        opPush(6)
        opPush(7)
        opPush(8)        
        opPush(5)
        opPush(22)
        roll()
        self.assertListEqual(opstack,[1, 2, 3, 4, 5, 6, 7, 8, 5, 22])
    
    ####################################################################################

    def testStack(self):
        pass # unsure how to test print, maybe have it return instead
        text_trap = io.StringIO()
        sys.stdout = text_trap
        opstack.clear()
        opPush(2)
        opPush(3)
        stack()
        sys.stdout = sys.__stdout__
        self.assertEqual(text_trap.getvalue(), "3\n2\n")

    def testStack2(self):
        pass # unsure how to test print, maybe have it return instead
        text_trap = io.StringIO()
        sys.stdout = text_trap
        opstack.clear()
        stack()
        sys.stdout = sys.__stdout__
        self.assertEqual(text_trap.getvalue(), "")

    def testStack3(self):
        pass # unsure how to test print, maybe have it return instead
        text_trap = io.StringIO()
        sys.stdout = text_trap
        opstack.clear()
        opPush("1")
        opPush("2")
        opPush(1)
        opPush(2)
        stack()
        sys.stdout = sys.__stdout__
        self.assertEqual(text_trap.getvalue(), '2\n1\n2\n1\n')                

    ####################################################################################


    def testPsDict(self):
        opstack.clear()
        opPush(2)
        psDict()
        self.assertIsInstance(opPop(), dict)

    def testPsDict2(self):
        opstack.clear()
        opPush("STR")
        psDict()
        self.assertIsInstance(opPop(), dict)

    def testPsDict3(self):
        opstack.clear()
        psDict()         
        self.assertEqual(opPop(),{})                


    ####################################################################################


    def testPsDef(self):
        opstack.clear()
        dictstack.clear()
        opPush(2)
        psDict()
        begin()
        opPush("/a")
        opPush(2)
        
        psDef()
        self.assertEqual(dictstack[-1],{"/a":2})

    def testPsDef2(self):
        opstack.clear()
        dictstack.clear()
        opPush(2)
        psDict()
        begin()
        opPush("/a")
        opPush(2)
        opPush(2)
        psDict()
        begin()
        opPush("/a")
        opPush(2)
        psDef()
        self.assertEqual(dictstack[-1],{"/a":2})

    def testPsDef3(self):
        opstack.clear()
        dictstack.clear()
        opPush("SS")
        psDict()
        begin()
        opPush("SS")
        opPush(2)
        psDef()
        self.assertEqual(dictstack[-1],{'SS': 2})                




    ####################################################################################

    def testEnd(self):
            opstack.clear()
            dictPush(5)
            end()

    def testEnd2(self):
            opstack.clear()
            dictPush(5)
            dictPush(6)
            end()

            self.assertEqual(dictPop(),5)        

    ####################################################################################

if __name__ == '__main__':
    unittest.main()

