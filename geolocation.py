__author__ = 'Brad_PC'
import time
import sys
import datetime
import ephem
import urllib.request as geturl
import xmlUtility,xmltodict, collections
import parser

def sunsetfix():
    righthere=ephem.Observer()
    print(GetLongitude())
    righthere.lat=-34.0274634
    righthere.lon=150
    #righthere.date= GetTimeNow()
    print(righthere.next_setting(ephem.Sun(), use_center=True))


def SunsetQuery(d):
    #Get the current location and then determine Sunset time
    righthere=ephem.Observer()
    # righthere.lat=GetLatitude()
    righthere.lon=GetLongitude()
    righthere.date= GetTimeNow()


    timeforlights=righthere.next_setting(ephem.Sun(), use_center=True)
    x=timeforlights.datetime()
    #print("Latitude: ", righthere.lat, " Longitude: ", righthere.lon, "Date and Time: ", x)
    x=x+datetime.timedelta(days=-1,seconds= int(xmlUtility.GetfromXML("General", "UTCOffset")))
    #print("Time for lights: ",x)
    #print("Time Now: ",d )
    #print(d, ">", x, " and ", d, "<", GetTimeOff())
    if d > x and d < GetTimeOff():
        return True
    else:
        return False

def GetUTCOffset():
    ts=datetime.datetime.timestamp(datetime.datetime.now())
    x=datetime.datetime.fromtimestamp(ts) - datetime.datetime.utcfromtimestamp(ts)
    #print("UTC Offset: ",x)
    return x.seconds

def GetTimeNow():
    return datetime.datetime.now()

def GetTimeOff():
    x=datetime.datetime.now()
    #print ("Pre time:",x)
    y= x.replace(hour=20, minute=20, second=0, microsecond=0)
    #print ("Turn off:",y)
    return y

def geocode(address):
    address = geturl.quote('https://maps.googleapis.com/maps/api/geocode/xml?address=%s' % address, safe="%/:=&?~#+!$,;'@()*[]" )
    req= geturl.urlopen(address)
    print(address)
    response = req.read()
    req.close()
    response = xmltodict.parse(response)
    print(response)
    return response['GeocodeResponse']['result']['geometry']['location']

def GetLatitude():
    x= xmlUtility.GetfromXML("General", "lat")
    return x

def GetLongitude():
    x= xmlUtility.GetfromXML("General", "lng")
    return x
