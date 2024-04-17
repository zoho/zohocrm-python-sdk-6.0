try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Owner(object):
	def __init__(self):
		"""Creates an instance of Owner"""

		self.__name = None
		self.__id = None
		self.__last_name = None
		self.__first_name = None
		self.__key_modified = dict()

	def get_name(self):
		"""
		The method to get the name

		Returns:
			string: A string representing the name
		"""

		return self.__name

	def set_name(self, name):
		"""
		The method to set the value to name

		Parameters:
			name (string) : A string representing the name
		"""

		if name is not None and not isinstance(name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: name EXPECTED TYPE: str', None, None)
		
		self.__name = name
		self.__key_modified['name'] = 1

	def get_id(self):
		"""
		The method to get the id

		Returns:
			int: An int representing the id
		"""

		return self.__id

	def set_id(self, id):
		"""
		The method to set the value to id

		Parameters:
			id (int) : An int representing the id
		"""

		if id is not None and not isinstance(id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: id EXPECTED TYPE: int', None, None)
		
		self.__id = id
		self.__key_modified['id'] = 1

	def get_last_name(self):
		"""
		The method to get the last_name

		Returns:
			string: A string representing the last_name
		"""

		return self.__last_name

	def set_last_name(self, last_name):
		"""
		The method to set the value to last_name

		Parameters:
			last_name (string) : A string representing the last_name
		"""

		if last_name is not None and not isinstance(last_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: last_name EXPECTED TYPE: str', None, None)
		
		self.__last_name = last_name
		self.__key_modified['last_name'] = 1

	def get_first_name(self):
		"""
		The method to get the first_name

		Returns:
			string: A string representing the first_name
		"""

		return self.__first_name

	def set_first_name(self, first_name):
		"""
		The method to set the value to first_name

		Parameters:
			first_name (string) : A string representing the first_name
		"""

		if first_name is not None and not isinstance(first_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: first_name EXPECTED TYPE: str', None, None)
		
		self.__first_name = first_name
		self.__key_modified['first_name'] = 1

	def is_key_modified(self, key):
		"""
		The method to check if the user has modified the given key

		Parameters:
			key (string) : A string representing the key

		Returns:
			int: An int representing the modification
		"""

		if key is not None and not isinstance(key, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: key EXPECTED TYPE: str', None, None)
		
		if key in self.__key_modified:
			return self.__key_modified.get(key)
		
		return None

	def set_key_modified(self, key, modification):
		"""
		The method to mark the given key as modified

		Parameters:
			key (string) : A string representing the key
			modification (int) : An int representing the modification
		"""

		if key is not None and not isinstance(key, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: key EXPECTED TYPE: str', None, None)
		
		if modification is not None and not isinstance(modification, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: modification EXPECTED TYPE: int', None, None)
		
		self.__key_modified[key] = modification
