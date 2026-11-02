# simple-network-checker
A simple Python tool that checks website availability and response time.

## Features

- Lets the user enter a  website address.
- Adds `https://` when no protocol is entered.
- Uses `example.com` when the input is left empty.
- Shows whether the server responds.
- Displays the HTTP status code.
- Measures the response time in milliseconds.
- Handles common connection errors.

## Requirements

- Python 3
- No external libraries are required.

## How to run

1. Download or clone this repository.
2. Open a terminal in the project folder.
3. Run:

```bash
python main.py
```

On Windows, you can also use:

```powershell
py main.py
```

## Example

```text
--- NETWORK CHECKER ---
Example: python.org
Enter a website: example.com

Checking https://example.com...
Status: Online
HTTP status code: 200
Response time: 180.5 ms

Check finished.
```

The response time and status code can be different each time you run the program.

## Note

This program checks whether a website responds to an HTTP/HTTPS request. It is not a full internet speed test and does not work exactly like the `ping` command.
