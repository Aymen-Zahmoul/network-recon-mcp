import whois

def run_whois(target: str) -> str:
    try:
        result = whois.whois(target)
        return str(result)
    except Exception as e:
        return f"WHOIS error: {e}"
