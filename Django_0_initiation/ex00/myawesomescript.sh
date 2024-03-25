#!/bin/sh

# Checking if there is a link given as argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <bit.ly_link>"
    exit 1
fi

# Checking if the given link begins with "bit.ly"
#if ! echo "$1" | grep -q "^https\?://bit\.ly"; then
#    echo "The input has to begin with: bit.ly"
#    exit 1
#fi

# Adress Bit.ly to decode
BITLY_LINK=$1

# Query the Bit.ly API to obtain the JSON response
response=$(curl -s -L -o /dev/null -w "%{url_effective}" -D - "$BITLY_LINK")

# Extract the original address from the JSON response
original_url=$(echo "$response" | grep -oP '(?<=Location: ).*' | tr -d '\r')

# Display original address
echo "Original adress: $original_url"
