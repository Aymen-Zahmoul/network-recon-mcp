# Network Recon Assistant (MCP)

An MCP server that gives Claude recon tools for network analysis.

## Tools
- `whois_lookup` — domain/IP registration info
- `dns_lookup`   — A, MX, NS, TXT records
- `nmap_scan`    — open ports and services
- `banner_grab`  — raw service banner on a given port

## Setup
pip install -r requirements.txt

## Run
python server.py

## Connect to Claude Desktop
Add to your claude_desktop_config.json:
{
  "mcpServers": {
    "network-recon": {
      "command": "python",
      "args": ["/absolute/path/to/server.py"]
    }
  }
}
