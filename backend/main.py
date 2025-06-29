from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from backend.speech_handler import listen, speak
from backend.nlp_handler import handle_command
from backend.actions.weather import get_weather
from backend.email_module import send_email
from backend.reminder_module import set_reminder, get_all_reminders


app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Voice Assistant API is running."}

@app.get("/voice")
def voice_command():
    query = listen()
    response = handle_command(query)
    speak(response)
    return {"query": query, "response": response}

@app.get("/text/{query}")
def text_command(query: str):
    response = handle_command(query)
    return {"query": query, "response": response}

@app.get("/reminder")
def set_reminder_endpoint(time: str, message: str):
    return set_reminder(time, message)

@app.get("/reminders")
def get_reminders_endpoint():
    return get_all_reminders()



@app.post("/send-email")
async def email_sender(request: Request):
    try:
        data = await request.json()
    except Exception as e:
        return {"error": f"Invalid JSON body: {str(e)}"}

    recipient = data.get("recipient")
    subject = data.get("subject")
    body = data.get("body")

    if not recipient or not subject or not body:
        return {"error": "Missing recipient, subject, or body."}

    result = send_email(recipient, subject, body)
    return result



@app.get("/weather")
def get_weather_endpoint(location: str):
    """
    Get weather info for a location.
    Example: /weather?location=Pune
    """
    result = get_weather(location)
    return {"location": location, "forecast": result}