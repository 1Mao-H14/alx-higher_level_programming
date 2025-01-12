#!/bin/bash
# a Bash script that takes in a URL, sends a request to that URL,
# and displays the size of the body of the response
curl -i -X GET -o file.txt 'http://0.0.0.0:5000'
# using cut
grep 'Content-Length' file.txt | cut -d ':' -f 2
