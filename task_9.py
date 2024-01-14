import psutil
import uuid

def get_mac_address():
    mac_addresses = []

    # Get the MAC addresses for all network interfaces
    for interface, addrs in psutil.net_if_addrs().items():
        for addr in addrs:
            if addr.family == psutil.AF_LINK:
                mac_addresses.append(addr.address)

    return mac_addresses

# Get and print MAC addresses
mac_addresses = get_mac_address()

if not mac_addresses:
    print("No MAC addresses found.")
else:
    print("MAC addresses:")
    for i, mac_address in enumerate(mac_addresses):
        print(f"  Interface {i + 1}: {mac_address}")
