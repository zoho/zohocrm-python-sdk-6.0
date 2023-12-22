try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class FileDetails(object):
	def __init__(self):
		"""Creates an instance of FileDetails"""

		self.__file_name__s = None
		self.__size__s = None
		self.__id = None
		self.__file_id__s = None
		self.__delete = None
		self.__key_modified = dict()

	def get_file_name__s(self):
		"""
		The method to get the file_name__s

		Returns:
			string: A string representing the file_name__s
		"""

		return self.__file_name__s

	def set_file_name__s(self, file_name__s):
		"""
		The method to set the value to file_name__s

		Parameters:
			file_name__s (string) : A string representing the file_name__s
		"""

		if file_name__s is not None and not isinstance(file_name__s, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: file_name__s EXPECTED TYPE: str', None, None)
		
		self.__file_name__s = file_name__s
		self.__key_modified['File_Name__s'] = 1

	def get_size__s(self):
		"""
		The method to get the size__s

		Returns:
			string: A string representing the size__s
		"""

		return self.__size__s

	def set_size__s(self, size__s):
		"""
		The method to set the value to size__s

		Parameters:
			size__s (string) : A string representing the size__s
		"""

		if size__s is not None and not isinstance(size__s, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: size__s EXPECTED TYPE: str', None, None)
		
		self.__size__s = size__s
		self.__key_modified['Size__s'] = 1

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

	def get_file_id__s(self):
		"""
		The method to get the file_id__s

		Returns:
			string: A string representing the file_id__s
		"""

		return self.__file_id__s

	def set_file_id__s(self, file_id__s):
		"""
		The method to set the value to file_id__s

		Parameters:
			file_id__s (string) : A string representing the file_id__s
		"""

		if file_id__s is not None and not isinstance(file_id__s, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: file_id__s EXPECTED TYPE: str', None, None)
		
		self.__file_id__s = file_id__s
		self.__key_modified['File_Id__s'] = 1

	def get_delete(self):
		"""
		The method to get the delete

		Returns:
			string: A string representing the delete
		"""

		return self.__delete

	def set_delete(self, delete):
		"""
		The method to set the value to delete

		Parameters:
			delete (string) : A string representing the delete
		"""

		if delete is not None and not isinstance(delete, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: delete EXPECTED TYPE: str', None, None)
		
		self.__delete = delete
		self.__key_modified['_delete'] = 1

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
