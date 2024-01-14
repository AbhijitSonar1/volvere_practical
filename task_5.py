
import os
import multiprocessing

# Get the number of CPU cores
cpu_cores = os.cpu_count()
print(f"Number of CPU cores: {cpu_cores}")

# Get the number of CPU threads
cpu_threads = multiprocessing.cpu_count()
print(f"Number of CPU threads: {cpu_threads}")