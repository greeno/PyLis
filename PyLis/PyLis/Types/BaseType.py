'''
Created on Jul 2, 2012

@author: cdg2
'''

class BaseType(object):
    '''
    classdocs
    '''
    def toType( self, client ):
        """
        Each Type should convert from Pythonic type to Xml Type.
        """
        raise NotImplementedError( "This class needs to implement toType" )

    def __init__(self):
        '''
        Constructor
        '''
        self.toType()
        