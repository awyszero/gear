import sqlite3

''' with this method we get data from data base'''
def getdate():
    s = sqlite3.connect("drug.db")    # here we connect to data base
    s.row_factory =sqlite3.Row    # we wont to get data from data base in raw formate enstateof tapule formate
    get = s.execute("SELECT * FROM info")    # here we execute data base command to get all data in the date base that we have
    for t in get:
        print ("drug name: {} drug class: {}".format(t["Name"],t["class"]))    # here we print the information that we get from database

''' this method if for enter data in the database of us'''
def enterdata(n,c):
    s =sqlite3.connect("drug.db")
    s.row_factory =sqlite3.Row
    s.execute("CREATE TABLE IF NOT EXISTS info(Name txt, class txt)")    # database command to create table if not existed and we have 2 column
    s.execute("INSERT INTO info(Name,class) VALUES (?,?)",(n,c))     # database command to insert the date that we get from the user
    s.commit()      # database command to save the data that we have entered now


''' here simp;e function to delate data from the database'''
def dealetdata():
    s =sqlite3.connect("drug.db")
    s.row_factory=sqlite3.Row
    s.execute("DELETE FROM info")   # database command to delate from date base
    s.commit()