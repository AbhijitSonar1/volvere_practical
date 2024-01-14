from screeninfo import get_monitors

# Get the list of monitors
monitors = get_monitors()

if not monitors:
    print("No monitors found.")
else:
    # Print information about each monitor
    for i, monitor in enumerate(monitors):
        print(f"Monitor {i + 1}:")
        print(f"  Size: {monitor.width_mm / 25.4:.2f} x {monitor.height_mm / 25.4:.2f} inches")
        print("\n")
