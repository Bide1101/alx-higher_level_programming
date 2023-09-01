#!/bin/bash
# This script ends a JSON request to a URL and displays the response
curl -s -X POST "Content-Type: application/json" -d "$(cat $2)" $1
