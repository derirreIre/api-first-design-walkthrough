# Step by step example of using API First Design Principles to spin up a hello world polyglot stack 
# 1) Spin up a basic helloworld service

For an overview of what we are about to build see the `README.md` file. 

## Steps:
1) <b>Initially lets auto-generate our helloworld service</b> (we are here)
2) Updating endpoints and using OpenAPI templates
3) Spin up a second service and using auto-generated client-side code
4) Switching tech stack, replacing an existing python-based service with a golang based service

### System requirements satisfied?
- Check you have everything in the `requirements` section described in the 'README.md' file.

### Generating a basic hello world python-flask server
- Lets begin by generating a basic hello world python-flask server.

    ```openapi-generator-cli generate -i openapi-specs/hello-world/hello-world.yaml -g python-flask -o ./source_code/hello_world/python_flask_server```

- This will use to openapi generator to generate a python-flask server (`-g`), using the OpenAPI spec as input (`-i`), and output the source code to the chosen location (`-o`).

### Get our python-flask server running
  Firstly we need to source our python virtual environment. There are a few ways to do this, here is one suggestion. Lets start from the top level directory/folder of the project (parallel to this `README.md` file).
  ```bash
  # create your python virtual environment
  python3 -m venv _venv
  ```
  ```bash
  # on linux/mac/wsl, activate it
  source _venv/bin/activate
  ````
  ```bash
  # on windows, activate it 
  _venv/scripts/activate 
  ````
  ```bash
  # upgrade the python installer tool pip
  pip install -U pip  
  ````
  ```bash
  # install the required python packages
  pip install -r source_code/hello_world/python_flask_server/requirements.txt
  ```
  ```bash
  # navigate to your auto-generated python-flask server
  cd source_code/hello_world/python_flask_server/
  ```
  ```bash
  # start your server
  python -m openapi_server
  ```
  Now you should see that your server is running on your local machine (0.0.0.0 or 127.0.0.1 on port 8080). You can test the server by opening another terminal, and running the following curl command 
  ```bash 
  curl http://127.0.0.1:8080/v1/helloworld
  ```
  (or point your browser to `http://127.0.0.1:8080/v1/helloworld`) which will return response like: `"do some magic!"`

  The python-flask server also provides a really useful UI to test your server, enter the following into your browser ```http://127.0.0.1:8080/v1/ui/```

### Success! :)
  Great, we have accomplished the most difficult step, the first step, and we have a server running. But rather than returning `"do some magic!"`, we should update the server to return something more meaningful.
