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


def call_device(command, *args):
    return subprocess.run(["python", DEVICE, command, *args], stdout=subprocess.PIPE)


if __name__ == "__main__":
    app.run()
