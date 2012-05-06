#!/usr/bin/env python

from urllib2 import urlopen
import os
from tidylib import tidy_document
from bs4 import BeautifulSoup
import sys


dataDir="/Users/blueskywalker/Testbed/data/sanfrancisco/"
baseUrl='http://sanfrancisco.menupages.com'
url = baseUrl + '/restaurants/all-areas/all-neighborhoods/all-cuisines/'


def getRestaurant(max):
    if not os.path.exists(dataDir):
        os.makedirs(dataDir)
    
    for page in range(1,max):
        requestUrl = url + str(page) + "/"
        res = urlopen(requestUrl)       
        html=res.read()
        options = {'output-encoding':'utf8', 'output-xhtml':1 }
        document,errors = tidy_document(html,options)
        filePath = dataDir+"restaurant.tidy"+str(page)+".html"
        fd = open(filePath,"w")
        fd.write(document)
        fd.close()
        print filePath

def getMenu():
    storeFile = open("list.txt","r")
    txt = storeFile.read()
    storeFile.close()
    
    list=txt.split('\n\n\n')
    

 #   print list
    
    for store in list:    
#        print store
        rest = store.split('\n')
        if len(rest)!=3:
            break
        try:
            url=baseUrl+rest[2] +'menu'
            print url
            res=urlopen(url)
            html=res.read()    
         
            options = {'output-encoding':'utf8', 'output-xhtml':1 }
            document,errors = tidy_document(html,options)   
            
            filepath = dataDir+ (rest[2].split('/'))[2] + ".html"
            saveFile = open(filepath,"w")
            saveFile.write(document)
            saveFile.close()
            print filepath
        except :
            print "skip:"+url
            
#    dom = BeautifulSoup(document).prettify()
#    print dom
        
def main():
#    getRestaurant(31)
    getMenu()
    
if __name__ == "__main__":
    main()
    
