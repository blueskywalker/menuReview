#!/usr/bin/env python
# -*- coding: utf-8 -*-


import MySQLdb
from _mysql_exceptions import OperationalError
from _mysql_exceptions import DataError
import sys

def readLocation(filename):
    stores=open(filename,"r").read().split("\n\n\n")
    
    ret= {}
    for store in stores:
        tmp=store.split('\n')
        if(len(tmp)==3):
            ret[tmp[0]]={'name':tmp[0],'location':tmp[1],'address':tmp[2]}    
            
    return ret

def readFromList(filename):
    stores=open(filename,"r").read().split("\n\n\n")
    
    ret = {}
    for store in stores:
        tmp = store.split('\n')
        if(len(tmp)==3):
            ret[tmp[0]]={'name':tmp[0],'address':tmp[1]}
    return ret

def normalize(loc,origin):
        
    for key in origin.keys()[:3]:        
        if(loc.has_key(key)):
            if(loc[key]['address'].split(' ')[0]!=origin[key]['address'].split(' ')[0]):
                print "%s != %s"%(loc[key]['address'],origin[key]['address'])
        
def createRestaurantTable():
    db=MySQLdb.connect(host='localhost',port=3306,user='root',passwd='mysql')
    cur = db.cursor()
    try:
        cur.execute("drop table food.restaurant;");
    except OperationalError as dberr:
        if(dberr[0]==1051):
            pass
        else:
            raise dberr
 
    cur.execute("""
        use food;
        create table restaurant (
            id int not null auto_increment primary key,
            name varchar(100) not null,
            street varchar(150),
            city varchar(50),
            state varchar(50),
            zip varchar(10),
            country varchar(30),
            latlng varchar(50),
            index(name),
            index(city),
            index(state),
            index(zip),
            index(street),
            index(country)
        );
    """)
    
    cur.close()
    db.commit()
    db.close()

def insertRestaurant(values):
#    try:
        db=MySQLdb.connect(host='localhost',port=3306,user='root',passwd='mysql')
        cur = db.cursor()

        cur.executemany( """
            INSERT INTO food.restaurant (name,latlng,street,city,state,zip,country)
            VALUES (%s,%s,%s,%s,%s,%s,%s);
            """,values)

        cur.close()
        db.commit()
        db.close()

#    except DataError as derr:
#        print "DB Error"
        
def main(args):
    if(len(args)<3):
        print "%s list.txt location.txt"%(args[0])
        sys.exit(-1)
    
#    origin = readFromList(args[1])
    
    location=readLocation(args[2])    
#    normalize(location,origin)    
    
    values=[]
    
    for key in location.keys():
        try:
            address = location[key]['address'].split(',')
            
            tmp = address[2].strip().split(' ')
            
            state=""
            zipcode=""
            
            if(len(tmp)!=2):
                if(tmp[0].isalpha()):
                    state=tmp[0]
                else:
                    state="CA"
                    zipcode=tmp[0]
            else:
                state=tmp[0]
                zipcode=tmp[1]
                
            values.append((location[key]['name'].strip(),location[key]['location'].strip(),
                address[0].strip(),address[1].strip(),state,zipcode,"USA"))
        except:
            # print location[key]
            continue
    
    print values[0]
    
#    createRestaurantTable()
    insertRestaurant(values)    
    print "Successfully done"

if __name__ == '__main__':
    main(sys.argv)