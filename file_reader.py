import json


class FileReader(object):
	
	def __init__(self, folder, file_name):
		self.folder =  folder
		self.file_name = file_name

	def get_json_attribute(self, data, attribute, default_value):
		return data.get(attribute) or default_value

	def read_json_from_file(self):
		file_path = folder + '/' + file_name
		
		data_raw = '{}'
		with open(file_path) as json_file:  
			data_raw = json.load(json_file)

		return data_raw


class UserFileReader(FileReader):

	def __init__(self, folder, file_name):
		super(UserFileReader, self).__init__(folder, file_name)

	def get_users(self, fields):
		file_path = folder + '/' + file_name
		
		data_raw = '{}'
		with open(file_path) as json_file:  
			data_raw = json.load(json_file)

		list_users = self.get_json_attribute(data_raw, 'data', [])
		result = []

		for user_item in list_users:
			is_lacked_field = False
			for field in fields:
				is_lacked_field = is_lacked_field or user_item.get(field)
			if is_lacked_field:
				continue
			result.append(user_item)

		return result