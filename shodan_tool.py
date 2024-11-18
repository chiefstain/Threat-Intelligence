import requests
import json

def get_shodan_info(api_key, query):
    base_url = "https://api.shodan.io/shodan/host/search"
    params = {
        'key': api_key,
        'query': query
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        results = response.json()
        return results
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")

def save_results_to_file(results, file_name):
    with open(file_name, "w") as file:
        json.dump(results, file, indent=4)
        print(f"Results saved to {file_name}")

def main():
    # Shodan API Key
    api_key = "api"
    query = input("Enter your Shodan query: ")  # Dynamic input from the user

    print("Fetching data from Shodan API...")
    results = get_shodan_info(api_key, query)

    if results:
        print("Results:")
        for result in results.get('matches', []):
            ip = result.get('ip_str', 'N/A')
            port = result.get('port', 'N/A')
            org = result.get('org', 'N/A')
            print(f"IP: {ip}, Port: {port}, Org: {org}")

        # Save results to file
        save_results_to_file(results, "shodan_results.json")
    else:
        print("No results found.")

if __name__ == "__main__":
    main()
