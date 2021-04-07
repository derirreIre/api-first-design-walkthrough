# Step by step example of using API First Design Principles to spin up a hello world polyglot stack 
# 4) Switching tech stack, replacing an existing python based service with a golang based service

## Steps:
1) Initially lets auto-generate our helloworld service
2) Updating endpoints and using OpenAPI templates
3) Spin up a second service and using auto-generated client-side code
4) <b>Switching tech stack, replacing an existing python-based service with a golang based service</b> (we are here)

### Lets replace the _translate_ python-flask server

So by now we have both our services up and running in python. But lets say for whatever reason we want to swap out our python-based _translate_ service, for a golang based one.

As we have been following API-first design principles, this is a very easy task. We need to auto-generate a server from the already existing OpenAPI specification. And add a file containing our business logic.

### Generate Golang translate server:
To generate the Go server, we will use the same OpenAPI specification as before. And similarly there is a OpenAPI template .mustache file that will make use of the _default_controller_business_logic.go_ file. From the top level directory of our project run.
```bash
openapi-generator-cli generate -i openapi-specs/translate/translate.yaml -g go-gin-server -o ./source_code/translate/go-gin-server -t openapi-specs/translate/templates/go-gin-server
```
change the default port of the Go based translate server to 8081 (`source_code/translate/go-gin-server/main.go`, line 30). 
```go
func main() {
	log.Printf("Server started")

	router := sw.NewRouter()

	log.Fatal(router.Run(":8081")) // the default port is 8080
}
```

Make sure your python Translate server is not running (run `ctrl+c` on your terminal to quit it)

### Golang setup
Navigate to the the top level directory of the project, where _README.md_ is. As per the requirements in the _README.md_ file, check that you have Go installed.

If you haven't used to _gin-gonic_ package before you will need to first run:
```bash
go get github.com/gin-gonic/gin
```

Get the server up and running, navigate to the directory containing the _main.go_ file `cd source_code/translate/go-gin-server`, and run
```bash
go run main.go
```
Now test the system end-to-end using `curl -X GET "http://127.0.0.1:8080/v1/helloworld?language=bavarian" -H  "accept: application/json"`. 

If everything has worked out, we have replaced the _translate_ Python server with a _translate_ Go server according to the same _translate_ OpenAPI spec (plus a handful of lines of business logic code). The _helloworld_ service is still able to communicate with the Go _translate_ service using the client-side code we generated from the _translate_ OpenAPI spec in part (3). And hopefully you realise some of the benefits and efficiencies API First design brings.
