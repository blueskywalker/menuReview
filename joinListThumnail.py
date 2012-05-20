#!/usr/bin/evn python

import sys
import os
from os import path

ROOT="C:\\Apache24\\ROOT\\thumnails"


def findThumb(rec):
    menu = rec.split('\t')
    print "%s-%s" % (menu[0],menu[1])
    thumbdir = "%s\\%s" %(ROOT,menu[1].replace(' ','-'))
    if (path.exists(thumbdir)):
        for f in os.listdir(thumbdir):
            if (f.split('-')[0]==menu[0]):
                fullpath = "%s\\%s"%(thumbdir,f)
                if(path.isdir(fullpath)):
                    founds= os.listdir(fullpath)
                    if(len(founds)>0):
                        menu.append(os.listdir(fullpath)[0])    
                    break
                else:
                    menu.append(fullpath)
                    break
    
    return menu
        

def writeOutput(filename,thumb):
    OUT = open(filename,"w")
    
    for item in thumb:
        OUT.write("%s\n"%('\t'.join(item)))
                  
    
    OUT.close()
    
    
def main(args):
    if (len(args)<2):
        print "%s img"%(args[0])
        sys.exit()
    
    OUT = open('thumbDB',"w")

    for l in open(args[1],"r").read().split('\n'):
        if(l!=""):
            menu=findThumb(l)
            withThumb = '\t'.join(menu)
            #print withThumb
            OUT.write("%s\n"%(withThumb))
        
    
    OUT.close()
    
    
if __name__ == '__main__':
    main(sys.argv)
    