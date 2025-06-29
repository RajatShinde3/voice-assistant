from dotenv import load_dotenv
import os
import smtplib
import re
from email.mime.text import MIMEText

# Load environment variables from .env file
load_dotenv()

EMAIL_ADDRESS = os.getenv("SENDER_EMAIL")
EMAIL_PASSWORD = os.getenv("SENDER_PASSWORD")

def send_email(to: str, subject: str, body: str) -> dict:
    try:
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = to

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, to, msg.as_string())

        return {"status": "Email sent successfully"}
    except Exception as e:
        return {"error": str(e)}

def parse_email_command(command: str) -> dict:
    try:
        pattern = r"send email to ([\w\.-]+@[\w\.-]+) saying (.+)"
        match = re.search(pattern, command.lower())

        if not match:
            return {"error": "Sorry, I couldn't understand your email command."}

        to_email = match.group(1)
        body = match.group(2).strip().capitalize()
        subject = "Voice Assistant Message"

        return send_email(to_email, subject, body)

    except Exception as e:
        return {"error": f"Error parsing email: {str(e)}"}
