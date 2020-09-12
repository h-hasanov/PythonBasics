import unittest
import Functions
import math
import mock
import datetime

class TestTheFunction(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        # Initialize things for all tests
        cls.x = 100
        
    @classmethod
    def tearDownClass(cls):
        # Do things after all tests have run
        cls.x = 0
    
    def test_with_one(self):
        print(self.x)
        self.assertEqual(Functions.divide(1,1),1)
    
    def test_with_zero(self):
        self.assertEqual(Functions.divide(0,0),0)
    
    def Asserts(self):
        equalsFunc = lambda a,b: self.assertEqual(a,b)
        notEqualsFunc = lambda a,b: self.assertNotEquals(a,b)
        trueFunc = lambda a: self.assertTrue(a)
        falseFunc = lambda a: self.assertFalse(a)
        assertIsFunc = lambda a,b: self.assertIs(a,b) #a is b
        assertInFunc = lambda a,listObj: self.assertIn(a, listObj)
        assertIsInstanceFunc = lambda a,t: self.assertIsInstance(a,t)
        
    def getMockToday(self):
        print("Mock Called")
        m = mock.Mock()
        m.month = 2
        m.day = 29
        return m
    
    def test_doSomethingWithLeapDay(self):
        datetime.datetime = mock.Mock()
        datetime.datetime.today.return_value = self.getMockToday()
        
        Functions.doSomethingWithLeapDay()
    
    def test_SumOnes(self):
        myMock = mock.Mock(spec = Functions.SumFunction)
        Functions.SumFunction = myMock
        Functions.SumFunction.return_value=999
        
        print(Functions.SumOnes())
        
        myMock.assert_called_with(a=1, b=1, c=1)
    
if __name__ == '__main__':
    unittest.main()

# python3 -m unittest <filenames>