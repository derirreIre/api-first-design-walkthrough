# Step by step example of using API First Design Principles to spin up a hello world polyglot stack 
# 2) Updating endpoints and using OpenAPI templates

## Steps:
1) Initially lets auto-generate our helloworld service
2) <b>Updating endpoints and using OpenAPI templates</b> (we are here)
3) Spin up a second service and using auto-generated client-side code
4) Switching tech stack, replacing an existing python-based service with a golang based service


### Adding some business logic

  Lets get to work adding some business logic. Our auto-generated function `source_code/hello_world/python_flask_server/openapi_server/controllers/default_controller.py` seems like the logic place to put our own code. However, each time we re-generate the server using the openapi-generator this file will be overwritten. So lets put our business logic into a separate file.

  Included in this project already are some business logic files, for example `source_code/hello_world/python_flask_server/openapi_server/controllers/default_controller_business_logic.py` to save on typing and copying/pasting.

  Instead lets update our Auto-generated code, such that rather than responding with `"do some magic!"`, we can call a function in our business logic file, and return that response instead. 

  We will change 
  ```python
  def helloworld_get(language=None):  # noqa: E501
    """
    ... (removing docu to save space) ...
    """
    return 'do some magic!'
  ```
  to below, where we will return a function from our business logic file.
  ```python
  def helloworld_get(language=None):  # noqa: E501
    """
    ... (removing docu to save space) ...
    """
    return default_controller_business_logic.helloworld_get(language)
  ```
  To get our python flask server to recognise these changes, go to your terminal where your flask server is running, type _ctrl+c_ (press the ctrl key and c key a the same time). This will stop the server, then simply run `python -m openapi_server` again. Hopefully there are no errors in the code. 
  Once again from another terminal run `curl http://127.0.0.1:8080/v1/helloworld`, and it should respond with something more meaningful:
  ```bash
  {
    "helloworld": "hello world",
    "language": "(default)"
  }
  ````
### Using OpenAPI Templates
In the above section we replaced some auto-generated code with some of our own custom code (to return the function from our business logic, rather a string about doing some magic). At this point we still have the issue whereby if we run the auto-generation again, this part of our own code will be overwritten. To help us work around this we can use OpenAPI Templates.

Here is the link to the OpenAPI python-flask templates:
https://github.com/OpenAPITools/openapi-generator/tree/master/modules/openapi-generator/src/main/resources/python-flask

An OpenAPI template allows one to specify the actual code that will be auto-generated. This can be a really useful technique to allow sharing of code templates within organisations.

For our simple project, we will replace 
```python
    return 'do some magic!'
```
with
```python
    return default_controller_business_logic.helloworld_get(language)
```
A template file that does this for us is included in the project already, `openapi-specs/hello-world/templates/controller.mustache`. If you compare this file to the default provided in the OpenAPI gitlab repo (https://github.com/OpenAPITools/openapi-generator/blob/master/modules/openapi-generator/src/main/resources/python-flask/controller.mustache), you will notice 2 differences 
1) we import our `*_business_logic.py` file, and we return the function from our business logic file.
  
2) we return a function from our business logic file
    ```
        return {{classFilename}}_business_logic.{{operationId}}({{#allParams}}{{paramName}}{{^required}}{{/required}}{{^-last}}, {{/-last}}{{/allParams}})
    ```
    compared to the default
    ```
        return 'do some magic!'
    ```

  Note: that we have purposely named our business logic file _default_controller_business_logic.py_ such that it can easily be mapped to the _default_controller.py_. It simplifies things within the mustache file with the variable `{{classFileName}}` appended with __business_logic_. See line 111 of _openapi-specs/hello-world/templates/controller.mustache_


To use the this OpenAPI template when auto-generating our code we just need to add one extra parameter to our OpenAPI command line (`-t openapi-specs/hello-world/templates/python-flask`)
```bash
openapi-generator-cli generate -i openapi-specs/hello-world/hello-world.yaml -g python-flask -o ./source_code/hello_world/python_flask_server -t openapi-specs/hello-world/templates/python-flask
```
Now, every time we re-generate our python flask server the code that serves the _/helloworld_ endpoint will return the function defined in our business logic file. So as OpenAPI schemas or endpoints etc change, we can re-generate the python flask server as much as we like, and we only need to maintain the actual code contained in our __business_logic.py_ file(s). I have added the (s) to files here, as it is possible to customize all the files that OpenAPI generates. This can be a very efficient way for teams streamline their development.

After re-generating the code, you should be able to stop and restart your python flask server, and once again test it out using the _curl_ command.

```bash
curl http://127.0.0.1:8080/v1/helloworld
```
