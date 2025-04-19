import argparse
import os
import requests
import sys
from tabulate import tabulate

# ANSI escape code for red text
RED = "\033[91m"
ENDC = "\033[0m"

def parse_args():
    """
    Parse command line arguments.
    """
 
    parser = argparse.ArgumentParser(
        description="""
        NetBox API caller.

        Example usage:
        python script.py
        python script.py --hostname 192.168.1.1 --port 8080

        Requires the NETBOX_API_TOKEN environment variable to be set.

        You can generate an API token by visiting the following URL
        (assuming NetBox is running at 127.0.0.1 on port 8000):
        http://127.0.0.1:8000/users/tokens/
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument('--hostname', type=str, default='127.0.0.1', help='Hostname of NetBox instance (default: 127.0.0.1)')
    parser.add_argument('--port', type=int, default=80, help='Port number of NetBox instance (default: 80)')

    return parser.parse_args()

def call_api(args):
    """
    Call the NetBox API to get site information and print it in a table format.
    """
    
    # Construct the URL for the API endpoint
    
    
    url = f"http://{args.hostname}:{args.port}/api/dcim/sites/"

    api_token = os.getenv('NETBOX_API_TOKEN')
    if not api_token:
        print(f"{RED}Error: NETBOX_API_TOKEN environment variable not set{ENDC}")
        sys.exit(1)

    headers = {'Authorization': f"Token {api_token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        if 'results' in data:
            print_results_as_table(data['results'])
        else:
            print(f"{RED}Unexpected response format.{ENDC}")
    except requests.RequestException as e:
        print(f"{RED}API call failed: {e}{ENDC}")
        sys.exit(1)

def print_results_as_table(results):
    """
    Print the netbox results in a table format using tabulate.
    """
    table_data = []
    headers = ["ID", "Name", "Slug", "Status", "Facility", "Region", "Tenant", "Physical Address"]

    for result in results:
        table_data.append([
            result.get('id'),
            result.get('name'),
            result.get('slug'),
            result.get('status', {}).get('label'),
            result.get('facility'),
            result.get('region', {}).get('name'),
            result.get('tenant', {}).get('name'),
            result.get('physical_address')
        ])

    print(tabulate(table_data, headers=headers, tablefmt="grid"))

if __name__ == "__main__":
    """
    Main
    """
    args = parse_args()
    call_api(args)
