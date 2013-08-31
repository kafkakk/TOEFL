import urllib
import urllib2
import os

def speech(cla, eng):
    url = "http://192.20.225.36/tts/cgi-bin/nph-nvdemo"
    values = {
            "voice":"lauren",
            "txt":eng,
            "speakButton":"SPEAK"
        }
    data = urllib.urlencode(values)
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)
    the_wav= response.read()
    with open(cla+"/"+eng+".wav", "wb") as f:
        f.write(the_wav)

files = os.listdir(os.curdir)
lasteng = ""
for f in files:
    if f.endswith("csv"):
        cla = f[0:f.find(".csv")]
        print cla
        os.system("mkdir -p "+cla)
        with open(f, "r") as csvFile:
            for line in csvFile:
                eng = line.split(",")[0].strip()
                if eng == lasteng:
                    print eng+" same"
                else:
                    print eng
                    speech(cla, eng)
                    lasteng = eng

