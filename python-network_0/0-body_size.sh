#!/bin/bash

# Get the URL from the command line argument
url=$1

# Send a GET request to the URL and save the response body to a variable
response_body=$(curl -sSL $url)

# Get the size of the response body in bytes
body_size=$(echo -n "$response_body" | wc -c)

# Display the size of the response body in bytes
echo "The size of the response body is $body_size bytes."
