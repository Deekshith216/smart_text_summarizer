**SMART TEXT SUMMARIZER**
An AI-powered Smart Text Summarizer built using Python, OpenAI API, and Streamlit.
This project summarizes long text into clear and concise outputs using structured prompting and a clean, extensible architecture.

**FEATURES**
Summarize long text instantly
Multiple summary formats:
Short Summary
Bullet Points
Key Takeaways
Uses structured prompts for consistent results
Clean backend architecture
Streamlit-based web user interface
Secure API key handling using environment variables

**HOW IT WORKS (SIMPLE EXPLANATION)**
User enters long text in the application
User selects the type of summary
The text is sent to the AI model using a structured prompt
The AI generates a concise summary
The summary is displayed on the screen

**PROJECT ARCHITECTURE**

User (Browser)
↓
Streamlit UI
↓
Summarizer Interface
↓
OpenAI Summarizer
↓
Structured Prompt
↓
AI-generated Summary

The UI and summarization logic are separated, making the project easy to maintain and extend.

**PROJECT STRUCTURE**
smart-text-summarizer/
app.py
CLI-based summarizer

streamlit_app.py
Streamlit web UI

requirements.txt
Project dependencies

.gitignore
Ignored files

summarizer/
base.py
Defines summarizer interface

openai_summarizer.py
OpenAI implementation

prompt_templates.py
Structured prompts

README.md / README.txt

**TECHNOLOGIES USED**
Python 3
OpenAI API
Streamlit
Object-Oriented Programming
Structured Prompt Engineering
API KEY SETUP (IMPORTANT)
This project uses environment variables to store the OpenAI API key securely.

Windows (PowerShell):

$Env:OPENAI_API_KEY="your_openai_api_key_here"

Never hardcode API keys in source code.

HOW TO RUN THE PROJECT

Clone the repository

git clone https://github.com/your-username/smart-text-summarizer.git

cd smart-text-summarizer

Create and activate virtual environment

python -m venv venv
venv\Scripts\activate

Install dependencies

pip install -r requirements.txt

Run the Streamlit app

streamlit run streamlit_app.py

The application will open automatically in your browser.
