try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import Constants
except Exception:
	from ..exception import SDKException
	from ..util import Constants


class Multiselectlookup(object):
	def __init__(self):
		"""Creates an instance of Multiselectlookup"""

		self.__display_label = None
		self.__linking_module = None
		self.__connected_module = None
		self.__lookup_apiname = None
		self.__api_name = None
		self.__connectedfield_apiname = None
		self.__connectedlookup_apiname = None
		self.__id = None
		self.__record_access = None
		self.__key_modified = dict()

	def get_display_label(self):
		"""
		The method to get the display_label

		Returns:
			string: A string representing the display_label
		"""

		return self.__display_label

	def set_display_label(self, display_label):
		"""
		The method to set the value to display_label

		Parameters:
			display_label (string) : A string representing the display_label
		"""

		if display_label is not None and not isinstance(display_label, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: display_label EXPECTED TYPE: str', None, None)
		
		self.__display_label = display_label
		self.__key_modified['display_label'] = 1

	def get_linking_module(self):
		"""
		The method to get the linking_module

		Returns:
			MinifiedModule: An instance of MinifiedModule
		"""

		return self.__linking_module

	def set_linking_module(self, linking_module):
		"""
		The method to set the value to linking_module

		Parameters:
			linking_module (MinifiedModule) : An instance of MinifiedModule
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.modules import MinifiedModule
		except Exception:
			from ..modules import MinifiedModule

		if linking_module is not None and not isinstance(linking_module, MinifiedModule):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: linking_module EXPECTED TYPE: MinifiedModule', None, None)
		
		self.__linking_module = linking_module
		self.__key_modified['linking_module'] = 1

	def get_connected_module(self):
		"""
		The method to get the connected_module

		Returns:
			MinifiedModule: An instance of MinifiedModule
		"""

		return self.__connected_module

	def set_connected_module(self, connected_module):
		"""
		The method to set the value to connected_module

		Parameters:
			connected_module (MinifiedModule) : An instance of MinifiedModule
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.modules import MinifiedModule
		except Exception:
			from ..modules import MinifiedModule

		if connected_module is not None and not isinstance(connected_module, MinifiedModule):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: connected_module EXPECTED TYPE: MinifiedModule', None, None)
		
		self.__connected_module = connected_module
		self.__key_modified['connected_module'] = 1

	def get_lookup_apiname(self):
		"""
		The method to get the lookup_apiname

		Returns:
			string: A string representing the lookup_apiname
		"""

		return self.__lookup_apiname

	def set_lookup_apiname(self, lookup_apiname):
		"""
		The method to set the value to lookup_apiname

		Parameters:
			lookup_apiname (string) : A string representing the lookup_apiname
		"""

		if lookup_apiname is not None and not isinstance(lookup_apiname, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: lookup_apiname EXPECTED TYPE: str', None, None)
		
		self.__lookup_apiname = lookup_apiname
		self.__key_modified['lookup_apiname'] = 1

	def get_api_name(self):
		"""
		The method to get the api_name

		Returns:
			string: A string representing the api_name
		"""

		return self.__api_name

	def set_api_name(self, api_name):
		"""
		The method to set the value to api_name

		Parameters:
			api_name (string) : A string representing the api_name
		"""

		if api_name is not None and not isinstance(api_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: api_name EXPECTED TYPE: str', None, None)
		
		self.__api_name = api_name
		self.__key_modified['api_name'] = 1

	def get_connectedfield_apiname(self):
		"""
		The method to get the connectedfield_apiname

		Returns:
			string: A string representing the connectedfield_apiname
		"""

		return self.__connectedfield_apiname

	def set_connectedfield_apiname(self, connectedfield_apiname):
		"""
		The method to set the value to connectedfield_apiname

		Parameters:
			connectedfield_apiname (string) : A string representing the connectedfield_apiname
		"""

		if connectedfield_apiname is not None and not isinstance(connectedfield_apiname, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: connectedfield_apiname EXPECTED TYPE: str', None, None)
		
		self.__connectedfield_apiname = connectedfield_apiname
		self.__key_modified['connectedfield_apiname'] = 1

	def get_connectedlookup_apiname(self):
		"""
		The method to get the connectedlookup_apiname

		Returns:
			string: A string representing the connectedlookup_apiname
		"""

		return self.__connectedlookup_apiname

	def set_connectedlookup_apiname(self, connectedlookup_apiname):
		"""
		The method to set the value to connectedlookup_apiname

		Parameters:
			connectedlookup_apiname (string) : A string representing the connectedlookup_apiname
		"""

		if connectedlookup_apiname is not None and not isinstance(connectedlookup_apiname, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: connectedlookup_apiname EXPECTED TYPE: str', None, None)
		
		self.__connectedlookup_apiname = connectedlookup_apiname
		self.__key_modified['connectedlookup_apiname'] = 1

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

	def get_record_access(self):
		"""
		The method to get the record_access

		Returns:
			bool: A bool representing the record_access
		"""

		return self.__record_access

	def set_record_access(self, record_access):
		"""
		The method to set the value to record_access

		Parameters:
			record_access (bool) : A bool representing the record_access
		"""

		if record_access is not None and not isinstance(record_access, bool):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: record_access EXPECTED TYPE: bool', None, None)
		
		self.__record_access = record_access
		self.__key_modified['record_access'] = 1

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
