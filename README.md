PyLis
=====

Learning Information Services(LIS) implementation for Blackboard Learn in Python

Available Functions for BbLearn
=====

PersonManagementServiceSyncService
-----
### AVAILABLE
+ createPerson(GUID.Type sourcedId, PersonRecord.Type personRecord, )
+ deletePerson(GUID.Type sourcedId, )
+ replacePerson(GUID.Type sourcedId, PersonRecord.Type personRecord, )


### UNAVAILABLE
+ changePersonIdentifier(GUID.Type sourcedId, GUID.Type newSourcedId, )
+ createByProxyPerson(PersonRecord.Type personRecord, )
+ deletePerson(GUID.Type sourcedId, )
+ discoverPersonIds(QueryObject.Type queryObject, )
+ readAllPersonIds()
+ readPerson(GUID.Type sourcedId, )
+ readPersonCore(GUID.Type sourcedId, )
+ readPersonIdsFromSavePoint(SequenceIdentifier.Type fromSavePoint, )
+ readPersons(GUIDSet.Type sourcedIdSet, )
+ readPersonsFromSavePoint(SequenceIdentifier.Type fromSavePoint, )
+ replacePerson(GUID.Type sourcedId, PersonRecord.Type personRecord, )
+ updatePerson(GUID.Type sourcedId, PersonRecord.Type personRecord, )

BulkDataExchangeManagementServiceSyncService
----
### AVAILABLE
+ announceBulkDataExchange(LUID.Type transactionId, BulkBlockManifest.Type bulkBlockManifest, )

### UNAVAILABLE
+ announceFailureBulkDataExchange(LUID.Type transactionId, FailureReport.Type failureReport, )
+ cancelBulkDataExchange(LUID.Type transactionId, )
+ ignoreBulkDataExchange(LUID.Type transactionId, )
+ reportBulkDataExchange(LUID.Type transactionId, BulkBlockReport.Type bulkBlockReport, )
+ requestBulkDataExchange(LUID.Type transactionId, FilterObject.Type filter, )
