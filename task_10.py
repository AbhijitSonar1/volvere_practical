import requests

def get_public_ip():
    try:
        # Use httpbin.org to get the public IP address
        response = requests.get('https://httpbin.org/ip')
        data = response.json()
        public_ip = data.get('origin')
        return public_ip
    except Exception as e:
        print(f"Error retrieving public IP address: {e}")
        return None

# Get and print the public IP address
public_ip_address = get_public_ip()

if public_ip_address:
    print(f"Public IP address: {public_ip_address}")
else:
    print("Unable to retrieve public IP address.")
