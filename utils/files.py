import os, shutil

data_path = "./Dataset/"

def remove(file_path):
	"""remove all file without `.wav` in the pathway"""
	for root, dirs, files in os.walk(file_path):
		for item in files:
			if not item.endswith('.wav'):
				try:
					print("Delete file: ", os.path.join(root, item))
					os.remove(os.path.join(root, item))
				except:
					continue

def rename(file_path):
	"""rename the file with the same format to avoid the same-name files"""
	for root, dirs, files in os.walk(file_path):
		for item in files:
			if item.endswith('.wav'):
				people_name = root.split('/')[-2]
				emotion_name = root.split('/')[-1]
				item_name = item[:-4] # without '.wav'
				old_path = os.path.join(root, item)
				new_path = os.path.join(root, item_name + '-' + emotion_name + '-'+ people_name + '.wav')
				try:
					os.rename(old_path, new_path)
					print('converting ', old_path, ' to ', new_path)
				except:
					continue

def move(file_path):
	"""cateragy the file by the feeling and move to the correspond folder"""
	for root, dirs, files in os.walk(file_path):
		for item in files:
			if item.endswith('.wav'):
				emotion_name = root.split('/')[-1]
				old_path = os.path.join(root, item)
				new_path = os.path.join(file_path, emotion_name, item)
				try:
					shutil.move(old_path, new_path)
					print("Move ", old_path, " to ", new_path)
				except:
					continue
