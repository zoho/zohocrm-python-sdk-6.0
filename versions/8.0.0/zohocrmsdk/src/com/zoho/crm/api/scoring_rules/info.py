try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Info(object):
	def __init__(self):
		"""Creates an instance of Info"""

		self.__call = None
		self.__per_page = None
		self.__next_page_token = None
		self.__count = None
		self.__page = None
		self.__previous_page_token = None
		self.__page_token_expiry = None
		self.__email = None
		self.__more_records = None
		self.__key_modified = dict()

	def get_call(self):
		"""
		The method to get the call

		Returns:
			bool: A bool representing the call
		"""

		return self.__call

	def set_call(self, call):
		"""
		The method to set the value to call

		Parameters:
			call (bool) : A bool representing the call
		"""

		if call is not None and not isinstance(call, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: call EXPECTED TYPE: bool', None, None)
		
		self.__call = call
		self.__key_modified['call'] = 1

	def get_per_page(self):
		"""
		The method to get the per_page

		Returns:
			int: An int representing the per_page
		"""

		return self.__per_page

	def set_per_page(self, per_page):
		"""
		The method to set the value to per_page

		Parameters:
			per_page (int) : An int representing the per_page
		"""

		if per_page is not None and not isinstance(per_page, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: per_page EXPECTED TYPE: int', None, None)
		
		self.__per_page = per_page
		self.__key_modified['per_page'] = 1

	def get_next_page_token(self):
		"""
		The method to get the next_page_token

		Returns:
			string: A string representing the next_page_token
		"""

		return self.__next_page_token

	def set_next_page_token(self, next_page_token):
		"""
		The method to set the value to next_page_token

		Parameters:
			next_page_token (string) : A string representing the next_page_token
		"""

		if next_page_token is not None and not isinstance(next_page_token, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: next_page_token EXPECTED TYPE: str', None, None)
		
		self.__next_page_token = next_page_token
		self.__key_modified['next_page_token'] = 1

	def get_count(self):
		"""
		The method to get the count

		Returns:
			int: An int representing the count
		"""

		return self.__count

	def set_count(self, count):
		"""
		The method to set the value to count

		Parameters:
			count (int) : An int representing the count
		"""

		if count is not None and not isinstance(count, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: count EXPECTED TYPE: int', None, None)
		
		self.__count = count
		self.__key_modified['count'] = 1

	def get_page(self):
		"""
		The method to get the page

		Returns:
			int: An int representing the page
		"""

		return self.__page

	def set_page(self, page):
		"""
		The method to set the value to page

		Parameters:
			page (int) : An int representing the page
		"""

		if page is not None and not isinstance(page, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: page EXPECTED TYPE: int', None, None)
		
		self.__page = page
		self.__key_modified['page'] = 1

	def get_previous_page_token(self):
		"""
		The method to get the previous_page_token

		Returns:
			string: A string representing the previous_page_token
		"""

		return self.__previous_page_token

	def set_previous_page_token(self, previous_page_token):
		"""
		The method to set the value to previous_page_token

		Parameters:
			previous_page_token (string) : A string representing the previous_page_token
		"""

		if previous_page_token is not None and not isinstance(previous_page_token, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: previous_page_token EXPECTED TYPE: str', None, None)
		
		self.__previous_page_token = previous_page_token
		self.__key_modified['previous_page_token'] = 1

	def get_page_token_expiry(self):
		"""
		The method to get the page_token_expiry

		Returns:
			datetime: An instance of datetime
		"""

		return self.__page_token_expiry

	def set_page_token_expiry(self, page_token_expiry):
		"""
		The method to set the value to page_token_expiry

		Parameters:
			page_token_expiry (datetime) : An instance of datetime
		"""

		from datetime import datetime

		if page_token_expiry is not None and not isinstance(page_token_expiry, datetime):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: page_token_expiry EXPECTED TYPE: datetime', None, None)
		
		self.__page_token_expiry = page_token_expiry
		self.__key_modified['page_token_expiry'] = 1

	def get_email(self):
		"""
		The method to get the email

		Returns:
			bool: A bool representing the email
		"""

		return self.__email

	def set_email(self, email):
		"""
		The method to set the value to email

		Parameters:
			email (bool) : A bool representing the email
		"""

		if email is not None and not isinstance(email, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: email EXPECTED TYPE: bool', None, None)
		
		self.__email = email
		self.__key_modified['email'] = 1

	def get_more_records(self):
		"""
		The method to get the more_records

		Returns:
			bool: A bool representing the more_records
		"""

		return self.__more_records

	def set_more_records(self, more_records):
		"""
		The method to set the value to more_records

		Parameters:
			more_records (bool) : A bool representing the more_records
		"""

		if more_records is not None and not isinstance(more_records, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: more_records EXPECTED TYPE: bool', None, None)
		
		self.__more_records = more_records
		self.__key_modified['more_records'] = 1

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
