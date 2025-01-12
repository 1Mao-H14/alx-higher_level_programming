#!/bin/bash
# a Bash script that takes in a URL, sends a request to that URL,and displays the size of the body of the response
curl -X GET 'http://0.0.0.0:5000' | grep 'Content-Length' file.txt | cut -d ': ' -f 2
