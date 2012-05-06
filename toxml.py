try:
    from lxml import etree
    print("running with lxml.etree")
except ImportError:
    try:
        # Python 2.5
        import xml.etree.cElementTree as etree
        print("running with cElementTree on Python 2.5+")
    except ImportError:
        try:
            # Python 2.5
            import xml.etree.ElementTree as etree
            print("running with ElementTree on Python 2.5+")
        except ImportError:
            try:
                # normal cElementTree install
                import cElementTree as etree
                print("running with cElementTree")
            except ImportError:
                try:
                    # normal ElementTree install
                    import elementtree.ElementTree as etree
                    print("running with ElementTree")
                except ImportError:
                    print("Failed to import ElementTree from any known place")


import sys
import htmllib
  
def main(args):
    if(len(args)!=3):
        print "Usage : %s input output" % (args[0])
        sys.exit()
        
    listFile = open(args[1],"r")
    alldata = listFile.read()
    list = alldata.split('\n')
    
    root = etree.Element("root")
    
    for menu in list:
        try:            
            items = menu.split('|')
            if len(items)<2:
                continue
            item = etree.SubElement(root, "item")
            rest = etree.SubElement(item,"restaurant")
            rest.text = items[0]
            menu = etree.SubElement(item, "menu")
            menu.text = items[1]
            if items[2] is not None or len(items[2])>0:
                desc = etree.SubElement(item, "description")
                desc.text = items[2]
        except:
            print "error or end of list"
 
    outFile = open(args[2],"w")           
    outFile.write(etree.tostring(root, pretty_print=True))
        
    
if __name__ == "__main__":
    main(sys.argv)
    