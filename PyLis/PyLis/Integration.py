'''
Created on Jul 2, 2012

@author: cdg2
'''
from suds.client import Client
from Types.Person import Person

import logging
class Integration(object):
    '''
    Main entry point for LIS Integration. You can get all integration points from here.
    '''
    baseUri=None
    username=None
    password=None

    personClient = None
    bulkClient = None
    courseClient = None
    groupClient = None
    memberClient = None
    def __init__(self,baseUri,username,password):
        '''
        baseUri is everything before and including the services in the URL from the config screens in Learn.
        If https://sp8.bblearn.nau.edu/webapps/bb-data-integration-lis-BBLEARN/services/PersonManagementServiceSyncService.wsdl
        Then https://sp8.bblearn.nau.edu/webapps/bb-data-integration-lis-BBLEARN/services/
        '''
        self.baseUri=baseUri
        self.username=username
        self.password=password
        
        ## Init all clients
        self.personClient = Client(self.baseUri + "PersonManagementServiceSyncService.wsdl",
                        location = self.baseUri + "PersonManagementServiceSyncService",
                        username = self.username,
                        password = self.password)
        self.bulkClient = Client(self.baseUri + "BulkDataExchangeManagementServiceSyncService.wsdl",
                        location = self.baseUri + "BulkDataExchangeManagementServiceSyncService",
                        username = self.username,
                        password = self.password)
        self.courseClient = Client(self.baseUri + "CourseSectionManagerSyncService.wsdl",
                        location = self.baseUri + "CourseSectionManagerSyncService",
                        username = self.username,
                        password = self.password)
        self.groupClient = Client(self.baseUri + "GroupManagementServiceSyncService.wsdl",
                        location = self.baseUri + "GroupManagementServiceSyncService",
                        username = self.username,
                        password = self.password)
        self.memberClient = Client(self.baseUri + "MembershipManagementServiceSyncService.wsdl",
                        location = self.baseUri + "MembershipManagementServiceSyncService",
                        username = self.username,
                        password = self.password)
        
    def getPersonClient(self):
        return self.personClient
    
    def getBulkClient(self):
        return self.bulkClient
    
    def getCourseClient(self):
        return self.courseClient
    
    def getGroupClient(self):
        return self.groupClient
    
    def getMemberClient(self):
        return self.memberClient
    
    def createPerson(self,guid,person):
        guidType = self.personClient.factory.create('sourcedGUID')
        guidType.sourcedId=guid
        logging.debug(guidType)
        personType = person.toType(self.personClient)
        print personType
        logging.debug(personType)
        ret = self.personClient.service.createPerson(guid,personType)
        response = self.personClient.last_received().getChild("soapenv:Envelope").getChild("soapenv:Header").getChild("ims:imsx_syncResponseHeaderInfo").getChild("ims:imsx_statusInfo").getChild("ims:imsx_codeMajor").getText()
        if response == "failure":
            logging.error(self.personClient.last_received())
            raise Exception("createPerson Failure")
        logging.debug(self.personClient.last_received())
        return ret
        