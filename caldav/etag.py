from syncmap import SyncMap
import datetime

#Item Sync Meta Information
uid = "98342-750239-873205"
created = datetime.datetime.now()
last_modified = datetime.datetime.now()


#Get instructions for event
syncmap = SyncMap("url://mycalendar")
etaga = syncmap.etag(uid,created,last_modified)
etagb = syncmap.etag(uid,created,last_modified)
instruction = syncmap.compile_instruction(uid,None,None)
print(instruction)

#Execute instruction
synced = False
if(instruction["Cmd"] == "Copy"):
    for target in instruction["Target"]:
        if(target == "A"):
            # Copy from remote to local
            pass

        if(target == "B"):
            # Copy from local to remote
            pass
elif(instruction["Cmd"] == "Delete"):
    for target in instruction["Source"]:
        if(target == "A"):
            # Delete from local
            pass

        if(target == "B"):
            # Delete from remote
            pass
elif(instruction["Cmd"] == "Conflict"):
    # Conflict logging or resultion
    pass
else:
    raise Exception("Synchronisation Error. Unknown instruction for syncing event with UID " + str(uid))

#Update Status if execution successfull
syncmap.update_status(uid,etaga,etagb)