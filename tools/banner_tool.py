import socket

def run_banner(target: str, port: int) -> str:
    try:
        s = socket.socket()
        s.settimeout(3)
        s.connect((target, port))
        banner = s.recv(1024).decode(errors="ignore").strip()
        s.close()
        return banner if banner else "No banner received"
    except Exception as e:
        return f"Banner grab error: {e}"
