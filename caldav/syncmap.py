from jcache import JCache
import functools 
import hashlib
import datetime

#Source: https://unterwaditzer.net/2016/sync-algorithm.html

class SyncMap:
    def __init__(self,identifier):
        """
        The identifier is e.g. the calendar name or the address book name... must be unique.
        """
        self.identifier = identifier
        self.cache = JCache()
        self.status = {}
        self.load(self.identifier)

    def etag(self, uid, created, last_modified):
        etag_raw = uid + last_modified.strftime("%F %T") + created.strftime("%F %T")
        etag = hashlib.md5(etag_raw.encode('utf-8')).hexdigest()
        return etag
    
    def update_status(self, uid, etaga, etagb):
        new_entry = [etaga,etagb]
        entry = self.status.setdefault(uid,new_entry)
        if functools.reduce(lambda x, y : x and y, map(lambda p, q: p == q,entry,new_entry), True): 
            # Status did not change (entry === new_entry)
            raise Exception("Status update was unnecessary. No Syncoperation was required.")
        else: 
            # Status changed
            return True

    def load(self, identifier):
        try:
            self.status = self.cache.fetch(identifier)
        except:
            self.status = {}

    def save(self):
        self.cache.stash(self.identifier, self.status)
    
    def make_instruction(self, uid = None, a = False, b = False):
        """
        uid = Universal Identifier of the item
        a = Does it exist locally?
        b = Does it exist remote?
        """

        statustags = self.status.get(uid) 
        if(a and not b and not statustags):
            instruction = {
                "Cmd" : "Copy",
                "From" : "A",
                "To" : "B"
            }
            return instruction
        elif(not a and b and not statustags):
            instruction = {
                "Cmd" : "Copy",
                "From" : "B",
                "To" : "A"
            }
            return instruction
        

