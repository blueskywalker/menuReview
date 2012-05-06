#!/usr/bin/env python

import sys
import re

imgdb=dict()

def getImgdb(imageFile):
    txt = open(imageFile,"r").read()

    for item in txt.split('\n'):
        menuList=item.split('|')
        if(len(menuList)!=2):
            continue
        imgdb[menuList[0]]=menuList[1]


def filterOut(menuFile):
    txt = open(menuFile,"r").read()

    v = re.compile('([#\w]*)\.\s*(.*)')
         
    for item in txt.split('\n'):
        try:
            lists=item.split('|')
            norm = v.match(lists[1])
            if norm is not None:
                menu=norm
            else:
                menu=lists[1]
            
            if(imgdb.has_key(menu)):
                print "%s|%s"%(item,imgdb[menu])
        except:
            pass

    
    
def main(args):
    if(len(args)!=3):
        print "%s image menua" % (args[0])
        return

    getImgdb(args[1])

    filterOut(args[2])


if __name__=="__main__":
    main(sys.argv)
