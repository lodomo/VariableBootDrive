import fcntl

import yaml
from flask import Flask, abort, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    if not is_active():
        abort(404)
    return render_template("index.html")

    """
    Methods:
    - mount [path]
    - unmount
    - flash_mode_on
    - flash_mode_off
    - sign_in [password]
    - change_password [old_password] [new_password]
    - web_interface_on
    - web_interface_off
    - update
    - info
    """


@app.route("/sign_in")


def is_active():
    yaml_file = "settings.yaml"
    with open(yaml_file, "r") as file:
        # Shared lock (blocks write access)
        fcntl.flock(file, fcntl.LOCK_SH)
        settings = yaml.safe_load(file)
        fcntl.flock(file, fcntl.LOCK_UN)
    return settings["web_if"]["client"]["active"]


if __name__ == "__main__":
    app.run()
