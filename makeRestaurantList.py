#!/usr/bin/env python

from bs4 import BeautifulSoup
import htmllib
 
datadir = "/Users/blueskywalker/Testbed/data/sanFrancisco/"

def unescape(s):
    p = htmllib.HTMLParser(None)
    p.save_bgn()
    p.feed(s)
    return p.save_end()


def extract(index):
    path = datadir+"restaurant.tidy"+str(index)+".html"
    storeFile = open(path,"r")
    stores = storeFile.read()
    
    dom = BeautifulSoup(stores)
    table = dom.find("table","search-results")
    names = table.find_all("td","name-address")

    for name in names:
        content= name(text=True)
        store= (name.a(text=True)[1])
        address = content[3].strip()
        link = name.a.get('href')
        
#        print "%s,%s,%s" % (store,address,link)
        print store.encode('utf-8')
        print address    
        print unescape(link)
        print "\n"
    
def main():
    for i in range(1,31):
        extract(i)

if __name__ == "__main__":
    main()
    
