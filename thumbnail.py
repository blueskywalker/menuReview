#!/usr/bin/env python

import sys
import MySQLdb
import re
from _mysql_exceptions import OperationalError


def createMenuTable():
    db=MySQLdb.connect(host='localhost',port=3306,user='root',passwd='mysql')
    cur = db.cursor()
    try:
        cur.execute("drop table food.menuItems;");
    except OperationalError as dberr:
        if(dberr[0]==1051):
            pass
        else:
            raise dberr
 
    cur.execute("""
        use food;
        
        create table menuItems (
            id int not null auto_increment primary key,
            restid int not null references restaurant(id), 
            menu text not null,
            description text,
            image text,
            thumbnail text                
        );
    """)
    
    cur.close()
    db.commit()
    db.close()

def insertMenu(values):
#    try:
        db=MySQLdb.connect(host='localhost',port=3306,user='root',passwd='mysql')
        cur = db.cursor()

        cur.executemany( """
            INSERT INTO food.menuItems (restid,menu,description,image,thumbnail)
            VALUES (%s,%s,%s,%s,%s);
            """,values)

        cur.close()
        db.commit()
        db.close()

#    except DataError as derr:
#        print "DB Error"

def getRestId():
    
        db=MySQLdb.connect(host='localhost',port=3306,user='root',passwd='mysql')
        cur = db.cursor()

        cur.execute("SELECT id,name FROM food.restaurant;")
        
        ret = cur.fetchall()
        cur.close()
        db.close()
        
        return ret;

def removePrefix(path):
    return (path[16:]).replace('\\','/')

def removeParenthesis(name):
    m=re.search("(.+)(\(.*\))",name)
    if(m is None):
        return name
    else:
        return m.group(1).strip()
    
FILTER={ '2223 (closed)':'2223',
    "abigail's":"Abigail's Bakery Cafe".lower()    
}


def filterOut(name):
    if(FILTER.has_key(name)):
        return FILTER[name]
    return name

def restlookup():
    restId = getRestId()
    
    lookup=dict()
    for rest in restId:        
        lookup[rest[1].lower()]=rest[0]
    return lookup

def readFromList(listf,lookup):
    tmp = open(listf,"r").read().split('\n\n\n')
    ret={}
  
    #print len(tmp)
    
    for rest in tmp:
        store = rest.split('\n')
        if(len(store)!=3):
            continue
        
        key = filterOut(store[0].lower())
        #print "%s=>%s"%(store[0],key)
        try:
            ret[store[2].split('/')[2].replace('-',' ')]=lookup[key]
        except:
            print  "skip:" +store[2].split('/')[2].replace('-',' ')
            continue
    
    return ret
    
    
def main(args):
    if(len(args)<3):
        print "%s menuDB.tx list.txt"%(args[0])
        sys.exit()

    
    lookup=restlookup()
    
    lookup2=readFromList(args[2],lookup)
    
    
    data=open(args[1],"r").read().split('\n')
     
    values=[]
    for rec in data:
        menu = rec.split('\t')
        
        
        if(len(menu)==6):
            try:
                rid = lookup2[menu[1]]
                values.append((rid,menu[2].strip(),menu[3].strip(),menu[4].strip(),removePrefix(menu[5].strip())))
            except:
                print "skip:"+ menu[1]
                continue
                
    
    print len(values)
    createMenuTable()
    
    insertMenu(values)
    
    print "Finished========="    
    
if __name__ == '__main__':
    main(sys.argv)
    