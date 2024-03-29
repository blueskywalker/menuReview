#!/usr/bin/env python

import sys
import urllib2
import urllib
import simplejson
import time

def getImage(qry):
    
    url = "%s%s%s" % ('https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q=',
                    urllib.quote(qry),'&userip=50.131.148.185')
    
#    print url
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    
    # Process the JSON string.
    
    results = simplejson.load(response)

#    print results['responseData']['results'][0]['url']
    return results['responseData']['results'][0]['url']

def main(args):
    if(len(args)!=2):
        print "%s menus.txt"%(args[0])
        return
    
    menus = open(args[1],"r").read().split('\n')
    
    OUT = open("images.txt","w")
    
    for menu in menus:
        try:
            time.sleep(1)            
            print "%s|%s" % (menu,getImage(menu))
            print >> OUT, "%s|%s" % (menu,getImage(menu))
            OUT.flush()
        except:
            continue
    
    OUT.close()
    
# now have some fun with the results...

if __name__ == '__main__':
    main(sys.argv)