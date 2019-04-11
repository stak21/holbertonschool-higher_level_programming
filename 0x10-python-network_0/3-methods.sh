#!/bin/bash
# OPTIONS all methods available
curl -i -X OPTIONS -s "$1" | grep "Allow" | cut -d ' ' -f2-
