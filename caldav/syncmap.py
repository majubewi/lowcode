from jcache import JCache
import functools 
import hashlib
import datetime

#Source: https://unterwaditzer.net/2016/sync-algorithm.html

class SyncMap:
    def __init__(self,identifier):
        """
        The identifier is e.g. the account + calendar name / address book name... must be unique.
        Just take the CalDav-Resource URL...
        """
        self.identifier = identifier
        self.cache = JCache()
        self.status = {}
        self.load(self.identifier)

    def __del__(self):
        self.save()

    def etag(self, uid, created, last_modified):
        etag_raw = uid + last_modified.strftime("%F %T") + created.strftime("%F %T")
        etag = hashlib.md5(etag_raw.encode('utf-8')).hexdigest()
        return etag

    def delete_status(self, uid):
        self.update_status(uid)
    
    def update_status(self, uid, etaga = None, etagb = None):
        """
        After a successfull sync of the item this function needs to be called.
        """
        try:
            if(uid and (etaga or etagb)):
                if(etaga == None):
                    etaga = etagb
                elif(etagb == None):
                    etagb = etaga
                elif(etaga == None and etagb == None):
                    raise Exception("Must supply at least one etag.")

                uid = str(uid)
                new_entry = [etaga,etagb]
                entry = self.status.setdefault(uid,new_entry)
                if functools.reduce(lambda x, y : x and y, map(lambda p, q: p == q,entry,new_entry), True): 
                    # Status did not change (entry === new_entry)
                    pass
                else: 
                    # Status changed
                    self.status[uid] = new_entry
                return
            elif(uid):
                uid = str(uid)
                del self.status[uid]
        except KeyError as e:
            raise Exception("Synchronization Error. There is no cached entry for item with UID " + str(uid))

    def load(self, identifier):
        try:
            self.status = self.cache.fetch(identifier)
        except:
            self.status = {}

    def save(self):
        self.cache.stash(self.identifier, self.status)
    
    def compile_instruction(self, uid = None, a = None, b = None):
        """
        uid = Universal Identifier of the item
        a = etag of the local item if exists
        b = etag of the remote item if exists
        """

        statustags = self.status.get(uid) 
        if(a and not b and not statustags):
            instruction = {
                "Cmd" : "Copy",
                "Target" : ["B"]
            }
            return instruction
        elif(not a and b and not statustags):
            instruction = {
                "Cmd" : "Copy",
                "Target" : ["A"]
            }
            return instruction
        elif(a and not b and statustags):
            instruction = {
                "Cmd" : "Delete",
                "Target" : ["A","status"]
            }
            return instruction
        elif(not a and b and statustags):
            instruction = {
                "Cmd" : "Delete",
                "Target" : ["B","status"]
            }
            return instruction
        elif(a and b and not statustags):
            instruction = {
                "Cmd" : "Conflict",
                "Target" : []
            }
            return instruction
        elif(not a and not b and statustags):
            instruction = {
                "Cmd" : "Delete",
                "Target" : ["status"]
            }
            return instruction
        elif(a and b and statustags):
            if(statustags[0] != a and statustags[1] == b):
                instruction = {
                    "Cmd" : "Copy",
                    "Target" : ["B"]
                }
                return instruction
            elif(statustags[0] == a and statustags[1] != b):
                instruction = {
                    "Cmd" : "Copy",
                    "Target" : ["A"]
                }
                return instruction
            elif(statustags[0] != a and statustags[1] != b):
                instruction = {
                    "Cmd" : "Conflict",
                    "Target": []
                }
                return instruction
            else:
                raise Exception("Synchronisation Error. Modification of item with UID " + str(uid) + " locally and remote.")
        else:
            raise Exception("Synchronisation Error. Unseen case for item with UID " + str(uid))
        

