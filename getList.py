#/usr/bin/env python

import urllib
import urllib2
import sys


 
def main(args):
    
    url='http://localhost:8080/select'
#    url='http://data-service-jubshi.appspot.com/insert'
    
    opts = {"city":'san francisco'}
    param=urllib.urlencode(opts)
    
    
    req = urllib2.Request(url+ '?' + param)
    req.add_header('Content-Encoding','gzip')    

    print req.get_full_url()
#    sys.exit()
    res = urllib2.urlopen(req )
    
    print res.read()
    
        
if __name__ == "__main__":
    main(sys.argv)