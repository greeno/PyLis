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

CourseSectionManagerSyncService
----
### AVAILABLE
+ createCourseSection(GUID.Type sourcedId, CourseSectionRecord.Type courseSectionRecord, )
+ deleteCourseSection(GUID.Type sourcedId, )
+ replaceCourseSection(GUID.Type sourcedId, CourseSectionRecord.Type courseSectionRecord, )
### UNAVAILABLE
+ changeCourseSectionIdentifier(GUID.Type sourcedId, GUID.Type newSourcedId, )
+ createByProxyCourseSection(CourseSectionRecord.Type courseSectionRecord, )
+ createCourseSectionFromCourseSection(GUID.Type sourcedId, Text.Type academicSession, GUID.Type newSourcedId, )
+ discoverCourseSectionIds(QueryObject.Type queryObject, )
+ readAllCourseSectionIds()
+ readCourseSection(GUID.Type sourcedId, )
+ readCourseSectionIdsFromSavePoint(SequenceIdentifier.Type fromSavePoint, )
+ readCourseSections(GUIDSet.Type sourcedIdSet, )
+ readCourseSectionsFromSavePoint(SequenceIdentifier.Type fromSavePoint, )
+ updateCourseSection(GUID.Type sourcedId, CourseSectionRecord.Type courseSectionRecord, )
+ updateCourseSectionStatus(GUID.Type sourcedId, xs:normalizedString status, )

GroupManagementServiceSyncService
----
### AVAILABLE
+ createGroup(GUID.Type sourcedId, GroupRecord.Type groupRecord, )
+ deleteGroup(GUID.Type sourcedId, )
+ replaceGroup(GUID.Type sourcedId, GroupRecord.Type groupRecord, )
### UNAVAILABLE
+ addGroupRelationship(GUID.Type sourcedId, Relationship.Type relationship, )
+ changeGroupIdentifier(GUID.Type sourcedId, GUID.Type newSourcedId, )
+ createByProxyGroup(GroupRecord.Type groupRecord, )
+ discoverGroupIds(QueryObject.Type queryObject, )
+ readAllGroupIds()
+ readGroup(GUID.Type sourcedId, )
+ readGroupIdsForPerson(GUID.Type personSourcedId, )
+ readGroupIdsFromSavePoint(SequenceIdentifier.Type fromSavePoint, )
+ readGroups(GUIDSet.Type sourcedIdSet, )
+ readGroupsFromSavePoint(SequenceIdentifier.Type fromSavePoint, )
+ removeGroupRelationship(GUID.Type sourcedId, GUID.Type relationId, )
+ updateGroup(GUID.Type sourcedId, GroupRecord.Type groupRecord, )

MembershipManagementServiceSyncService
----
### AVAILABLE
+ createMembership(GUID.Type sourcedId, MembershipRecord.Type membershipRecord, )
+ deleteMembership(GUID.Type sourcedId, )
+ replaceMembership(GUID.Type sourcedId, MembershipRecord.Type membershipRecord, )
### UNVAILABLE
+ changeMembershipIdentifier(GUID.Type sourcedId, GUID.Type newSourcedId, )
+ createByProxyMembership(MembershipRecord.Type membershipRecord, )
+ discoverMembershipIds(QueryObject.Type queryObject, )
+ readAllMembershipIds()
+ readMembership(GUID.Type sourcedId, )
+ readMembershipIdsForCollection(GUID.Type groupSourcedId, MembershipIdType.Type collection, )
+ readMembershipIdsForPerson(GUID.Type personSourcedId, )
+ readMembershipIdsForPersonWithRole(GUID.Type personSourcedId, Role.Type role, GUIDSet.Type sourcedIdSet, )
+ readMembershipIdsFromSavePoint(SequenceIdentifier.Type fromSavePoint, )
+ readMemberships(GUIDSet.Type sourcedIdSet, )
+ readMembershipsFromSavePoint(SequenceIdentifier.Type fromSavePoint, )
+ updateMembership(GUID.Type sourcedId, MembershipRecord.Type membershipRecord, )