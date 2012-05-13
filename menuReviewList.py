#!/usr/bin/env python
import sys
import re
import urllib
import urllib2
from urlparse import urlparse
import Image

TMP_IMAGE_FILE = '/tmp/save_image'

def getExtension(url):
    return urlparse(url)[2].split(".")[-1].strip()
    
def readFromUrl(url):
    print url
    tmp = "%s.%s"%(TMP_IMAGE_FILE,getExtension(url))
        
    res = urllib2.urlopen(url).read()
    tmpFile = open(tmp,"wb")
    tmpFile.write(res)
    tmpFile.close()
    return tmp

def convertImage(src,dst):
    size=80,80
    im=Image.open(src)
    im.thumbnail(size,Image.ANTIALIAS)
    im.save(dst,"JPEG")
 
def generateThumbnail(list):
    listWithImg = open(list,"r").read().split('\n')

    for l in listWithImg:
        store = l.split('|')
        tmp = readFromUrl(store[4])
        convertImage(tmp,'/tmp/thumb.jpg')        
        break

def filterOutBug(store):
    if (not store[3].startswith('http')):
        if (len(store)>4 and store[4].startswith('http')):
            return store[4]
        else:
            return None
    return store[3]
    
def makeListWithId(src,dst):
    listWithImg = open(src,"r").read().split('\n')
    dstFile = open(dst,"w")
    
    count=0
    for l in listWithImg:
        store = l.split('|')
        count = count + 1
        if(len(store) <2):
            continue
        
        desc = store[2]
        uri = store[3]    
        if (not store[3].startswith('http')):
            if(len(store)>4 and store[4].startswith('http')):
                uri = store[4]
                desc = "%s %s"%(store[2],store[3])
            else:
                continue
        
        m=re.search("url=(.*)",uri)
        url=urllib.unquote(m.group(1))
        
        dstFile.write("%d\t%s\t%s\t%s\t%s\n"%(count,store[0],store[1],desc,url))
    
    dstFile.close()
    
        
def main(args):
    if(len(args)!=2):
        print "%s listWithImage.txt" %(args[0])
        return
    
#    makeListWithId(args[1],'listWithId.txt')
    generateThumbnail(args[1])   
        

if __name__ == '__main__':
    main(sys.argv)