# backend/reminder_module.py

import datetime

# In-memory storage for reminders
reminders = []

def set_reminder(time: str, message: str) -> dict:
    """
    Set a reminder with a specified time and message.

    :param time: Reminder time in "YYYY-MM-DD HH:MM" format.
    :param message: Reminder message.
    :return: Success or error status with a message.
    """
    try:
        reminder_time = datetime.datetime.strptime(time, "%Y-%m-%d %H:%M")
        reminders.append({
            "time": reminder_time,
            "message": message
        })
        return {
            "status": "success",
            "message": f"Reminder set for {reminder_time.strftime('%Y-%m-%d %H:%M')}"
        }
    except ValueError:
        return {
            "status": "error",
            "message": "Invalid time format. Use YYYY-MM-DD HH:MM"
        }

def get_all_reminders() -> list:
    """
    Retrieve all stored reminders.

    :return: List of reminders with time and message.
    """
    # Optionally sort reminders by time
    sorted_reminders = sorted(reminders, key=lambda r: r["time"])
    return [{
        "time": r["time"].strftime("%Y-%m-%d %H:%M"),
        "message": r["message"]
    } for r in sorted_reminders]

# backend/reminder_module.py

def parse_reminder_command(command: str):
    """
    Dummy function to parse reminder commands like 'Remind me to call mom at 6 PM'
    Returns (time_str, message)
    """
    if "at" in command:
        parts = command.split("at")
        message = parts[0].replace("remind me to", "").strip()
        time = parts[1].strip()
        return time, message
    return None, None
