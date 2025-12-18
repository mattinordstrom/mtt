package main

import (
	"flag"
	"fmt"
	"math/rand"
	"os"
	"time"

	"github.com/google/uuid"
	"github.com/oklog/ulid/v2"
	"golang.design/x/clipboard"
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

	if err := clipboard.Init(); err != nil {
		fmt.Fprintf(os.Stderr, "ERROR: failed to initialize clipboard: %v\n", err)
		os.Exit(1)
	}
	clipboard.Write(clipboard.FmtText, []byte(id))

	// Need a short sleep here to ensure clipboard is updated (TODO use wl-copy instead on Wayland?)
	time.Sleep(300 * time.Millisecond)

	//got := clipboard.Read(clipboard.FmtText)
	//fmt.Fprintf(os.Stderr, "DEBUG: clipboard now has: %s\n", string(got))

	fmt.Println(string(LightBlue) + id + string(Reset))
}
