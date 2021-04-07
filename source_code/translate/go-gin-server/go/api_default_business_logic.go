package openapi

import (
	"fmt"
	"net/http"

	"github.com/gin-gonic/gin"
)

// TranslateGetBusinessLogic - translate hello world endpoint
func TranslateGetBusinessLogic(c *gin.Context) {
	queryParams := c.Request.URL.Query()
	fmt.Println(queryParams)
	// todo: add proper debug string here to print query
	if queryParams["language"][0] == "bavarian" {
		c.JSON(http.StatusOK, InlineResponse200{Language: "bavarian", Text: "servus welt"})
	} else {
		defaultResp := InlineResponse200{Language: "default", Text: "hello world"}
		c.JSON(http.StatusOK, defaultResp)
	}
}
