#!/usr/bin/env python

import sys
import re



def main(args):
    if (len(args)!=2):
        return
    
    txt = open(args[1],"r").read()


    v = re.compile('([#\w]*)\.\s*(.*)')
    
    for menu in txt.split('\n'):
        m=v.match(menu)
        if m is not None:
            print m.group(2) 
        else:
            print menu
            
if __name__ == '__main__':
    main(sys.argv)

