# Network Recon Assistant (MCP)

An MCP server that gives Claude recon tools for network analysis —
WHOIS lookup, DNS enumeration, port scanning via Nmap, and banner grabbing.
Built with Python as a hands-on project at the intersection of AI and cybersecurity.

---

## Tools

| Tool            | Description                              |
|-----------------|------------------------------------------|
| `whois_lookup`  | Domain/IP registration info              |
| `dns_lookup`    | A, MX, NS, TXT records                   |
| `nmap_scan`     | Open ports and services (top 100 ports)  |
| `banner_grab`   | Raw service banner on a given port       |

---

## Requirements

- Python 3.10+
- nmap installed on your system:
  - Linux: `sudo apt install nmap`
  - macOS: `brew install nmap`
  - Windows: https://nmap.org/download.html

---

## Installation
```bash
git clone https://github.com/YOUR_USERNAME/network-recon-mcp.git
cd network-recon-mcp
pip install -r requirements.txt
```

---

## Connect to Claude Desktop

### Step 1 — Find your config file

Open Claude Desktop, then:
- Click **Claude** in the menu bar → **Settings** → **Developer** → **Edit Config**

This opens `claude_desktop_config.json`. Its location by OS:

| OS      | Path                                                        |
|---------|-------------------------------------------------------------|
| macOS   | `~/Library/Application Support/Claude/claude_desktop_config.json` |
| Windows | `%APPDATA%\Claude\claude_desktop_config.json`               |
| Linux   | `~/.config/Claude/claude_desktop_config.json`               |

### Step 2 — Add the server

Paste this into the file (replace the path with your actual absolute path):
```json
{
  "mcpServers": {
    "network-recon": {
      "command": "python",
      "args": ["/absolute/path/to/network-recon-mcp/server.py"]
    }
  }
}
```

**Example paths:**
- macOS/Linux: `/home/yourname/projects/network-recon-mcp/server.py`
- Windows: `C:\\Users\\yourname\\projects\\network-recon-mcp\\server.py`

> ⚠️ On Windows use double backslashes `\\` in the path.

### Step 3 — Restart Claude Desktop

Fully quit and reopen Claude Desktop. You should see a **hammer icon** 🔨
in the bottom right of the chat input — that confirms your MCP server is connected.

### Step 4 — Try it out

Ask Claude things like:
- *"Run a WHOIS lookup on google.com"*
- *"What DNS records does github.com have?"*
- *"Scan localhost for open ports"*
- *"Grab the banner on localhost port 80"*

---

## Troubleshooting

- **Hammer icon not showing** → Check your JSON syntax (no missing commas or brackets) and restart fully
- **Nmap errors** → Make sure nmap is installed on your system, not just the Python wrapper
- **Path errors** → Use the absolute path, not a relative one like `./server.py`
- **Logs location:**
  - macOS: `~/Library/Logs/Claude/`
  - Windows: `%APPDATA%\Claude\logs\`

---

## ⚠️ Disclaimer

This tool is intended for learning and authorized use only.
Only scan systems you own or have explicit permission to test.
