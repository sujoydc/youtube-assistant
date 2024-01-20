#!/bin/bash

# Check if a directory path is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <path_to_directory>"
    exit 1
fi

FOLDER_PATH=$1

# Navigate to the folder
cd "$FOLDER_PATH" || exit

# Create a virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Upgrade pip as it always throws WARNING otherwise
pip3 install --upgrade pip

# Install from requirements.txt
if [ -f "requirements.txt" ]; then
    pip3 install -r requirements.txt
else
    echo "The file 'requirements.txt' not found."
fi

# Open VS Code
code .
