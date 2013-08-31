import time
import httplib
import os
import urllib
import urllib2
files = os.listdir(os.curdir)
lasteng = ""
for f in files:
    if f.endswith("csv"):
        cla = f[0:f.find(".csv")]
        print cla
        os.system("mkdir -p \""+cla+"\"")
        with open(f, "r") as csvFile:
            while True:
            	rline = csvFile.readline()
            	if rline == '':
            		break
            	word = rline.split("#")[0].strip()
                if word == lasteng:
            	    print word + " same"
                    continue
                else:
                    print word
                    lasteng = word
            	httpServ = httplib.HTTPConnection("translate.google.cn", 80)
            	httpServ.connect()
            	requestStr = "/translate_tts?ie=UTF-8&q="+word.replace(" ", "%20")+"&tl=en&total=1&idx=0&textlen="+str(len(word))+"&prev=input"
                print requestStr
            	httpServ.request('GET', requestStr)
            #	httpServ.putheader("User-Agent", r"Mozilla/5.0 (MSIE 9.0; Windows NT 6.1; Trident/5.0)");
            	response = httpServ.getresponse()
            	if response.status == httplib.OK:
            		fileStr = response.read()
            		file = open(cla+"/"+word+".mp3", 'wb')
            		file.write(fileStr)
            		time.sleep(0.1)
            	else:
            		if response.status == 302:
            			print response.getheader("Location")
            		exit()
            	httpServ.close()
