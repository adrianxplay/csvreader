import csv
gmail = 0
yahoo = 0
live = 0
hotmail = 0
audi = 0
vw = 0
outlook = 0

with open('BDDTotal-audi.csv', 'rU') as emaillist:
    spamreader = csv.reader(emaillist, dialect=csv.excel_tab)
    row_count = 0;
    for row in spamreader:
        row_count += 1
        tmp = row[0]
        if "GMAIL" in tmp.upper() : gmail+=1
        elif "OUTLOOK" in tmp.upper() : outlook+=1
        elif "YAHOO" in tmp.upper() : yahoo+=1
        elif "LIVE" in tmp.upper() : live+=1
        elif "AUDI.COM.MX" in tmp.upper() : audi+=1
        elif "VW-CONCESIONARIOS" in tmp.upper() : vw+=1
        elif "HOTMAIL" in tmp.upper() : hotmail+=1

    print "REGISTROS: " + str(row_count)
    print "GMAIL: " + str(gmail)
    print "YAHOO: " + str(yahoo)
    print "LIVE: " + str(live)
    print "HOTMAIL: " + str(hotmail)
    print "AUDI.COM.MX: " + str(audi)
    print "VW: " + str(vw)
    print "OUTLOOK: " + str(outlook)
    print "TOTAL: " + str(outlook + gmail + yahoo + live + hotmail + audi + vw)
