#!/usr/bin/env python

import sys
import urllib
import urllib2
import time
import simplejson


def getRestaurant(listfile):
    return open(listfile,"r").read().split('\n\n\n');

def getGeocodeFromGoogle(store,address,output):
    server="http://maps.googleapis.com/maps/api/geocode/json?address="
    url = "%s%s,%s,%s&sensor=false"%(server,address,"san francisco","CA")
    
    res=urllib2.urlopen(url.replace(' ','+'))
    print url
    
    #print res.read()
    resobj=simplejson.loads(res.read())
    #print resobj['results'][0]
    
    if(len(resobj['results'])<1):
        print "no result %s-%s"%(store,address)
        return
    
    
    result = resobj['results'][0]
    if(result is not None):
        print >>output,store
        location = result['geometry']['location']
        print >>output,"%s,%s"%(location['lat'],location['lng'])
        print >>output,result['formatted_address']
        print >>output,"\n"
        output.flush()
        
    
#    for item in resobj['results'][0].iteritems():
#        print item
    
def main(args):
    if (len(args) != 2):
        print "%s list.txt" %(args[0])

    stores = getRestaurant(args[1])

    OUTPUT = open("StoreWithLocation.txt","w")
    
    count=0
    for store in stores:
        if(store.strip() != ""):
            name,address,link = store.split('\n')        
            getGeocodeFromGoogle(name,address.split('|')[0],OUTPUT)
            count = count + 1
            print "%d-%s"%(count,name)
            time.sleep(60) 
            
    OUTPUT.close()

            
if __name__ == '__main__':
    main(sys.argv)