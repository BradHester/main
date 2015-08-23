__author__ = 'Brad_PC'
import serial
import geolocation
import xmlUtility
import LogUtility

#main

if geolocation.SunsetQuery(geolocation.GetTimeNow()):
   print("Lights should be on")
   LogUtility.writelog("Lights should be on")
else:
    print("Lights should be off")
    LogUtility.writelog("Lights should be off")
#geolocation.GetTimeOff()
#lat = xmlUtility.GetfromXML("General", "lat")
#lng = xmlUtility.GetfromXML("General", "lng")

#print("Latitude : ,", lat + " Longitude: ", lng)
#xmlUtility.TestXML()#xmlUtility.CreateConfig()
#geolocation.sunsetfix()

