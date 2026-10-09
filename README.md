
# 📅 Deadline Tracker

An AI-powered student assistant that extracts important deadlines from syllabus documents, timetables, assignment sheets, and text using Google's Gemini AI.

## ✨ Features

- 📄 **Deadline Extraction** — Identify assignments, exams, due dates, times, and instructions.
- 🖼️ **Image Analysis** — Upload JPG or PNG images of academic documents.
- 🤖 **AI-Powered Analysis** — Uses Gemini AI to extract and organize deadline information.
- 📧 **Email Summary** — Send extracted deadlines to your email.
- 🎓 **Student-Friendly Interface** — Simple and easy-to-use web application.

## 🛠️ Tech Stack

- Python
- Streamlit
- Google Gemini API
- Gmail SMTP

## 📁 Project Structure

```text
deadline-tracker/
├── app.py
├── prompts.py
├── requirements.txt
├── .gitignore
└── .streamlit/
    ├── secrets.toml
    └── secrets.toml.example
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd deadline-tracker
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API credentials

Create `.streamlit/secrets.toml` using `.streamlit/secrets.toml.example` as a reference.

Add your credentials:

```toml
GEMINI_API_KEY = "your-gemini-api-key"
GMAIL_ADDRESS = "your-email@gmail.com"
GMAIL_APP_PASSWORD = "your-gmail-app-password"
```

Get your Gemini API key from [Google AI Studio](https://aistudio.google.com/).

For Gmail, enable 2-Step Verification and create an App Password from [Google Account Security](https://myaccount.google.com/apppasswords).

**Important:** Never commit your actual API keys or passwords to GitHub.

### 5. Run the application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal, usually `http://localhost:8501`.

## 🚀 How to Use

1. Enter your name and email address.
2. Upload a syllabus or assignment image, or paste academic text.
3. Click **Extract Deadlines**.
4. Review the extracted tasks, dates, and instructions.
5. Click **Email My Deadlines** to receive a summary.

## 🌐 Deployment

Deploy the application using [Streamlit Community Cloud](https://share.streamlit.io/).

1. Push your project to GitHub.
2. Create a new app in Streamlit Community Cloud.
3. Select your repository and `app.py`.
## 4. Add your credentials under the app's Secrets settings.
5. Deploy and test your application.

## 🔒 Security

- Keep `.streamlit/secrets.toml` private.
- Commit only `.streamlit/secrets.toml.example` with placeholder values.
- Never expose API keys or Gmail App Passwords in source code.

## ⚠️ Limitations

- Extracted dates may require manual verification.
- The current version sends email summaries but does not schedule automatic future reminders.
- Deadlines are not permanently stored in a database.

## 🎯 Future Enhancements

- Calendar integration
- Automatic deadline reminders
- Task prioritization
- Persistent deadline storage
- Search and filter deadlines

## 👩‍💻 Author

**Sinaz Afrin**

Built with Python, Streamlit, and Google Gemini AI.
