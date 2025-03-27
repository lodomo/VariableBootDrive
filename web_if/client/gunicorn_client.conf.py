import yaml
YAML_FILE = "settings.yaml"
SETTINGS = {}

with open(YAML_FILE, "r") as file:
    SETTINGS = yaml.safe_load(file)["web_if"]["client"]

port = SETTINGS["port"]
bind = f"0.0.0.0:{port}"
workers = int(SETTINGS["workers"])
threads = int(SETTINGS["threads"])
worker_class = SETTINGS["worker_class"]
timeout = int(SETTINGS["timeout"])
keepalive = int(SETTINGS["keepalive"])
max_requests = int(SETTINGS["max_requests"])
max_requests_jitter = int(SETTINGS["max_requests_jitter"])

def on_starting(server):
    initialize()

def on_reload(server):
    initialize()

def initialize():
    pass
