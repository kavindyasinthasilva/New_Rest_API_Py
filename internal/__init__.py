import threading

from internal import config
from internal.http import routers


def init():
    # Your initialization logic here
    print("Internal initialization in Python") 

    # Use an Event to signal when the server thread can start
    start_server_event = threading.Event()

    config.get_config()

    def start_server_function():
        start_server_event.wait()
        routers.server()

    # Create a thread for starting the server
    server_thread = threading.Thread(target=start_server_function)
    server_thread.start()

    # Signal the server thread to start
    start_server_event.set()

    # Optionally, return the thread objects if needed
    return server_thread


