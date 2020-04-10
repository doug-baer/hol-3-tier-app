#!/usr/bin/env python3

# app.py - script used to process database results for presentation

import os
import cgi
import requests

webservers = {
  '192.168.120.30': 'web-01a',
  '192.168.120.31': 'web-02a',
  '192.168.120.32': 'web-03a'
 }

print("Content-type:text/html\n\n")
print("<head><title>Customer Database</title></head>\n")
print("<body>\n")
print("<h1>Customer Database Access</h1>\n")

remote = os.getenv("REMOTE_ADDR")
form = cgi.FieldStorage()
querystring = form.getvalue("querystring")

if remote in webservers:
    accessName = webservers[remote]
else:
    accessName = remote

print("Accessed via:", accessName, "\n<p>")

if querystring != None:
    url = 'http://db-01a:3306/cgi-bin/data.py?querystring=' + querystring
else:
    url = 'http://db-01a:3306/cgi-bin/data.py'
    querystring = ""

r = requests.get(url)

print('<form action="/cgi-bin/app.py">')
print(' Name Filter (blank for all records):')
print(' <input type="text" name="querystring" value="'+querystring+'">')
print(' <input type="submit" value="Apply">')
print('</form>')

print("\n<table border=1 bordercolor=black cellpadding=5 cellspacing=0>")

print("\n<th>Rank</th><th>Name</th><th>Universe</th><th>Revenue</th>")

# deal with the data coming across the wire
a = r.text.split("|\n#")
for row in a:
    if len(row) != 1:
        print("<tr>")
        splitrow = row.split("|")
        for item in splitrow:
            if item != None:
                print("<td>",item,"</td>")
        print("</tr>\n")
    print("</body></html>\n")
