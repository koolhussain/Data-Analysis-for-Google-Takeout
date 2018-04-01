import json
import os
import sqlite3

fullpath = os.path.join
json_dir = './Json'

def create_connection(db_file):
	try:
		conn = sqlite3.connect(db_file)
		return conn
	except Error as e:
		print('Connection Error:', str(e))
	return None

def create_table(conn):
	try:
		conn.execute('''CREATE TABLE IF NOT EXISTS photos(row_id INT PRIMARY KEY, time_stamp TEXT, title TEXT, description TEXT,
			url TEXT, image_views TEXT, creation_date TEXT, creation_month TEXT, creation_year TEXT, creation_time TEXT,
			latitude INT, longitude INT, altitude INT)''')

	except Exception as e:
		print('Create Table Error', str(e))

def create_entry(conn, entry):
	sql = ''' INSERT INTO photos(row_id, time_stamp, title, description, url, image_views, creation_date, creation_month,
	 creation_year, creation_time, latitude, longitude, altitude) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?) '''
	cur = conn.cursor()
	cur.execute(sql, entry)
	return cur.lastrowid


def main():	
	database = fullpath(os.getcwd(), 'google_photos.db')	
	conn = create_connection(database)
	with conn:
		create_table(conn)
		row_counter = 0
		for filenames in os.walk(json_dir):
			for filename in filenames[2]:
				print(filename)
				row_counter = row_counter + 1
				try:
					with open(fullpath(json_dir, filename), 'r') as json_data:
						data = json.load(json_data)
						row_id = row_counter
						time_stamp = data["creationTime"]["timestamp"]
						title = data["title"]
						description = data["description"]
						url = data["url"]
						image_views = data["imageViews"]
						creation_date = data["creationTime"]["formatted"].split(',')[0].split(' ')[1]
						creation_month = data["creationTime"]["formatted"].split(',')[0].split(' ')[0]
						creation_year = data["creationTime"]["formatted"].split(',')[1]
						creation_time = data["creationTime"]["formatted"].split(',')[2]
						latitude = data["geoData"]["latitude"]
						longitude = data["geoData"]["longitude"]
						altitude = data["geoData"]["altitude"]
						task = (row_id, time_stamp, title, description, url, image_views, creation_date,
							creation_month, creation_year, creation_time, latitude, longitude, altitude,)
						entry_id = create_entry(conn, task)
						json_data.close()	
				except Exception as e:
					print('Main',str(e))
					# print(filename)
main()

