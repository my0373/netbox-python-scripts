import argparse
import os
import requests
import sys
import re
import json

# ANSI escape codes for colored output
RED = "\033[91m"
GREEN = "\033[92m"
ENDC = "\033[0m"

def slugify(name):
    slug = re.sub(r'[^a-zA-Z0-9]+', '-', name.lower()).strip('-')
    return slug

def parse_args():
    parser = argparse.ArgumentParser(description="Create a new site group in NetBox")
    parser.add_argument('--hostname', type=str, default='127.0.0.1', help='NetBox hostname (default: 127.0.0.1)')
    parser.add_argument('--port', type=int, default=80, help='NetBox port (default: 80)')
    parser.add_argument('--name', required=True, help='Name of the site group')
    parser.add_argument('--description', default='', help='Optional description of the site group')
    parser.add_argument('--debug', action='store_true', help='Print the JSON payload before sending')
    return parser.parse_args()

def main():
    args = parse_args()

    # Construct the JSON payload
    # This is fully documetented in the NetBox API documentation
    # http://127.0.0.1:8000/api/schema/swagger-ui/#/dcim/dcim_site_groups_create
    
    payload = {
        "name": args.name,
        "parent": 1,
        "slug": slugify(args.name),
        "description": args.description,

    }



    api_token = os.getenv('NETBOX_API_TOKEN')
    if not api_token:
        print(f"{RED}Error: NETBOX_API_TOKEN environment variable not set{ENDC}")
        sys.exit(1)

    url = f"http://{args.hostname}:{args.port}/api/dcim/site-groups/"
    headers = {
        'Authorization': f'Token {api_token}',
        'Content-Type': 'application/json'
    }


    if args.debug:
        print("Generated JSON payload:")
        print(json.dumps(payload, indent=2))

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()
        print(f"{GREEN}Site group created successfully:{ENDC} {response.json()}\n")
    except requests.RequestException as e:
        print(f"{RED}API request failed: {e}{ENDC}")
        if response.content:
            print(f"{RED}{response.content.decode()}{ENDC}")
        sys.exit(1)

if __name__ == '__main__':
    main()
