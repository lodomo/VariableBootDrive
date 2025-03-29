import json
import subprocess

import yaml
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

YAML_FILE = "settings.yaml"
SETTINGS = {}
with open(YAML_FILE, "r") as file:
    SETTINGS = yaml.safe_load(file)["web_if"]["api"]

DEVICE = SETTINGS["device_backend_script"]


@app.route("/")
def index():
    text = """
    <h1>YOU DO NOT BELONG HERE.<h1><h2>VBD:WEB API</h2>
    """
    return text


@app.route("/info")
def info():
    result = call_device("--info")
    device_info = result.stdout.decode().strip()
    info_json = json.loads(device_info.replace("'", '"'))
    return info_json


# Created these paths based on Dal's design to make them interchangable with the device frontend.

# Use POST to upload files


@app.route("/img/local/<filename>")
def img_local():
    """
    Upload a file to the device
    """
    pass


@app.route("/img/remote/<filename>")
def img_remote():
    """
    Download a file to device from remote server
    """
    pass


@app.route("/pi/health")
def pi_health():
    """
    Get the health of the device
    """
    return info()


@app.route("/pi/os")
def pi_os():
    """
    Update the OS of the device
    """
    pass


@app.route("/pi/vbd")
def pi_vbd():
    """
    Update the VBD of the device
    """
    pass


@app.route("/pi/pin/<old>/<new>")
def pi_pin():
    """
    Update the pin of the device
    """
    pass


@app.route("/pi/auth")
def pi_auth():
    """
    User login
    """
    pass


@app.route("/pi/mode/<filename_or_off>")
def pi_mode():
    """
    Set the device ISO mode
    """
    pass


@app.route("/pi/fd/")
def pi_fd():
    """
    Toggle the device flash drive mode
    """
    pass


def call_device(command, *args):
    return subprocess.run(["python", DEVICE, command, *args], stdout=subprocess.PIPE)


if __name__ == "__main__":
    app.run()
