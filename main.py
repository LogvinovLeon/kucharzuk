import urllib2
import json
import time
import subprocess

while (1):
    try:
        resp = urllib2.urlopen('http://www.czyjestjuzkucharzyk.pl/api.json')
        data = json.loads(resp.read())
        if not data['arrived']:
            print time.strftime("%H:%M:%S") + " : NO"
        else:
            print "YES"
            subprocess.Popen(['notify-send', "Kucharzyk"])
            with open("times.dat", "a") as myfile:
                myfile.write(time.strftime("%D %H:%M:%S\n"))
            execfile("generateHTML.py")
            break
        time.sleep(1)
    except:
        pass
