#!/bin/bash
adr="$1"
curl -I -X GET -o file.html "http://$adr"
awk -F ': ' ' /Content-Length/ { print $2 }' file.html
