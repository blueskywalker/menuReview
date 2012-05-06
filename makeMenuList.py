#!/usr/bin/env python

from bs4 import BeautifulSoup
import htmllib
import os
import fnmatch


datadir = "/Users/blueskywalker/Testbed/data/sanFrancisco/"
menuListFile = open(datadir+"MenuList.txt","w")

def getRestaurantName(path):
    fileName = os.path.basename(path)
    ep = fileName.rfind(".html")
    return fileName[0:ep].replace('-',' ')

def parseMenu(fileName):
    
    dom=BeautifulSoup(open(fileName,"r"))
    try:
        table = dom.find(id="restaurant-menu")
        for menu in table.find_all("th"):
            detail= menu(text=True)
            try:
                print >> menuListFile,"%s|%s|%s" % (getRestaurantName(fileName),detail[1],detail[2].strip())
            except:
                print "error item"
    except:
        print "skip:"+fileName
            
def scanFiles():
    for fn in os.listdir(datadir):
        if (fnmatch.fnmatch(fn, '*.html')):
            parseMenu(datadir+fn)
            
            
def main():
   scanFiles()
#    parseMenu(datadir+'zare-at-fly-trap.html')    
    
if __name__ == "__main__":
    main()