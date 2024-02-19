from flask import Flask

from endpoint.ping.ping import pinging_endpoint

app = Flask(__name__)


def ping_handler():
    response = pinging_endpoint()
    return response
