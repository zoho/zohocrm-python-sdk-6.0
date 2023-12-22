try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import APIResponse, Choice, CommonAPIHandler, Constants
	from zohocrmsdk.src.com.zoho.crm.api.param import Param
except Exception:
	from ..exception import SDKException
	from ..util import APIResponse, Choice, CommonAPIHandler, Constants
	from ..param import Param


class EmailRelatedRecordsOperations(object):
	def __init__(self, record_id, module_name):
		"""
		Creates an instance of EmailRelatedRecordsOperations with the given parameters

		Parameters:
			record_id (int) : An int representing the record_id
			module_name (string) : A string representing the module_name
		"""

		if not isinstance(record_id, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: record_id EXPECTED TYPE: int', None, None)
		
		if not isinstance(module_name, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: module_name EXPECTED TYPE: str', None, None)
		
		self.__record_id = record_id
		self.__module_name = module_name


	def get_emails_related_records(self, param_instance=None):
		"""
		The method to get emails related records

		Parameters:
			param_instance (ParameterMap) : An instance of ParameterMap

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api import ParameterMap
		except Exception:
			from ..parameter_map import ParameterMap

		if param_instance is not None and not isinstance(param_instance, ParameterMap):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: param_instance EXPECTED TYPE: ParameterMap', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v6/'
		api_path = api_path + str(self.__module_name)
		api_path = api_path + '/'
		api_path = api_path + str(self.__record_id)
		api_path = api_path + '/Emails'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		handler_instance.set_param(param_instance)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.email_related_records.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')

	def get_emails_related_record(self, message_id):
		"""
		The method to get emails related record

		Parameters:
			message_id (string) : A string representing the message_id

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		if not isinstance(message_id, str):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: message_id EXPECTED TYPE: str', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v6/'
		api_path = api_path + str(self.__module_name)
		api_path = api_path + '/'
		api_path = api_path + str(self.__record_id)
		api_path = api_path + '/Emails/'
		api_path = api_path + str(message_id)
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_GET)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_READ)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.email_related_records.response_handler import ResponseHandler
		except Exception:
			from .response_handler import ResponseHandler
		return handler_instance.api_call(ResponseHandler.__module__, 'application/json')


class GetEmailsRelatedRecordsParam(object):
	type = Param('type', 'com.zoho.crm.api.EmailRelatedRecords.GetEmailsRelatedRecordsParam')
	filter = Param('filter', 'com.zoho.crm.api.EmailRelatedRecords.GetEmailsRelatedRecordsParam')
	index = Param('index', 'com.zoho.crm.api.EmailRelatedRecords.GetEmailsRelatedRecordsParam')
	owner_id = Param('owner_id', 'com.zoho.crm.api.EmailRelatedRecords.GetEmailsRelatedRecordsParam')
