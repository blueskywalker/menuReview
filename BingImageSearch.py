#!/usr/bin/env python

import sys
import urllib
import urllib2
from bs4 import BeautifulSoup

def getImage(qry):
    
    host='http://www.bing.com/images/search?'
    # query="q=%s&go=&qs=n&form=QBIR&pq=%s&sc=7-5&sp=-1&sk="% (urllib.quote(qry),urllib.quote(qry))
    query="q=%s&go=&qs=n&form=QBIR&pq=%s&sc=7-5&sp=-1&sk="% (urllib.quote(qry),urllib.quote(qry))
    url = host + query

#    print url
    
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)

    dom = BeautifulSoup(response.read())
    result=dom.find(id="sg_results")
    list=result.select('.sg_u')

    return list[0].img['src']

    
def main(args):
    if(len(args)!=2):
        print "%s menus.txt"%(args[0])
        return
    
    menus = open(args[1],"r").read().split('\n')
    OUT = open("ImagesResult.txt","w")
    
    for menu in menus:
        try:
            print >>OUT,"%s|%s" % (menu,getImage(menu))
            OUT.flush()
        except:
            continue

    OUT.close()
    

if __name__ == '__main__':
    main(sys.argv)
