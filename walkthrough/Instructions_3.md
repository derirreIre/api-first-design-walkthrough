# Step by step example of using API First Design Principles to spin up a hello world polyglot stack
# 3) Spin up a second service and using auto-generated client-side code 

## Steps:
1) Initially lets auto-generate our helloworld service
2) Updating endpoints and using OpenAPI templates
3) <b>Spin up a second service and using auto-generated client-side code</b> (we are here)
4) Switching tech stack, replacing an existing python-based service with a golang based service


### Adding a second microservice

Our _helloworld_ service is great, but what if we want to make it a bit fancier by adding the possibility to select your language of choice. This also gives us an excuse to spin up another microservice. We will spin up a _translation_ python-flask server and the corresponding client-side code that our first _helloworld_ service can use to interact with the _translation_ service.

### Generating the Translation Python-Flask server
As with the _helloworld_ service, the OpenAPI specs and template files can be found here: _openapi-specs/translate_

Open a new terminal and generate and run the server

Generate code with: 
```bash
openapi-generator-cli generate -i openapi-specs/translate/translate.yaml -g python-flask -o ./source_code/translate/python-flask -t openapi-specs/translate/templates/python-flask
```
Change the default port to 8081 (`source_code/translate/python-flask/openapi_server/__main__.py`, line 14) as the default port of 8080 is already in use by the _helloworld_ service. If you like you can add a _\_\_main\_\_.mustache_ template file to change the port everytime you generate the service (`https://github.com/OpenAPITools/openapi-generator/blob/master/modules/openapi-generator/src/main/resources/python-flask/__main__.mustache`)

Activate your python virtual environment if not already done. There is no need to create a second venv, we will use the same toolchain as with the _helloworld_ service.
```bash
source _venv/bin/activate  # source your virtual environment
```

Run your python flask server, navigate to `source_code/translate/python-flask` 
```bash
cd source_code/translate/python-flask
```
and run the following in your terminal:
```bash
python -m openapi_server
```
Navigate to the demo UI on your browser to test it out:
```http://127.0.0.1:8081/v1/ui/```

### Generating the translation service's client-side code
Another big efficiency booster when using API-First development, is that we can also generate code that a client can use to interact with a server (not just the server itself).

We will now auto-generate a python client module that the _helloworld_ service can import and use straight out of the box.

Generate translate client code:
```bash
openapi-generator generate -i openapi-specs/translate/translate.yaml -g python-legacy -o ./source_code/translate/python-client
```
There should now be a _README.md_ file (see: source_code/translate/python-client/README.md) which has some sample code to illustrate how to use the code. 

Rather than copy and paste the client-side code/module somewhere, we will simply add it to our existing python toolchain/virtual_env. Source the auto-generated python module:
```bash
pip install source_code/translate/python-client
# you may need to adjust the relative path to source_code/translate/python-client
```
If you now run `pip freeze` in your terminal where your virtual environment is active, you will get a list of module, and in there should be the auto-generated _openapi-client==1.0.0_

Now that the client-side code is available to your _helloworld_ service, lets use it to get our two services communicating. 

### Using the translation service's client-side code
Back in the _helloworld_ service directory, open up the file containing our business logic: [source_code/hello_world/python_flask_server/openapi_server/controllers/default_controller_business_logic.py](./../source_code/hello_world/python_flask_server/openapi_server/controllers/default_controller_business_logic.py). We will make two changes to the file.

1) Uncomment lines 10 to 31. This is function that will use the client-side code to talk to the translate service. This function is basically the example code from the above mentioned _README.md_ file, using the parameters of the _translate_ service.

2) Uncomment lines 55 to 56, and delete lines 53 and 54, so that we are returning the function that communicates with the translate service. 

The file should look something like this:
```python

from openapi_server.models.inline_response200 import InlineResponse200  # noqa: E501



import time
from pprint import pprint


### This function and import will be used after ###
### the translation service is up and running,  ###
### and client-side is part of the python venv.  ###
import openapi_client
from openapi_client.rest import ApiException

def language_endpoint_client(language, text="hello world"):
    configuration = openapi_client.Configuration(
        host = "http://127.0.0.1:8081/v1"
    )

    # Enter a context with an instance of the API client
    with openapi_client.ApiClient(configuration) as api_client:
        # Create an instance of the API class
        api_instance = openapi_client.DefaultApi(api_client)

        try:
            # translate hello world endpoint
            api_response = api_instance.translate_get(language=language, text=text)
            return InlineResponse200(language=api_response.language, helloworld=api_response.text)
        except ApiException as e:
            print("Exception when calling DefaultApi->translate_get: %s\n" % e)


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
        # print("language: tbd, helloworld: hello world")
        # return InlineResponse200(language='not yet implemented', helloworld='hello world')
        ### after translation service is up and running ###
        return language_endpoint_client(language=language)

```

Now that the client-side code has been added to the _helloworld_ service, go the the terminal, stop it running (ctrl+c), and restart it 
```bash
python -m openapi_server
```

Now test your _helloworld_ service using the following curl commands

```bash
# default
curl http://127.0.0.1:8080/v1/helloworld
# returns:
# {
#   "helloworld": "hello world",
#   "language": "(default)"
# }

# english
curl -X GET "http://127.0.0.1:8080/v1/helloworld?language=english" -H  "accept: application/json"
# returns
# {
#   "helloworld": "hello world",
#   "language": "english"
# }

# bavarian
curl -X GET "http://127.0.0.1:8080/v1/helloworld?language=bavarian" -H  "accept: application/json"
# returns
# {
#   "helloworld": "servus welt",
#   "language": "bavarian"
# }
```
If you check the terminals running _helloworld_ and _translate_ services, you should also see some debug prints to let you know what is going on. 

Right now only 'english' and 'bavarian' are supported. You can add more languages/functionality etc in the translate service's [default_controller_business_logic.py](source_code/translate/python-flask/openapi_server/controllers/default_controller_business_logic.py) file.
