#!/usr/bin/env python3

# data.py - script used to produce database results over HTTP for simple sqlite3 database

import cgi
import sqlite3

conn = sqlite3.connect('/etc/httpd/db/clients.db')
curs = conn.cursor()

print("Content-type:text/plain\n\n")

form = cgi.FieldStorage()
querystring = form.getvalue("querystring")
if querystring != None:
    queryval = "%" + querystring + "%"
    select = "SELECT * FROM clients WHERE name LIKE '" + queryval + "'"
else:
    select = "SELECT * FROM clients"

for row in curs.execute(select):
    if len(row) == 4:
        for item in row:
            print(item,'|')
        print("#")

conn.close()
