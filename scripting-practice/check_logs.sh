#!/bin/bash

LOG_FILE="application.log"

echo "APPLICATION LOG CHECK"
echo "---------------------"

# Check whether the log file exists
if [ -f "$LOG_FILE" ]; then

    echo "Log file found."

    # Check whether the file contains errors
    if grep -qi "error" "$LOG_FILE"; then
        echo "WARNING: Errors detected in the log!"
    else
        echo "STATUS: No errors detected."
    fi

else
    echo "WARNING: Log file does not exist."
fi