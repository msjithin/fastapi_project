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
    curl -X 'GET' \
        'http://localhost:8080/items/?skip=0&limit=100' \
        -H 'accept: application/json'
else
    curl -X 'GET' \
        'http://localhost:8080/items/?skip=0&limit='$limit \
        -H 'accept: application/json'
fi