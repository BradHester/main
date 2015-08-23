__author__ = 'Brad_PC'
import serial
import geolocation
import xmlUtility
import LogUtility
import LightUtility
import time

#main

TimeNow=geolocation.GetTimeNow()

if xmlUtility.GetfromXML("Lights","overrideon")=="True":
    print("Override On")
    z=time.strptime(xmlUtility.GetfromXML("Lights","OverrideTime"),"%H:%M")
    y= TimeNow.replace(hour=z.tm_hour, minute=z.tm_min, second=0, microsecond=0)
    if TimeNow > y and TimeNow < LightUtility.GetTimeOff():
        print("Lights should be on")
        if LightUtility.AreLightsOn()==0:
            LightUtility.TurnLightsOn()
        else:
            print("Lights already Running")
    else:
        if LightUtility.AreLightsOn()==1:
            LightUtility.TurnLightsOff()
        else:
            print("Nothing to do here")
else:
    print("Override Off")
    if TimeNow > LightUtility.GetTimeOn():
        print("Lights should be on")
    else:
        print("Lights should be off")