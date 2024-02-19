from contextlib import contextmanager

from flask import Flask, request, jsonify
from services.ping.ping_services import PingService

app = Flask(__name__)


# Mocking a context manager for demonstration purposes
@contextmanager
def mock_context():
    yield None


def pinging_endpoint():
    ping_service = PingService()
    # Calling the do method
    result, err = ping_service.do(mock_context(), [])

    return encode_ping_response(result)


def decode_ping_request():
    return None, None


def encode_ping_response(response):
    return jsonify(response), 200
