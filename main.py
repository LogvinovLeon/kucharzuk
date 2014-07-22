import urllib2
import time
import subprocess

while (1):
    try:
        resp = urllib2.urlopen("http://www.czyjestjuzkucharzyk.pl")
        if resp.read().find("TAK") == -1:
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