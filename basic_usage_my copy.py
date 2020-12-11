import datetime
import sys



## We'll try to use the local caldav library, not the system-installed
sys.path.insert(0, '..')

import caldav
from icalendar import vDatetime

import dateutil
import re

from caldav_utils import *

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

i = 0
#----------------------------------------------START-----------------


for e in es:
    vev = e.vobject_instance.vevent
    #vev = preprocessingVeventInstance(vev)

    i = i +1
    #RRULE CONVERSION (APPROACH 2: Artificial UNTIL for infinite sets) 
    """
    This version is easier than mapping to erpnext events when you think about the follwing usecase:
    A Calendarevent is mapped to ...
    """
    # https://pypi.org/project/recurring-ical-events/ function between()
    if(hasattr(vev,"rrule")):
        try:
            #Finite
            if(re.search(r'UNTIL|COUNT',vev.rrule.value)):
                datetimes = list(vev.getrruleset())
                
            #Infinite
            else:
                
                vev.rrule.value = vev.rrule.value + ";UNTIL=" + (datetime.datetime.now() + datetime.timedelta(days=10)).strftime("%Y%m%d")
                print(str(len(list(vev.getrruleset()))))
        except Exception as ex:
            
            print("Event No.: " + str(i))
            print("No Events total: " + str(len(es)))
            #vev.prettyPrint()
            #vev = makeComparable(vev)
            #print("-------------------__CHANGES__--------------------")
            #vev.prettyPrint()
            #print(str(len(list(vev.getrruleset()))))

            #vev = toNaiveFromVobjVevent(vev)
            
            #vev.prettyPrint()
            #print(str(vev))
            #matches = re.findall(r'\[datetime.datetime\([^\].]*\]',str(vev))
            #print(matches)
            #print(dir(vev))

            #print(vev.serialize())

            #print(traceback.format_exc())
            
            
            






            

                
                



