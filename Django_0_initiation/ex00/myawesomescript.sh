#!/bin/sh

# Checking if there is a link given as argument
if [ -n "$1" ]; then

  ## Address Bit.ly to decode
  BITLY_LINK=$1

  ## Query the Bit.ly API to obtain the JSON response
  curl -s -L -o /dev/null -w "%{url_effective}" -D - "$BITLY_LINK" | grep -m 1 -oP '(?<=Location: ).*'

fi