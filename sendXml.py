#/usr/bin/env python

import urllib
import sys

import MultipartPostHandler, urllib2, cookielib
from lxml import etree
from bs4 import BeautifulSoup



def send_by_multipart(url,city,data):
    
    cookies = cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookies),
                                MultipartPostHandler.MultipartPostHandler)
    params = { "username" : "jubshimesh@gmail.com", "password" : "hsemihsbuj",
           "city":city,"data" : data }
    opener.open(url, params)


def send_by_post(url,city,data):
    opts = {"city":city, "data":data}
    data=urllib.urlencode(opts)
    req = urllib2.Request(url)
    req.add_header('Content-Encoding','gzip')    
    req.add_data(data)
    print req.get_full_url()
    urllib2.urlopen(req)
    

def makeXmlElement(menus):
    root = etree.Element("root")

    for menu in menus:
        try:
            items = menu.split('|')        
            if len(items)<2:
                continue       
        
            item = etree.SubElement(root, "item")
            rest = etree.SubElement(item,"restaurant")
            rest.text = items[0]
            menu = etree.SubElement(item, "menu")
            menu.text = items[1]
            if len(items)>2:
                desc = etree.SubElement(item, "description")
                desc.text = items[2]
        except:
            print "skip"
            
    return etree.tostring(root, pretty_print=True)
    

def chunks(l,n):
    return [l[i:i+n] for i in range(0,len(l),n)]

def multiple_input(*args):  
    listFile = open(args[0],"r")
    alldata = listFile.read()
    items = alldata.split('\n')
    
    if(len(items)>0):
                
        for menu in chunks(items,100):
            data=makeXmlElement(menu)
            send_by_post(args[1],args[2],data)
#                    send_by_post(args[1],args[2],data)


     
def main(args):
    if(len(args)<2):
        print "%s xmlfile [local] "%(args[0])
        sys.exit()
    
    
    url='http://data-service-jubshi.appspot.com/insert'
    if len(args)>2 and args[2]=='local':
        url='http://localhost:8080/insert'

    city='san francisco'
    filename = args[1]
    
    multiple_input(filename,url,city)
    
#    send_by_post(url, city, filename)    
        
if __name__ == "__main__":
    main(sys.argv)