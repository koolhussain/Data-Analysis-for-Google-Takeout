import json
# import rhinoscriptsyntax as rs


with open('file.json', 'r') as json_data:
	data = json.load(json_data)
	json_data.close()
	print ("Timestamp: {}".format(data["creationTime"]["timestamp"]))
	print ("Title: {}".format(data["title"]))
	print ("Description: {}".format(data["description"]))
	print ("URL: {}".format(data["url"]))
	print ("Image Views: {}".format(data["imageViews"]))
	print ("Created: {}".format(data["creationTime"]["formatted"]))
	print ("Lattitude Position: {}".format(data["geoData"]["latitude"]))
	print ("Longitude Position: {}".format(data["geoData"]["longitude"]))
	print ("Alltitude: {}".format(data["geoData"]["altitude"]))
	print ("Created: {}".format(data["creationTime"]["formatted"].split(',')))
	print ("Created: {}".format(data["creationTime"]["formatted"].split(',')[0].split(' ')))
	print ("Date: {}".format(data["creationTime"]["formatted"].split(',')[0].split(' ')[1]))
	print ("Month: {}".format(data["creationTime"]["formatted"].split(',')[0].split(' ')[0]))
	print ("Year: {}".format(data["creationTime"]["formatted"].split(',')[1]))
	print ("Created: {}".format(data["creationTime"]["formatted"].split(',')[2]))
	if (data["description"] == ""):
		print("Description: {}".format("N/A"))