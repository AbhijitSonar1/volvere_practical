import GPUtil

# Get the list of available GPUs
gpus = GPUtil.getGPUs()

if not gpus:
    print("No GPU found.")
else:
    # Print information about each GPU
    for i, gpu in enumerate(gpus):
        print(f"GPU {i + 1}:")
        print(f"  Name: {gpu.name}")
        print(f"  Driver: {gpu.driver}")
        print(f"  Memory Total: {gpu.memoryTotal} MB")
        print(f"  Memory Free: {gpu.memoryFree} MB")
        print(f"  Memory Used: {gpu.memoryUsed} MB")
        print(f"  GPU Load: {gpu.load * 100}%")
        print(f"  GPU Temperature: {gpu.temperature} C")
        print("\n")
