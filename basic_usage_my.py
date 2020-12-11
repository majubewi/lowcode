import datetime
import sys



## We'll try to use the local caldav library, not the system-installed
sys.path.insert(0, '..')

import caldav
from icalendar import vDatetime

import dateutil
import re

import utils

## CONFIGURATION.  The minimum requirement is an URL.  Username and
## password is also probably nice to have.  The DAVClient object also
## supports a proxy (URL), an auth object (to be passed to the
## requests library, instead of using username and password) and a
## boolean ssl_verify_cert that can be set to False for self-signed
## certificates.
try:
    ## To make it easy to actually execute this test code, connection
    ## details to your caldav server can be given in the
    ## tests/conf_private.py file (check conf_private.py.EXAMPLE)
    from conf_private import caldav_servers
    url = caldav_servers[0]['url']
    username = caldav_servers[0]['username']
    password = caldav_servers[0]['password']
    
except ImportError:
    ## ...or you can just edit this file and put your private details here
    url = 'https://example.com/caldav.php'
    username = 'somebody'
    password = 'hunter2'


## A DAVClient object should be set up with the connection details.
## Initiating the object does not cause any requests to the server.
client = caldav.DAVClient(url=url, username=username, password=password)

## You may list up the calendars you own through the principal-object
my_principal = client.principal()
calendars = my_principal.calendars()
c = calendars[0]
es = c.events()

#----------------------------------------------START-----------------
for e in es:
    vev = e.vobject_instance.vevent

    #RRULE CONVERSION (APPROACH 1: REAL MAPPING)
    if(hasattr(vev,"rrule")):
        #print(list(vev.getrruleset())) #potentially infinite
        #print(str(vev.dtstart.value.day) + "th is " + str(vev.dtstart.value.strftime("%a")))
        print("------------------------------------------")
        print(vev.dtstart.value)
        print("DOW dtstart: " + str(vev.dtstart.value.weekday()))
        print(vev.rrule.value)

        rule = dateutil.rrule.rrulestr(vev.rrule.value,dtstart=vev.dtstart.value)

        #Include only mappable rrules
        if(isMappable(vev)):
            #DAILY
            if(rule._freq == 3 and noByDay(vev.rrule.value)):
                repeat_this_event = 1
                repeat_on = "Daily"
                until = getUntil(vev.dtstart.value.date(),rule)
                if until:
                    repeat_till = until.strftime("%Y-%m-%d")
            #DAILY to WEEKLY (Special Case)
            elif(rule._freq == 3 and not noByDay(vev.rrule.value)):
                match = re.search(r'BY[A-Z]{4,5}DAY',vev.rrule.value) #Catches BYWEEKDAY, BYMONTHDAY and BYYEARDAY
                if match:
                    print("Special Case not applicable")
                else:
                    repeat_this_event = 1
                    repeat_on = "Weekly"
                    until = getUntil(vev.dtstart.value.date(),rule)
                    print(rule._byweekday)
                    if until:
                        repeat_till = until.strftime("%Y-%m-%d")
                    if 0 in rule._byweekday:
                        monday = 1
                    if 1 in rule._byweekday:
                        tuesday = 1
                    if 2 in rule._byweekday:
                        wednesday = 1
                    if 3 in rule._byweekday:
                        thursday = 1
                    if 4 in rule._byweekday:
                        friday = 1
                    if 5 in rule._byweekday:
                        saturday = 1
                    if 6 in rule._byweekday:
                        sunday = 1
            #WEEKLY
            elif(rule._freq == 2):
                repeat_this_event = 1
                repeat_on = "Weekly"
                until = getUntil(vev.dtstart.value.date(),rule)
                print(rule._byweekday)
                if until:
                    repeat_till = until.strftime("%Y-%m-%d")
                if 0 in rule._byweekday:
                    monday = 1
                if 1 in rule._byweekday:
                    tuesday = 1
                if 2 in rule._byweekday:
                    wednesday = 1
                if 3 in rule._byweekday:
                    thursday = 1
                if 4 in rule._byweekday:
                    friday = 1
                if 5 in rule._byweekday:
                    saturday = 1
                if 6 in rule._byweekday:
                    sunday = 1
            #MONTHLY
            elif(rule._freq == 1 and noByDay(vev.rrule.value) and isNotFebruaryException(vev.dtstart.value.date())):
                repeat_this_event = 1
                repeat_on = "Monthly"
                until = getUntil(vev.dtstart.value.date(),rule)
                if until:
                    repeat_till = until.strftime("%Y-%m-%d")
            #YEARLY
            elif(rule._freq == 0 and noByDay(vev.rrule.value) and isNotFebruaryException(vev.dtstart.value.date())):
                repeat_this_event = 1
                repeat_on = "Yearly"
                until = getUntil(vev.dtstart.value.date(),rule)
                if until:
                    repeat_till = until.strftime("%Y-%m-%d")
            #Not mapped
            else:
                print("->Generally mappable but ERROR")
        #Not mappable but finite
        elif(getUntil(vev.dtstart.value.date(),rule) is not None):
            datetimes = list(vev.getrruleset())
            print("->WARNING")
            vev.prettyPrint()
        #Not mappable and infinite
        else:
            print("->ERROR")
            vev.prettyPrint()

    

        





            

                
                



