
class APIResponse(object):

    """
    This class is the common API response object.
    """

    def __init__(self, headers, status_code, object):

        """
        Creates an APIResponse class instance with the specified parameters.

        Parameters:
             headers (dict) : A dict containing the API response headers.
             status_code (int) : An integer containing the API response HTTP status code.
             object (object) : An object containing the API response class instance.
        """

        self.__headers = headers
        self.__status_code = status_code
        self.__object = object

    def get_headers(self):

        """
        This is a getter method to get API response headers.

        Returns:
            dict: A dict representing the API response headers.
        """

        return self.__headers

    def get_status_code(self):

        """
        This is a getter method to get the API response HTTP status code.

        Returns:
            int: An integer representing the API response HTTP status code.
        """

        return self.__status_code

    def get_object(self):

        """
        This method to get an API response class instance.

        Returns:
            object: An object containing the API response class instance.
        """

        return self.__object
