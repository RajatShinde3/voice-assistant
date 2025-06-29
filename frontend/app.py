import streamlit as st
import requests

st.set_page_config(page_title="Voice Assistant", layout="centered")
st.markdown('<style>' + open("frontend/assets/style.css").read() + '</style>', unsafe_allow_html=True)

st.title("🎙️ Voice Assistant")
st.subheader("Your Glassy Smart Assistant Powered by Python")

tab1, tab2, tab3, tab4 = st.tabs(["📢 Text Command", "⏰ Reminder", "📨 Email", "🌦️ Weather"])

with tab1:
    st.markdown("### Type a Command")
    user_input = st.text_input("Example: 'Send email to abc@gmail.com saying hello there'")
    if st.button("Run Command"):
        if user_input:
            response = requests.get(f"http://localhost:8000/text/{user_input}")
            st.success(f"🔊 {response.json()['response']}")
        else:
            st.warning("Please enter a command.")

with tab2:
    st.markdown("### Set a Reminder")
    reminder_time = st.text_input("Time (e.g., 10:30 AM)")
    reminder_msg = st.text_input("Reminder Message")
    if st.button("Set Reminder"):
        res = requests.get(f"http://localhost:8000/reminder", params={"time": reminder_time, "message": reminder_msg})
        st.success(res.json())

    if st.button("View All Reminders"):
        res = requests.get("http://localhost:8000/reminders")
        st.json(res.json())

with tab3:
    st.markdown("### Send Email")
    to = st.text_input("Recipient Email")
    subject = st.text_input("Subject")
    body = st.text_area("Message")
    if st.button("Send Email"):
        payload = {"recipient": to, "subject": subject, "body": body}
        res = requests.post("http://localhost:8000/send-email", json=payload)
        st.success(res.json())

with tab4:
    st.markdown("### Get Weather Report")
    location = st.text_input("Enter City or Location")
    if st.button("Get Weather"):
        res = requests.get(f"http://localhost:8000/weather", params={"location": location})
        st.json(res.json())
