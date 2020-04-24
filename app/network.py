import socket


def get_local_ip() -> str:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        s.connect(("10.255.255.255", 1))

        return s.getsockname()[0]
    except Exception:
        return "127.0.0.1"
    finally:
        s.close()
