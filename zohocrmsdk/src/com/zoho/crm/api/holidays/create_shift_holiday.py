try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
	from zohocrmsdk.src.com.zoho.crm.api.holidays.body_wrapper import BodyWrapper
except Exception:
	from ..exception import SDKException
	from ..util import Constants
	from .body_wrapper import BodyWrapper


class CreateShiftHoliday(BodyWrapper):
	def __init__(self):
		"""Creates an instance of CreateShiftHoliday"""
		super().__init__()

		self.__holidays = None
		self.__key_modified = dict()

	def get_holidays(self):
		"""
		The method to get the holidays

		Returns:
			list: An instance of list
		"""

		return self.__holidays

	def set_holidays(self, holidays):
		"""
		The method to set the value to holidays

		Parameters:
			holidays (list) : An instance of list
		"""

		if holidays is not None and not isinstance(holidays, list):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: holidays EXPECTED TYPE: list', None, None)
		
		self.__holidays = holidays
		self.__key_modified['holidays'] = 1

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
