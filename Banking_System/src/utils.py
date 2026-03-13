import os
import json
import logging

# Load config
with open("../config/config.json", "r") as f:
    config = json.load(f)

# Ensure logs folder exists
os.makedirs(os.path.dirname(config["log_file"]), exist_ok=True)

# Setup logging
logging.basicConfig(
    filename=config["log_file"],
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def id_exists(user_id):
    try:
        with open(config["user_file"], "r") as f:
            for line in f:
                data = eval(line.strip())
                if data[0] == user_id:
                    return True
    except FileNotFoundError:
        return False
    return False

def read_users():
    users = []
    try:
        with open(config["user_file"], "r") as f:
            for line in f:
                if line.strip():
                    users.append(eval(line.strip()))
    except FileNotFoundError:
        pass
    return users

def write_users(users):
    with open(config["user_file"], "w") as f:
        for user in users:
            f.write(str(user) + "\n")