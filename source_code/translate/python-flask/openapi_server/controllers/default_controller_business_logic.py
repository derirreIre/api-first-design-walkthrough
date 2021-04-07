
from openapi_server.models.inline_response200 import InlineResponse200  # noqa: E501


def translate_get(language=None, text=None):  # noqa: E501
    """translate hello world endpoint

    returns hello world in a language # noqa: E501

    :param language: hello world in your language of choice
    :type language: str
    :param text: hello world in your language of choice
    :type text: str

    :rtype: InlineResponse200
    """
    print("debug - language: " + language + " text: " + text)
    if language == 'bavarian' or language == 'Bavarian':
        return InlineResponse200(language=language, text='servus welt')
    else:
        return InlineResponse200(language='not yet implemented, using default(english)', text='hello world')
