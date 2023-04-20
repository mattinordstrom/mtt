package main

import (
	"fmt"
	"strings"
)

func main() {
	////////////////
	//// SUBSTRING AND REPLACE
	testString := "Hello, World!"
	fmt.Println(testString[7:12])

	fmt.Println(testString[:5])

	newTestString := strings.Replace(testString, "Hello", "Jello", 1)
	fmt.Println(newTestString)

	////////////////
	//// IF STATEMENT
	a := 200
	b := 33
	if b > a {
		fmt.Println("b is greater than a")
	} else if a == b {
		fmt.Println("a and b are equal")
	} else {
		fmt.Println("b is not greater than a")
	}
}
