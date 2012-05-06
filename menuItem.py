#!/usr/bin/env python

import sys
import re

invList=dict()

def processItem(item):
    items = item.split('|')
    if(len(items)<2):
        return

    if(invList.has_key(items[1])):
        invList[items[1]].append(items[0])
    else:
        invList[items[1]]=[items[0],]
        
        

def parse(menuFile):
    return open(menuFile,"r").read().split('\n')

def main(args):
    if (len(args)<2):
        print("%s menuList"%(args[0]))
        sys.exit(0)
        
    menuList = parse(args[1])
    
    for menuItem in menuList:
        processItem(menuItem)
    
    comp = re.compile('([#\w]*)\.\s*(.*)')

    for k,v in invList.iteritems():
        m=comp.match(k)
        if m is not None:
            print m.group(2) 
        else:
            print k

    
if __name__ == '__main__':
    main(sys.argv)