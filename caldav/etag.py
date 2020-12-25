from syncmap import SyncMap
import datetime

#Retrieve etags
uid = "98342-750239-873205"
created = datetime.datetime.now()
last_modified = datetime.datetime.now()


#Get instructions for event
syncmap = SyncMap("url://mycalendar")
etaga = syncmap.etag(uid,created,last_modified)
etagb = syncmap.etag(uid,created,last_modified)
print(syncmap.compile_instruction(uid,etaga,None))
syncmap.update_status(uid)




#Get corresponding objects