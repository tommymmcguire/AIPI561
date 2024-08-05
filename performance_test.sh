#!/bin/bash

# Variables
URL="http://localhost:5001/chat"
CONCURRENCY=2
REQUESTS=5
DATA='{"message": "What are some effective marketing strategies for a new startup?"}'
TIMEOUT=150  # Timeout in seconds

# Create a temporary file for the payload
TEMP_PAYLOAD=$(mktemp)
echo "$DATA" > $TEMP_PAYLOAD

# Run Apache Bench with increased timeout and verbosity
ab -v 4 -s $TIMEOUT -p $TEMP_PAYLOAD -T application/json -c $CONCURRENCY -n $REQUESTS $URL

# Clean up the temporary file
rm $TEMP_PAYLOAD
