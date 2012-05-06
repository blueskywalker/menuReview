#!/usr/bin/env python

import sys
import solr
import os
import traceback

def main(argv):
    if len(argv)<3:
        print "%s list.txt menu.txt"%(argv[0])
        sys.exit(0)
        
    print 'open %s' % (argv[1])    
    txt=open(argv[1],"r").read()
    list = txt.split('\n\n\n')
    rest = dict()
    for store in list:
        try:
            details = store.split('\n')
            name = details[2].split('/')
            print name[2]
            rest[name[2].replace('-',' ')]=details[1]
        except:
            print 'skip'
      
    
    list = open(argv[2],"r").read().split('\n')
    
    host = "http://192.168.1.3:8983/solr"               
    #host="http://localhost:8983/solr"
    
    s = solr.SolrConnection(host)
     
    #print rest['2223']    
    #sys.exit()
    
    count=1
    for item in list:
        try:
            print item
            itemlist = item.split('|')
            s.add(id=str(count), restaurant=itemlist[0],menu=itemlist[1],
                  description=itemlist[2] or "",
                  address=rest[str(itemlist[0]).lower()],
                  city="san francisco",
                  state="CA",
                  image=itemlist[3])
            count+=1
        except:
            continue
            print "Exception in user code:"
            print '-'*60
            traceback.print_exc(file=sys.stdout)
            print '-'*60
            break
    s.commit()

if __name__ == '__main__':
    main(sys.argv)