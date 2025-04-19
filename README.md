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
uv sync
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

## Troubleshooting

If you see an error like:
```
Error: NETBOX_API_TOKEN environment variable not set
```
Make sure you've properly set the environment variable before running the script.

If the API call fails or the response format is unexpected, verify your hostname, port, and token.

---

Enjoy managing your NetBox inventory with simple Python automation!

