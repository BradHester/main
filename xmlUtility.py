__author__ = 'Brad_PC'

import os
from xml.etree.ElementTree import ElementTree
from xml.etree.ElementTree import Element
import xml.etree.ElementTree as ET
import urllib, json, pprint
import urllib.parse as urlparse
import geolocation


def CreateConfig():
    root = ET.Element("root")
    doc = ET.SubElement(root, "General")
    x = geolocation.GetUTCOffset()
    ET.SubElement(doc, "UTCOffset", name='UTCOffset').text = "%s" % x
    ET.SubElement(doc, "lat").text = geolocation.geocode("3 Galileo Street, Gregory Hills, New South Wales")['lat']
    ET.SubElement(doc, "lng").text = geolocation.geocode("3 Galileo Street, Gregory Hills, New South Wales")['lng']

    tree = ET.ElementTree(root)
    print(tree)
    tree.write("Config.xml")


def GetfromXML(element, entry):
    tree = ET.ElementTree(file='config.xml')
    rt = tree.getroot()
    for elem in rt.find(element):
        if elem.tag == entry:
            return elem.text

def TestXML():
    tree = ET.parse('config.xml')
    rt = tree.getroot()
    for elem in rt.find("General"):
        print(elem.tag)

def WriteToXML(element, entry, value):
    tree = ET.ElementTree(file='config.xml')
    rt = tree.getroot()
    for elem in rt.find(element):
        if elem.tag == entry:
           #print (elem.tag, value)
            elem.text = value
            tree.write("Config.xml")
