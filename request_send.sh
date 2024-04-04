#!/bin/bash

# Default values
item="-all"

# Parse named arguments
while [[ "$#" -gt 0 ]]; do
    case $1 in
        -item) item="$2"; shift ;;
        *) echo "Unknown parameter passed: $1"; exit 1 ;;
    esac
    shift
done

# Check if item parameter is set to "default_value"
if [ "$item" = "-all" ]; then
    curl -X POST -H "Content-Type: application/json" -d '{"text":"apple"}' 'http://127.0.0.1:8000/items'
    curl -X POST -H "Content-Type: application/json" -d '{"text":"banana"}' 'http://127.0.0.1:8000/items'
    curl -X POST -H "Content-Type: application/json" -d '{"text":"carrot"}' 'http://127.0.0.1:8000/items'
    curl -X POST -H "Content-Type: application/json" -d '{"text":"dumpling"}' 'http://127.0.0.1:8000/items'
    curl -X POST -H "Content-Type: application/json" -d '{"text":"eggs"}' 'http://127.0.0.1:8000/items'
    curl -X POST -H "Content-Type: application/json" -d '{"text":"fish"}' 'http://127.0.0.1:8000/items'
    curl -X POST -H "Content-Type: application/json" -d '{"text":"grapes"}' 'http://127.0.0.1:8000/items'
else
    curl -X POST -H "Content-Type: application/json" -d '{"text":"'${item}'"}' 'http://127.0.0.1:8000/items?item'
fi
