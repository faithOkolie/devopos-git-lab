import shutil

# Get disk usage information
total, used, free = shutil.disk_usage("/")

# Calculate percentage used
usage_percent = (used / total) * 100

print("SERVER DISK MONITOR")
print("-------------------")

print(f"Total space: {total // (1024**3)} GB")
print(f"Used space: {used // (1024**3)} GB")
print(f"Free space: {free // (1024**3)} GB")

print(f"Disk usage: {usage_percent:.2f}%")

# Check disk usage condition
if usage_percent >= 80:
    print("WARNING: Disk space is running low!")
else:
    print("STATUS: Disk space is healthy.")