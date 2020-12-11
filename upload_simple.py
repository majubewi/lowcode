import caldav
from caldav_utils import *
import json
import datetime
import dateutil
import dateutil.rrule as RR
import pytz
import traceback 
import vobject

from dotmap import DotMap

def upload_calendar(data):
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
            
            
    
    
    new_calendar = vobject.newFromBehavior('vcalendar')
    e  = new_calendar.add('vevent')
    e.add('summary').value = "This is a note"
    dtstart = datetime.datetime(2020,12,2,9,0)
    e.add('dtstart').value = dtstart
    e.add('description').value = "Beschreibungstext"
    e.add('class').value = "Public" #Only Public, Private or Confidential !
    e.add('dtend').value = datetime.datetime(2020,12,2)
    e.add('last-modified').value = datetime.datetime.now()
    e.add('created').value = datetime.datetime.now()

    #Create rrule
    until = datetime.datetime(2020,12,31,9,0)
    rrule = RR.rrule(freq=RR.WEEKLY,until=until,byweekday=[RR.MO,RR.TU])
    print(rrule)

    

    ics = new_calendar.serialize()

    print(ics)

    #cal.save_event(ics)

    return json.dumps(ics)


if __name__ == "__main__":

    account = DotMap({
        "url" : "https://mail.tueit.de/SOGo/dav",
        "username" : "marius.widmann@tueit.de",
        "password" : "2f4bEc7N2h8nO2PgNVL1"
    })

    data = {
        "caldavaccount" : account,
        "calendarurl" : "https://mail.tueit.de/SOGo/dav/marius.widmann%40tueit.de/Calendar/personal/",
        "icalendar" : "Marius",
        "color" : "#ff4d4d"
    }

    message = upload_calendar(data)
    message = json.loads(message)
    #print(message["stats"])

