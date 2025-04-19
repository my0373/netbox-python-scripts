# NetBox Python Scripts

A set of Python scripts to interact with the NetBox platform using Python.

> **Note:** These scripts have been developed and tested only on **Linux** and **macOS** systems.

## Prerequisites

- Python 3.13 (may work on other versions, but has only been tested on 3.13)
- [`uv`](https://github.com/astral-sh/uv) (a fast Python package manager)

### Setting Up with `uv`

1. Install `uv`:
```bash
curl -Ls https://astral.sh/uv/install.sh | bash
```

2. Create and sync a virtual environment:
```bash
uv venv
uv pip install requests tabulate
```

3. Activate the virtual environment:
```bash
source .venv/bin/activate
```

## Setup

### 1. Generate an API Token

To authenticate with the NetBox API, you need an API token.

If NetBox is running locally on port 8000, go to:

```
http://127.0.0.1:8000/users/tokens/
```

Create a new token and copy it.

### 2. Set the Environment Variable

Export the token to your environment so the script can use it:
```bash
export NETBOX_API_TOKEN="your_api_token_here"
```

## Scripts

### Get sites stored in NetBox via the API.
### `api/get_sites.py`

This script retrieves a list of DCIM sites from a NetBox instance and prints the results in a table format.

#### Usage

Run the script using Python:
```bash
python api/get_sites.py
```

You can override the default host and port:
```bash
python api/get_sites.py --hostname 192.168.1.1 --port 8000
```

#### Example Output

```
+----+-----------+-----------+----------+--------------+----------+--------------+------------------------------------------------------------+
| ID | Name      | Slug      | Status   | Facility     | Region   | Tenant       | Physical Address                                            |
+----+-----------+-----------+----------+--------------+----------+--------------+------------------------------------------------------------+
| 1  | Brookside | brookside | Active   | 68Brookside  | Paulton  | York family  | 68 Brookside, Paulton, Paulton, Bristol, BS397YR         |
+----+-----------+-----------+----------+--------------+----------+--------------+------------------------------------------------------------+
```
### Create a new site group stored in NetBox via the API using POST.
### `api/post_new_site-group.py`

This script creates a new site group in the NetBox DCIM module using a POST request.

#### Usage

```bash
python api/post_new_site-group.py --name "Industrial Sites" --description "The industrial sites"
```

You can also specify a custom hostname and port:
```bash
python api/post_new_site-group.py --hostname 192.168.1.1 --port 8000 --name "Industrial Sites"
```

Enable debug mode to print the generated JSON payload before it is sent:
```bash
python api/post_new_site-group.py --name "Industrial Sites" --debug
```

#### Description

- `--name` is required and sets the name of the site group.
- `--description` is optional and defaults to an empty string.
- The `slug` is automatically generated from the name by converting it to lowercase and replacing spaces/special characters with hyphens.
- The script sends the payload using `application/json` with the required API token set via `NETBOX_API_TOKEN`.

If successful, the response will be printed in green. If it fails, the error will be shown in red.

## Troubleshooting

If you see an error like:
```
Error: NETBOX_API_TOKEN environment variable not set
```
Make sure you've properly set the environment variable before running the script.

If the API call fails or the response format is unexpected, verify your hostname, port, and token.

---

Enjoy managing your NetBox inventory with simple Python automation!
