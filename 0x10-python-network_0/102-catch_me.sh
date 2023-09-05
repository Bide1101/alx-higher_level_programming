#!/bin/bash
# This script makes a request to the given server
curl -s -X PUT "http://0.0.0.0:5000/catch_me" | grep "You got me!"
