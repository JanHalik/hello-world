   # The code to test
import unittest
import os
import sys
PROJECT_PATH = os.getcwd()
SOURCE_PATH = os.path.join(
    PROJECT_PATH,"bin"
)
sys.path.append(SOURCE_PATH)
 #from bin.test import TestClass   # The test framework
import testClass   # The test framework

class Test_TestClass(unittest.TestCase):
    __instance=testClass.TestClass(1)

    def test_method(self):
        self.assertEqual(self.__instance.print_val(),1)  

if __name__ == '__main__':
    unittest.main()