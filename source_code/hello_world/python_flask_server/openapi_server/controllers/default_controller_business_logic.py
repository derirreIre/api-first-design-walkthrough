
from openapi_server.models.inline_response200 import InlineResponse200  # noqa: E501



import time
from pprint import pprint


# ### This function and import will be used after ###
# ### the translation service is up and running,  ###
# ### and client-side is part of the python venv.  ###
# import openapi_client
# from openapi_client.rest import ApiException

# def language_endpoint_client(language, text="hello world"):
#     configuration = openapi_client.Configuration(
#         host = "http://127.0.0.1:8081/v1"
#     )

#     # Enter a context with an instance of the API client
#     with openapi_client.ApiClient(configuration) as api_client:
#         # Create an instance of the API class
#         api_instance = openapi_client.DefaultApi(api_client)

#         try:
#             # translate hello world endpoint
#             api_response = api_instance.translate_get(language=language, text=text)
#             return InlineResponse200(language=api_response.language, helloworld=api_response.text)
#         except ApiException as e:
#             print("Exception when calling DefaultApi->translate_get: %s\n" % e)


def helloworld_get(language=None):  # noqa: E501
    """test hello world endpoint

    returns hello world # noqa: E501

    :param language: hello world in your language of choice
    :type language: str

    :rtype: InlineResponse200
    """

    if language is None or language == "":
        print("language: default, helloworld: hello world")
        return InlineResponse200(language='(default)', helloworld='hello world')
    elif language == "english" or language == "English":
        print("language: english, helloworld: hello world")
        return InlineResponse200(language='english', helloworld='hello world')
    else:
        # ### before translation service is up and running ###
        print("language: tbd, helloworld: hello world")
        return InlineResponse200(language='not yet implemented', helloworld='hello world')
        # ### after translation service is up and running ###
        # return language_endpoint_client(language=language)


        
