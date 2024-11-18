import requests

# Function to get account information
def get_account_info(api_key):
    url = f"https://api.shodan.io/api-info?key={api_key}"
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return f"Error fetching account info: {e}"

# Function to search for an IP address
def search_ip(api_key, ip):
    url = f"https://api.shodan.io/shodan/host/{ip}?key={api_key}"
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return f"Error fetching IP info: {e}"
