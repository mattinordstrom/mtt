package main

// go mod init uuidgen
// go get github.com/google/uuid
// go build -o uuidgen

// Add to ../go.work

import (
	"flag"
	"fmt"

	"math/rand"
	"time"

	"github.com/google/uuid"
	"github.com/oklog/ulid/v2"
)

const LightBlue = "\x1b[96m"
const Reset = "\x1b[0m"

func main() {
	ulidFlag := flag.Bool("ulid", false, "Print ULID instead of UUID")
	flag.Parse()

	var id string

	if *ulidFlag {
		source := rand.NewSource(time.Now().UnixNano())
		entropy := rand.New(source)

		id = ulid.MustNew(ulid.Timestamp(time.Now()), entropy).String()
	} else {
		id = uuid.New().String()
	}

	fmt.Println(string(LightBlue) + id + string(Reset))
}
