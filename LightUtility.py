__author__ = 'Brad_PC'
import random
import xmlUtility
import datetime
import time
import geolocation
import LogUtility
import random
import io

def AreLightsOn():
    if xmlUtility.GetfromXML("Lights","LightsOn")=="True":
        return True
    else:
        return False

def ShouldLightsBeOn():
    if GetTimeNow() > GetTimeOn():
        print("Sunset")
    else:
        print("Not Sunset")

def GetTimeOff():
    x=datetime.datetime.now()
    #print ("Pre time:",x)
    z=time.strptime(xmlUtility.GetfromXML("Lights","TimeOff"),"%H:%M")
    y= x.replace(hour=z.tm_hour, minute=z.tm_min, second=0, microsecond=0)
    print ("Turn off:",y)
    return y

def GetTimeOn():
    x=datetime.datetime.now()
    #print ("Pre time:",x)
    z=time.strptime(xmlUtility.GetfromXML("Lights","TimeNextOn"),"%H:%M")
    y= x.replace(hour=z.tm_hour, minute=z.tm_min, second=0, microsecond=0)
    print ("Turn on:",y)
    return y

def TurnLightsOn():
    LogUtility.writelog("Turning Lights On")
    xmlUtility.WriteToXML("Lights", "LightsOn", "True")

def TurnLightsOff():
    #datetime.datetime.strptime()
    z=geolocation.SunsetQuery().replace(minute=random.randrange(10,60))
    x= str(z.hour)+":"+str(z.minute)
    LogUtility.writelog("Turning Lights Off. Next time set for: %s" %x)
    xmlUtility.WriteToXML("Lights", "TimeNextOn", "x")
    xmlUtility.WriteToXML("Lights", "LightsOn", "False")