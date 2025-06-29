import datetime
from backend.actions.weather import get_weather
from backend.reminder_module import parse_reminder_command
from backend.email_module import parse_email_command
from backend.wiki_module import wiki_answer
from backend.utils.helpers import extract_city, sanitize_text

def handle_command(command: str) -> str:
    """
    Processes user voice input and returns a spoken text response.
    This is the brain of the assistant.
    """
    command = sanitize_text(command.lower())

    # 1. Greeting
    if any(greet in command for greet in ["hello", "hi", "hey"]):
        return "Hi there! I'm Voxa, your voice assistant. How can I help you today?"

    # 2. Time
    elif "time" in command:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}."

    # 3. Date
    elif "date" in command:
        current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
        return f"Today's date is {current_date}."

    # 4. Dynamic Weather
    elif "weather" in command:
        city = extract_city(command)
        return get_weather(city)

    # 5. Set a Reminder
    elif "remind me" in command:
        return parse_reminder_command(command)

    # 6. Send Email
    elif "send email" in command:
        return parse_email_command(command)

    # 7. Search keyword trigger (frontend handles actual search)
    elif "search" in command:
        return "Opening a web search for you."

    # 8. Fallback to Wikipedia for general Q&A
    else:
        return wiki_answer(command)
