#!/usr/bin/env python
import sys
import re
import urllib
import urllib2
from urlparse import urlparse
import Image
import os
import httplib

TMP_IMAGE_FILE = 'C:\\tmp\\save_image'

def getExtension(url):
    return urlparse(url)[2].split(".")[-1].strip()
    
def readFromUrl(url):
    print url
    sys.stdout.flush()
    
    tmp = os.path.abspath("%s.%s"%(TMP_IMAGE_FILE,getExtension(url)))
    
    res = urllib2.urlopen(url,None,20).read()
    tmpFile = open(tmp,"wb")
    tmpFile.write(res)
    tmpFile.close()
    return tmp

def convertImage(src,dst):
    size=80,80
    im=Image.open(src)
    im.thumbnail(size,Image.ANTIALIAS)
    im.save(dst,"JPEG")


ROOTDIR=os.path.abspath('c:\\tmp\\SaveImages')

def normalizeFilename(fn):
    fn = fn.replace('"','')
    return fn.replace(' ','-')
    
    
def generateThumbnail(list,output):
    listWithImg = open(list,"r").read().split('\n')
    outFile = open(output,"w")
    
    for l in listWithImg:
#        print l
        store = l.split('\t')
        if(len(store)<2):
            continue
        
        dst = 'None'        
        try:
            img = readFromUrl(store[4])
            dst ="%s\\%s\\%s-%s.jpg"%(ROOTDIR,store[1].replace(' ','-'),store[0],normalizeFilename(store[2]))
            if(not os.path.exists(os.path.dirname(dst))):
                os.makedirs(os.path.dirname(dst))
        
            if(os.path.getsize(img)!=0):
                convertImage(img,dst)
            else:
                dst = 'None'
#        except (IOError,urllib2.HTTPError,httplib.BadStatusLine):
        except :
            dst = 'None'
        
        outFile.write("%s\t%s\n"%(store[0],dst))

    outFile.close()
    
    
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

    generateThumbnail(args[1],'thumbnailList.txt')   
        

if __name__ == '__main__':
    main(sys.argv)
