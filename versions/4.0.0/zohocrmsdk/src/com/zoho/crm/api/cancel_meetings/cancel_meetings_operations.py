try:
	from zohocrmsdk.src.com.zoho.crm.api.exception import SDKException
	from zohocrmsdk.src.com.zoho.crm.api.util import APIResponse, CommonAPIHandler, Constants
except Exception:
	from ..exception import SDKException
	from ..util import APIResponse, CommonAPIHandler, Constants


class CancelMeetingsOperations(object):
	def __init__(self, event):
		"""
		Creates an instance of CancelMeetingsOperations with the given parameters

		Parameters:
			event (int) : An int representing the event
		"""

		if not isinstance(event, int):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: event EXPECTED TYPE: int', None, None)
		
		self.__event = event


	def cancel_meetings(self, request):
		"""
		The method to cancel meetings

		Parameters:
			request (BodyWrapper) : An instance of BodyWrapper

		Returns:
			APIResponse: An instance of APIResponse

		Raises:
			SDKException
		"""

		try:
			from zohocrmsdk.src.com.zoho.crm.api.cancel_meetings.body_wrapper import BodyWrapper
		except Exception:
			from .body_wrapper import BodyWrapper

		if request is not None and not isinstance(request, BodyWrapper):
			raise SDKException(Constants.DATA_TYPE_ERROR, 'KEY: request EXPECTED TYPE: BodyWrapper', None, None)
		
		handler_instance = CommonAPIHandler()
		api_path = ''
		api_path = api_path + '/crm/v6/Events/'
		api_path = api_path + str(self.__event)
		api_path = api_path + '/actions/cancel'
		handler_instance.set_api_path(api_path)
		handler_instance.set_http_method(Constants.REQUEST_METHOD_POST)
		handler_instance.set_category_method(Constants.REQUEST_CATEGORY_ACTION)
		handler_instance.set_content_type('application/json')
		handler_instance.set_request(request)
		try:
			from zohocrmsdk.src.com.zoho.crm.api.cancel_meetings.action_handler import ActionHandler
		except Exception:
			from .action_handler import ActionHandler
		return handler_instance.api_call(ActionHandler.__module__, 'application/json')
