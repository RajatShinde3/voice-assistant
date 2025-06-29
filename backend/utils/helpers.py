import datetime
import json
import os
import re

LOG_FILE = "interaction_log.json"

def format_time(time_str: str) -> str:
    """
    Converts 24-hour HH:MM time to 12-hour format with AM/PM.
    Example: "18:30" -> "6:30 PM"
    """
    try:
        dt = datetime.datetime.strptime(time_str, "%H:%M")
        return dt.strftime("%I:%M %p").lstrip("0")
    except:
        return time_str

def log_interaction(user_input: str, assistant_reply: str):
    """
    Saves voice interaction to a log file.
    """
    entry = {
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "input": user_input,
        "reply": assistant_reply
    }

    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            logs = json.load(f)
    else:
        logs = []

    logs.append(entry)

    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=4)

def extract_city(command: str) -> str:
    """
    Attempts to extract city name from a sentence like:
    "What's the weather in Mumbai"
    """
    match = re.search(r"weather in ([a-zA-Z\s]+)", command.lower())
    if match:
        return match.group(1).strip()
    return "your city"

def sanitize_text(text: str) -> str:
    """
    Cleans up input text (removes weird characters, extra spaces, etc.)
    """
    return re.sub(r"\s+", " ", text).strip()
