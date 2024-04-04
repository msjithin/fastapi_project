#!/bin/bash

# Default values
limit="-all"

# Parse named arguments
while [[ "$#" -gt 0 ]]; do
    case $1 in
        -limit) limit="$2"; shift ;;
        *) echo "Unknown parameter passed: $1"; exit 1 ;;
    esac
    shift
done

# Check if item parameter is set to "default_value"
if [ "$limit" = "-all" ]; then
    curl -X GET 'http://127.0.0.1:8000/items'
else
    curl -X GET 'http://127.0.0.1:8000/items?limit='$limit
fi