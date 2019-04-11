#!/bin/bash
# Send a header to the server
curl "$1" -X GET -H "X-HolbertonSchool-User-Id: 98"
