try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class ReplacedValue(object):
	def __init__(self):
		"""Creates an instance of ReplacedValue"""

		self.__display_value = None
		self.__actual_value = None
		self.__key_modified = dict()

	def get_display_value(self):
		"""
		The method to get the display_value

		Returns:
			string: A string representing the display_value
		"""

		return self.__display_value

	def set_display_value(self, display_value):
		"""
		The method to set the value to display_value

		Parameters:
			display_value (string) : A string representing the display_value
		"""

		if display_value is not None and not isinstance(display_value, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: display_value EXPECTED TYPE: str', None, None)
		
		self.__display_value = display_value
		self.__key_modified['display_value'] = 1

	def get_actual_value(self):
		"""
		The method to get the actual_value

		Returns:
			string: A string representing the actual_value
		"""

		return self.__actual_value

	def set_actual_value(self, actual_value):
		"""
		The method to set the value to actual_value

		Parameters:
			actual_value (string) : A string representing the actual_value
		"""

		if actual_value is not None and not isinstance(actual_value, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: actual_value EXPECTED TYPE: str', None, None)
		
		self.__actual_value = actual_value
		self.__key_modified['actual_value'] = 1

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
