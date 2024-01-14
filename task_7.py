import psutil

# Get the total RAM size in bytes
total_ram_bytes = psutil.virtual_memory().total

# Convert bytes to gigabytes
total_ram_gb = total_ram_bytes / (1024 ** 3)

print(f"Total RAM Size: {total_ram_gb:.2f} GB")


