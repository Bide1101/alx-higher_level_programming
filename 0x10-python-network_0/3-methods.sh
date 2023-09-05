#!/bin/bash
# takes in a URL and displays all HTTP methods accepted by the server
curl -sI "$1" | grep "Allow:" | cut -f2- -d " "
