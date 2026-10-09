import smtplib
from email.mime.text import MIMEText

import streamlit as st
from google import genai
from google.genai import types

from prompts import (
    SYSTEM_PROMPT,
    WELCOME_MESSAGE_TEMPLATE,
    SUMMARY_REQUEST_PROMPT,
)

MODEL_NAME = "gemini-2.5-flash"

st.set_page_config(
    page_title="Deadline Tracker",
    page_icon="📅",
)

GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]
GMAIL_ADDRESS = st.secrets["GMAIL_ADDRESS"]
GMAIL_APP_PASSWORD = st.secrets["GMAIL_APP_PASSWORD"]


@st.cache_resource
def get_gemini_client():
    return genai.Client(api_key=GEMINI_API_KEY)


client = get_gemini_client()


def analyze_deadlines(text, uploaded_file=None):
    prompt = SYSTEM_PROMPT + "\n\nAnalyze this input:\n" + text
    contents = [prompt]

    if uploaded_file is not None:
        image_part = types.Part.from_bytes(
            data=uploaded_file.getvalue(),
            mime_type=uploaded_file.type,
        )
        contents.append(image_part)

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=contents,
    )

    return response.text or "No deadlines were identified."


def send_email(to_email, subject, body):
    message = MIMEText(body)
    message["Subject"] = subject
    message["From"] = GMAIL_ADDRESS
    message["To"] = to_email

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(GMAIL_ADDRESS, GMAIL_APP_PASSWORD)
        server.send_message(message)


# Onboarding
if "student_name" not in st.session_state:
    st.title("📅 Deadline Tracker")
    st.caption("Never miss an assignment deadline again!")

    with st.form("student_form"):
        name = st.text_input("Your name")
        email = st.text_input("Your email address")
        submitted = st.form_submit_button("Get Started")

    if submitted:
        if name.strip() and email.strip():
            st.session_state.student_name = name.strip()
            st.session_state.student_email = email.strip()
            st.rerun()
        else:
            st.warning("Please enter your name and email.")

    st.stop()


# Main application
st.title("📅 Deadline Tracker")

st.write(
    WELCOME_MESSAGE_TEMPLATE.format(
        name=st.session_state.student_name
    )
)

st.caption(
    f"Student: {st.session_state.student_name} | "
    f"Email: {st.session_state.student_email}"
)

uploaded_file = st.file_uploader(
    "Upload a syllabus or assignment sheet",
    type=["jpg", "jpeg", "png"],
)

text = st.text_area(
    "Or paste your syllabus / assignment details",
    placeholder="Example: Python assignment due on 20 October 2026",
)

if st.button("🔍 Extract Deadlines"):
    if not uploaded_file and not text.strip():
        st.warning("Upload an image or enter some text.")
    else:
        try:
            with st.spinner("Finding deadlines..."):
                result = analyze_deadlines(text, uploaded_file)

            st.session_state.deadline_result = result
            st.success("Deadline analysis completed!")

        except Exception as error:
            st.error(f"Analysis failed: {error}")


# Show extracted deadlines
if "deadline_result" in st.session_state:
    st.subheader("📋 Extracted Deadlines")
    st.write(st.session_state.deadline_result)

    if st.button("📧 Email My Deadlines"):
        try:
            with st.spinner("Sending email..."):
                summary = client.models.generate_content(
                    model=MODEL_NAME,
                    contents=[
                        SYSTEM_PROMPT,
                        SUMMARY_REQUEST_PROMPT,
                        st.session_state.deadline_result,
                    ],
                ).text

                send_email(
                    st.session_state.student_email,
                    "Your Deadline Tracker Summary",
                    summary or st.session_state.deadline_result,
                )

            st.success("Email sent! Check your inbox.")

        except Exception as error:
            st.error(f"Email failed: {error}")