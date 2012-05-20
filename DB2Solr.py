#!/usr/bin/env python

import sys
import solr
import os

import MySQLdb

def readFromDB():
        
    db=MySQLdb.connect(host='localhost',port=3306,user='root',passwd='mysql')
    cur = db.cursor()

    cur.execute("""
        SELECT m.id, menu,description, name,street,city,state,zip,country,latlng,image,thumbnail FROM food.menuitems m,food.restaurant r
        where m.restid=r.id ;
    """)
    
    ret = cur.fetchall()
    cur.close()
    db.close()
    
    return ret;

def main():
    rows=readFromDB()

    print len(rows)
    
#    host = "http://192.168.1.3:8983/solr"               
    host = "http://localhost:8983/solr"               

    solrServer = solr.SolrConnection(host)
    
    print "connected"
    
    for row in rows:
        print row[1]
        try:
            solrServer.add(id=row[0],menu=row[1],
                  description=row[2],
                  restaurant=row[3],                  
                  address=row[4],
                  city=row[5],
                  state=row[6],
                  zipcode=row[7],
                  country=row[8],
                  location=row[9],
                  image=row[10],
                  thumbnail=row[11])
        except:
            continue
        
    solrServer.commit()
    print "Done"

if __name__ == '__main__':
    main()