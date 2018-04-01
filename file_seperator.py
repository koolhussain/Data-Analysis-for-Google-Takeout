import os
import shutil

fullpath = os.path.join
json_dirt = "./Json"
photos_dirt = "./Photos"
start_dirt = "./takeout-20180323T190627Z-001"
other_dirt = "./Other"

dir_table = {'jpg': './Photos','jpeg': './Photos','png': './Photos','mp4': './Photos','json': './Json'}

def get_extension(filename):
	return filename[filename.rfind('.')+1:]


for dirname, dirnames, filenames in os.walk(start_dirt):
	for filename in filenames:
		file = fullpath(dirname, filename)
		extension = get_extension(filename)
		if (extension in dir_table):
			shutil.copy(file, fullpath(dir_table[extension], filename))
		else:
			shutil.copy(file, fullpath(other_dirt, filename))

