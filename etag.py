from dotmap import DotMap
import caldav
from caldav_utils import *
import json
import datetime
import dateutil
import traceback 

def etag_calendar(data):
    #Check if called from client side (not necessary)
    if(isinstance(data,str)):
        data = json.loads(data)

    #Connect to CalDav Account
    """
    account = frappe.get_doc("CalDav Account", data["caldavaccount"])
    """
    account = data["caldavaccount"]
    client = caldav.DAVClient(url=account.url, username=account.username, password=account.password)
    principal = client.principal()
    calendars = principal.calendars()

    #Look for the right calendar
    for calendar in calendars:
        if(str(calendar) == data["calendarurl"]):
            cal = calendar
    
    #Go through Events
    events = cal.events()

    #Stats
    stats = {
        "1a" : 0,
        "1b" : 0,
        "1c" : 0,
        "2a" : 0,
        "3a" : 0,
        "3b" : 0,
        "4a" : 0,
        "else" : 0,
        "error" : 0,
        "not_inserted" : 0,
        "exception_block_standard" : 0,
        "exception_block_meta" : 0
    }
    rstats = {
        "norrule" : 0,
        "daily" : 0,
        "weekly" : 0,
        "monthly" : 0,
        "yearly" : 0,
        "finite" : 0,
        "infinite" : 0,
        "total" : len(events),
        "singular_event" :0,
        "error" : 0,
        "exception" :0
    }
    #Error Stack
    error_stack = []

    for event in events:
        vev = event.vobject_instance.vevent

        etagb = 