import json
from .main import Log

LOG_FILE = "logs.json"
logs = []

def load_logs():
    global logs
    try:
        with open(LOG_FILE, "r") as file:
            logs_data = json.load(file)
            logs = [Log(**entry) for entry in logs_data]
    except FileNotFoundError:
        logs = []

def save_log(log):
    logs.append(log)
    with open(LOG_FILE, "w") as file:
        json.dump([l.dict() for l in logs], file, indent=4)

load_logs()
