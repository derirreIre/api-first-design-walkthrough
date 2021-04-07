# How-to example walkthrough using API First Design Principles to spin up a local hello world polyglot stack 
This project aims to show some of the benefits and efficiencies API First Design can bring through using a simple hello world example. We will not repeat the benefits here, they are nicely documented elsewhere (https://swagger.io/resources/articles/adopting-an-api-first-approach/). At the end of this walkthrough you will have spun up two services (Python and Go based respectively) according to their respective OpenAPI specifications, make some functional changes, and get them talking to each other on your local machine.

## Walkthrough Overview
The setup will consist of two services auto-generated from two API Specifications. 

The example consists of two services:

a) An `helloworld` service serving an endpoint that will respond with "hello world". 

b) A `translate` service will be spun up and will provide a <i>translation</i> of an input string into another language. 

The first `helloworld` service will use the `translate` service to translate "hello world" into the end-user's language of choice.

## Step-by-step

- [walkthrough/Instructions_1.md](walkthrough/Instructions_1.md)

  Initially the _helloworld_ service will be spun up as the vanilla auto-generated python-flask server using the OpenAPI generator.

- [walkthrough/Instructions_2.md](walkthrough/Instructions_2.md)

  Functional "business logic" code will be added so that the service responds with"hello world". The "business logic" is already included in pre-prepared `.py` (and `.go`) files. OpenAPI temmplates will be used so that all the business logic can be contained in a file that will not be overwritten each time the server is generated using the OpenAPI Generator.
  
- [walkthrough/Instructions_3.md](walkthrough/Instructions_3.md)

  The auto-generated vanilla _translate_ service will be spun up as another python-flask server, including the pre-prepared business logic. In this toy example we will use only "English" and "Bavarian" translations of "hello world".
  
  The client-side code to communicate with the _translate_ service will be auto-generated from its' OpenAPI specification.  This will be imported into the _helloworld_ service, so that it can take a language input parameter, communicate with the translate service, and return "hello world" in the language of choice to the end-user.

- [walkthrough/Instructions_4.md](walkthrough/Instructions_4.md)

  To serve as a practical example of API First Design we will swap the python based _translate_ service to a Golang implementation using the same OpenAPI spec. As everything has been generated according to API specs, the _translate_ service's client-side code (that is now already part of the _helloworld_ python-flask service) will also work seamlessly with the Golang implementation.

## Directory structure
- _/openapi-specs_ contains the openapi .yml specification files that are the 'single source of truth' for the functionality and documentation of our services. 

- _/source_code_ is the directory the auto-generated code will end up in. Already present are the `.py` and `.go` files containing the functional business logic which will be used by the auto-generated services. 

- _/walkthrough_ contains the step by step instructions to be followed.
## Requirements: 
- OpenAPI Generator (see download options here: https://openapi-generator.tech/docs/installation/)
  - type `openapi-generator-cli version` or `openapi-generator version` to see the version you have installed. Throughout the rest of this document we will use `openapi-generator-cli`, just watch out for this if you are copy/pasting the code below.
- Python 3 (https://www.python.org/downloads/)
  - type `python --version` or `python3 --version` into your terminal to check if you have python installed.
- GoLang (https://golang.org/doc/install)
  - type `go version` into your terminal to get the version of Golang you have installed.

## Instructions
The step by step tutorial can be found in the `instructions.md` file.

## feedback
please give any feedback/suggestions/critism you have, the more the merrier!