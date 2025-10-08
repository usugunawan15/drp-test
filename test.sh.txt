#!/bin/bash
# create_test_file.sh
# Safe: only creates test_output.txt with word "testing" in the current directory

# Get the directory where the script is executed
CURRENT_DIR="$(pwd)"
FILE_NAME="test_output.txt"
FILE_PATH="${CURRENT_DIR}/${FILE_NAME}"

# Write the word "testing" to the file
echo "testing" > "$FILE_PATH"

# Confirm result
echo "✅ File created at: $FILE_PATH"
echo "   Content:"
cat "$FILE_PATH"
