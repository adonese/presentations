package main

import "net/http"

func sms() {
	http.Get("https://smsgateway.something/send/?msg=4fnfnfn")
}
