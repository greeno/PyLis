'''
Created on Jul 2, 2012

@author: cdg2
'''
import unittest
from PyLis.Integration import Integration
from PyLis.Types.Person import Person
import logging
logging.basicConfig(level=logging.INFO)
logging.getLogger('suds.client').setLevel(logging.DEBUG)

class Test(unittest.TestCase):
    i = None
    
    def setUp(self):
        self.i=Integration("*****",
                           "*****",
                           "*****")

    def tearDown(self):
        pass
    
    def testCreatePerson(self):
        print self.i.getPersonClient()
        person = Person()
        self.i.createPerson("testing-cdg2", person)

    def testGetPersonClient(self):
        c = self.i.getPersonClient()
        print c
        
    def testGetBulkClient(self):
        c = self.i.getBulkClient()
        print c
        
    def testGetCourseClient(self):
        c = self.i.getCourseClient()
        print c
        
    def testGetGroupClient(self):
        c = self.i.getGroupClient()
        print c
    
    def testGetMemberClient(self):
        c = self.i.getMemberClient()
        print c
        
    


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()