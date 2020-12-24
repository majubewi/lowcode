import hashlib
import datetime

uid = "98342750239873205"
last_modified = datetime.datetime.now()
created = datetime.datetime.now()
etag_raw = uid + last_modified.strftime("%F %T") + created.strftime("%F %T")
etag = hashlib.md5(etag_raw.encode('utf-8')).hexdigest()

print(etag)