from flask import Flask, abort, render_template
from flask_cors import CORS
import yaml
import fcntl

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    if not is_active():
        abort(404)
    return render_template("index.html")


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
