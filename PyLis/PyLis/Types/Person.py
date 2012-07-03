'''
Created on Jul 2, 2012

@author: cdg2
'''
from BaseType import BaseType

class Person(BaseType):
    '''
    classdocs
    '''
    
    roles=[]
    agent=[]

    def __init__(self):
        '''
        Constructor
        '''
    
    def toType(self,client):
        ret = {"sourcedGUID":{
                              "refAgentInstanceID":"testing",
                              "sourcedId":"testing"
                             },
               "person":{
                         "formname":[{"formnameType":"First", # B1.1
                                     "formattedName":"Testing Full Name"
                                     }],
                         "name":{"nameType":   {"instanceIdentifier":{"textString":"First"},"instanceValue":{"textString":"First"}}, #B1.2
                                  "partName":   [{"instanceIdentifier":{"textString":"First"},"instanceValue":{"textString":"First"},"instanceName":{"textString":"First"}},
                                                 {"instanceIdentifier":{"textString":"Last"},"instanceValue":{"textString":"Last"},"instanceName":{"textString":"Last"}}] #B1.3
                                 },
                         #"address":{
                         #         },
                         #"contactinfo":{
                         #               },
                         #"demographics":{
                         #                },
                         #"agent":{"agentType":"agent"
                         #         },
                         "roles":[{"enterpriserolesType":"StudentInformationSystem",
                                   "systemRole":"User",
                                   "institutionRole":"Student",
                                   "userId":{"userIdValue":{"textString":"testing"},
                                             "userIdType":{"textString":"userId"},
                                             "password":{"textString":"PASSWORD"},
                                             #"pwEncryptionType":{"textString":"None"},
                                             "authenticationType":{"textString":"SSO"}
                                             }
                                  }],
                         "extension":{"extensionField":{"fieldName":"dataSourceKey",
                                                        "feldType":"String",
                                                        "fieldValue":"LMS_INTEGRATION"
                                                        }
                                      }
                         }
               
               }
        return ret
    
    def toType2(self,client):
        personRecord = client.factory.create('personRecord')
        personRecord.sourcedGUID="NEWFEED"
        personType = client.factory.create('person')
        formname = client.factory.create('formname')
        name = client.factory.create('name')
        address = client.factory.create('address')
        contactinfo = client.factory.create('contactinfo')
        demographics = client.factory.create('demographics')
        agent = client.factory.create('agent')
        roles = client.factory.create('roles')
        roles.systemRole="User"
        userId = client.factory.create('userId')
        userId.userIdValue="cdg2"
        #userId.userIdType="1"
        #userId.pwEncryptionType="NONE"
        #userId.authenticationType="LDAP"
        #userId.password="BLAH"
        roles.userId=userId
        extension = client.factory.create('extension')
        personType.formname = formname
        personType.name=name
        personType.address=address
        personType.contactinfo=contactinfo
        personType.demographics=demographics
        personType.agent=agent
        personType.roles=roles
        personType.extension=extension
        personRecord.person=personType
        return personRecord