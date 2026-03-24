import dns.resolver

def run_dns(target: str) -> str:
    record_types = ["A", "MX", "NS", "TXT"]
    results = []

    for rtype in record_types:
        try:
            answers = dns.resolver.resolve(target, rtype)
            for record in answers:
                results.append(f"{rtype}: {record}")
        except Exception:
            results.append(f"{rtype}: not found")

    return "\n".join(results)
