import datetime


def timeToTimestamp(time):
    d = datetime.datetime.strptime(time, "%H:%M:%S").replace(year=1970) + datetime.timedelta(hours=1)
    return d.strftime("%s") + "000"


def dateToTimestamp(date):
    d = datetime.datetime.strptime(date, "%x") + datetime.timedelta(hours=2)
    return d.strftime("%s") + "000"


f = open("times.dat", "r")
lines = f.readlines()
data = []
for line in lines:
    parts = line.split(' ')
    date = parts[0]
    time = parts[1]
    time = time.strip('\n')
    y = timeToTimestamp(time)
    x = dateToTimestamp(date)
    data.append("\t" * 6 + "{x: " + str(x) + ", y: " + str(y) + ", name: \"" + time + "\"}")
data = ',\n'.join(data)
tmp = open("template.html")
HTML = str(open("template.html").read())
HTML = HTML.replace("${data}", data)
open("index.html", "w").write(HTML)
