import subprocess
import time
import socket

import pytest


def wait_for_port(host: str, port: int, timeout: int = 30):
    start = time.time()
    while time.time() - start < timeout:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            if sock.connect_ex((host, port)) == 0:
                return True
        time.sleep(1)
    return False


@pytest.fixture(scope="session")
def live_server():
    host = "127.0.0.1"
    port = 8000

    proc = subprocess.Popen(
        ["shiny", "run", "--host", host, "--port", str(port), "src.app"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    if not wait_for_port(host, port, timeout=30):
        stdout, stderr = proc.communicate(timeout=5)
        raise RuntimeError(
            f"Shiny app failed to start on {host}:{port}\n\nSTDOUT:\n{stdout}\n\nSTDERR:\n{stderr}"
        )

    class Server:
        url = f"http://{host}:{port}"

    yield Server()

    proc.terminate()
    proc.wait(timeout=5)