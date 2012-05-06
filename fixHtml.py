#!/usr/bin/env python

from tidylib import tidy_document

datadir = "/Users/blueskywalker/Testbed/data/sanFrancisco/"

def fixHtml(index):
    path = datadir+"restaurant."+str(index)+".html"
    storeFile = open(path,"r")
    stores = storeFile.read()
    storeFile.close()
    document,errors = tidy_document(stores,options={ 'output-xhtml':1})

    outFile = open(datadir+"restaurant.tidy"+str(index)+".html","w")
    outFile.write(document)
    outFile.close()
    
def main():
    for i in range(1,31):
        fixHtml(i)
    
    
if __name__ == "__main__":
    main()
    
