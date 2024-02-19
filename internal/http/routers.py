from flask import Flask
import threading

from internal.config import get_config
from internal.http.handler import ping_handler

app = Flask(__name__)


def router():
    print("router called")

    @app.route('/ping', methods=['GET'])
    def ping_route():
        return ping_handler()


router()


def start_server(port, stop_event):
    app.run(port=port, threaded=True)
    stop_event.set()


def server():
    config_container = get_config()

    server_port = config_container .app_config.port
    # Create an event to signal the threads to stop
    stop_event = threading.Event()

    # Start the server in a separate thread
    server_thread = threading.Thread(target=start_server, args=(server_port, stop_event))
    server_thread.start()

    # To stop the server, you can set the stop_event
    input("Press Enter to stop the server...\n")
    stop_event.set()

    # Optionally, perform any cleanup or shutdown tasks before exiting
    server_thread.join()
