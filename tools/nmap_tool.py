import nmap

def run_nmap(target: str) -> str:
    try:
        nm = nmap.PortScanner()
        nm.scan(target, arguments="-sV --top-ports 100")

        results = []
        for host in nm.all_hosts():
            results.append(f"Host: {host} ({nm[host].hostname()})")
            results.append(f"State: {nm[host].state()}")
            for proto in nm[host].all_protocols():
                for port in sorted(nm[host][proto].keys()):
                    info     = nm[host][proto][port]
                    state    = info["state"]
                    name     = info["name"]
                    product  = info.get("product", "")
                    version  = info.get("version", "")
                    results.append(
                        f"  {proto}/{port}: {state} | {name} {product} {version}".strip()
                    )

        return "\n".join(results) if results else "No hosts found or no open ports"

    except Exception as e:
        return f"Nmap error: {e}"
