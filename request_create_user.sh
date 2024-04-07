#!/bin/bash

# Default values
username=""
password=""

# Parse named arguments
while [[ "$#" -gt 0 ]]; do
    case $1 in
        -u|--user) username="$2"; shift ;;
        -p|--pass) password="$2"; shift ;;
        *) echo "Unknown parameter passed: $1"; exit 1 ;;
    esac
    shift
done


# Check if parameters are set to default
if [[ "$username" != "" && "$password" != "" ]]; then
    curl -X 'POST' \
            'http://localhost:8080/users/' \
            -H 'accept: application/json' \
            -H 'Content-Type: application/json' \
            -d '{
            "email": "'${username}'",
            "password": "'${password}'"
            }'
else
    echo "Arguments for Username -u|--user and password -p|--pass are required"
    echo "Exiting!"
fi 