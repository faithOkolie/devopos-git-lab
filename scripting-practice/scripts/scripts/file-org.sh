
#!/bin/bash

echo "FILE ORGANISER"
echo "--------------"

# Step 1: Create folders
mkdir -p logs scripts reports

echo "Folders created successfully."

# Step 2: Move log files
for file in *.log; do
    if [ -f "$file" ]; then
        mv "$file" logs/
        echo "Moved $file to logs/"
    fi
done

# Step 3: Move script files
for file in *.sh *.py; do
    if [ -f "$file" ]; then
        mv "$file" scripts/
        echo "Moved $file to scripts/"
    fi
done

# Step 4: Move report files
for file in *.txt *.csv; do
    if [ -f "$file" ]; then
        mv "$file" reports/
        echo "Moved $file to reports/"
    fi
done

echo "------------------------"
echo "File organisation complete!"
