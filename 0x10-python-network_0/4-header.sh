#!/bin/bash
# Takes in a URL as an argument, sends a GET request and displays response body
curl -sH "X-School-User-Id: 98" "$1"
