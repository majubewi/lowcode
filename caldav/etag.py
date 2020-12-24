#Retrieve etags
uida = "98342-750239-873205"
uidb = "98342-750239-873345"
created = datetime.datetime.now()
last_modified = datetime.datetime.now()

etaga = etag(uida,created,last_modified)
etagb = etag(uidb,created,last_modified)

#Get instructions for event
instr = make_instructions(uid,etaga, etagb)


#Get corresponding objects