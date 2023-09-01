#!/bin/bash
# Takes in a URL, sends a POST request to the URL, and displays the response
curl -s -d "email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD" -X POST "$1"
