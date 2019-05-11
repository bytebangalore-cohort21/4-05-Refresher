# model - The file where all the database and data calls are made.
import sqlite3

election_dates = ['11 April', '18 April', '23 April', '29 April', '6 May', '12 May', '19 May']

def getdata_totalseats(state):
	conn = sqlite3.connect('election.db')
	c = conn.cursor()
	c.execute("select * from election where state = '%s'"% state)
	data = c.fetchone()
	return data,election_dates

