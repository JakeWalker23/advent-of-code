#!/bin/bash

# This script expects an argument for the day (e.g., day_1)
DAY_FOLDER="$1"

# Check if the day folder exists
if [ -d "$DAY_FOLDER" ]; then
  # Navigate to the specified day's folder
  cd "$DAY_FOLDER"
  # Find the Python file (assuming there's only one per folder) and run it
  PYTHON_FILE=$(ls | grep .py)
  if [ ! -z "$PYTHON_FILE" ]; then
    python3 "$PYTHON_FILE"
  else
    echo "Python file not found in $DAY_FOLDER."
  fi
else
  echo "Day folder $DAY_FOLDER not found."
fi
