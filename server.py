import asyncio
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

from tools.whois_tool import run_whois
from tools.dns_tool   import run_dns
from tools.nmap_tool  import run_nmap
from tools.banner_tool import run_banner

server = Server("network-recon")


@server.list_tools()
async def list_tools():
    return [
        Tool(
            name="whois_lookup",
            description="Get WHOIS registration info for a domain or IP",
            inputSchema={
                "type": "object",
                "properties": {
                    "target": {"type": "string", "description": "Domain or IP to look up"}
                },
                "required": ["target"]
            }
        ),
        Tool(
            name="dns_lookup",
            description="Get DNS records (A, MX, NS, TXT) for a domain",
            inputSchema={
                "type": "object",
                "properties": {
                    "target": {"type": "string", "description": "Domain to query"}
                },
                "required": ["target"]
            }
        ),
        Tool(
            name="nmap_scan",
            description="Scan the top 100 ports and detect services on a target",
            inputSchema={
                "type": "object",
                "properties": {
                    "target": {"type": "string", "description": "IP or domain to scan"}
                },
                "required": ["target"]
            }
        ),
        Tool(
            name="banner_grab",
            description="Grab the raw service banner from a specific port",
            inputSchema={
                "type": "object",
                "properties": {
                    "target": {"type": "string", "description": "IP or domain"},
                    "port":   {"type": "integer", "description": "Port number to connect to"}
                },
                "required": ["target", "port"]
            }
        ),
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict):
    # asyncio.to_thread() runs blocking functions in a thread
    # so they don't freeze the async event loop
    if name == "whois_lookup":
        output = await asyncio.to_thread(run_whois, arguments["target"])

    elif name == "dns_lookup":
        output = await asyncio.to_thread(run_dns, arguments["target"])

    elif name == "nmap_scan":
        output = await asyncio.to_thread(run_nmap, arguments["target"])

    elif name == "banner_grab":
        output = await asyncio.to_thread(run_banner, arguments["target"], arguments["port"])

    else:
        output = f"Unknown tool: {name}"

    return [TextContent(type="text", text=output)]


async def main():
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )


if __name__ == "__main__":
    asyncio.run(main())
