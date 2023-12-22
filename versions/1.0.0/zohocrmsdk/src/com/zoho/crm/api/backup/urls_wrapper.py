try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
	from zohocrmsdk.src.com.zoho.crm.api.backup.response_handler import ResponseHandler
except Exception:
	from ..exception import SDKException
	from ..util import Constants
	from .response_handler import ResponseHandler


class UrlsWrapper(ResponseHandler):
	def __init__(self):
		"""Creates an instance of UrlsWrapper"""
		super().__init__()

		self.__urls = None
		self.__key_modified = dict()

	def get_urls(self):
		"""
		The method to get the urls

		Returns:
			Urls: An instance of Urls
		"""

		return self.__urls

	def set_urls(self, urls):
		"""
		The method to set the value to urls

		Parameters:
			urls (Urls) : An instance of Urls
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.backup.urls import Urls
		except Exception:
			from .urls import Urls

		if urls is not None and not isinstance(urls, Urls):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: urls EXPECTED TYPE: Urls', None, None)
		
		self.__urls = urls
		self.__key_modified['urls'] = 1

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
