try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class ActionWrapper(object):
	def __init__(self):
		"""Creates an instance of ActionWrapper"""

		self.__custom_views = None
		self.__key_modified = dict()

	def get_custom_views(self):
		"""
		The method to get the custom_views

		Returns:
			list: An instance of list
		"""

		return self.__custom_views

	def set_custom_views(self, custom_views):
		"""
		The method to set the value to custom_views

		Parameters:
			custom_views (list) : An instance of list
		"""

		if custom_views is not None and not isinstance(custom_views, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: custom_views EXPECTED TYPE: list', None, None)
		
		self.__custom_views = custom_views
		self.__key_modified['custom_views'] = 1

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
