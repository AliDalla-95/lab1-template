import socket
import time
import os


def check_db_connection(host, port):
    start_time = time.time()
    timeout = 10  # 10 second timeout

    try:
        sock = socket.create_connection((host, port), timeout=timeout)
        print(f"Successfully connected to {host}:{port}")
        sock.close()
        return True
    except socket.error as e:
        elapsed_time = time.time() - start_time
        print(f"Failed to connect to {host}:{port}. Error: {str(e)}. Elapsed time: {elapsed_time:.2f} seconds")
        return False


if __name__ == "__main__":
    host = os.environ.get("SQL_HOST", "db")  # Replace with your actual PostgreSQL host
    port = os.environ.get("SQL_PORT", "5432")  # Default PostgreSQL port
    print(f'The host is:{host}')
    print(f'The port is: {port}')
    check_db_connection(host, port)
