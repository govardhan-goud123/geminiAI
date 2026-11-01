<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:101426,50:493b79,100:202b55&height=220&section=header&text=Gemini%20AI%20Assistant&fontSize=42&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=AI-Powered%20Conversational%20Chatbot&descAlignY=58&descSize=18" width="100%"/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&duration=3000&pause=1000&color=9D8CFF&center=true&vCenter=true&width=650&lines=Powered+by+Google+Gemini;Built+with+Python+%26+Streamlit;Interactive+AI+Chat+Experience;Simple.+Fast.+Intelligent." alt="Typing SVG" />

<br>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge\&logo=streamlit\&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge\&logo=googlegemini\&logoColor=white)
![HTML](https://img.shields.io/badge/HTML-E34F26?style=for-the-badge\&logo=html5\&logoColor=white)
![CSS](https://img.shields.io/badge/CSS-1572B6?style=for-the-badge\&logo=css3\&logoColor=white)

</div>

---

## About The Project

**Gemini AI Assistant** is an interactive AI chatbot developed using Python, Streamlit, and Google's Gemini API.

The application allows users to ask questions and receive intelligent AI-generated responses through a clean, modern chat interface.

It uses the Google GenAI Python SDK and Gemini 3.6 Flash model to process user prompts and generate responses.

The interface includes custom CSS styling, chat bubbles, loading animations, and session-based chat history.

## Features

* **AI-Powered Responses:** Generate intelligent responses using Google Gemini.
* **Interactive Chat Interface:** Chat with Gemini through Streamlit.
* **Chat History:** Display previous messages during the current application session.
* **Modern UI:** Custom dark-themed interface with gradient styling.
* **Loading Animation:** Visual feedback while Gemini generates responses.
* **Real-Time Interaction:** Submit prompts and display generated answers.
* **Error Handling:** Display API errors without crashing the application.
* **Simple Architecture:** Lightweight Python implementation.

## Technology Stack

| Technology              | Purpose                                    |
| ----------------------- | ------------------------------------------ |
| Python                  | Core programming language                  |
| Streamlit               | Web application and chat interface         |
| Google GenAI SDK        | Connects Python with Google's AI models    |
| Gemini 3.6 Flash        | AI response generation                     |
| HTML                    | Custom header structure                    |
| CSS                     | Dark theme, gradients, and UI styling      |
| Streamlit Session State | Maintains chat messages during the session |
| Gemini Interactions API | Sends prompts and receives AI responses    |

## Application Architecture

```text
              USER
                |
                v
       STREAMLIT CHAT UI
                |
                v
          USER PROMPT
                |
                v
        GOOGLE GENAI SDK
                |
                v
       GEMINI 3.6 FLASH
                |
                v
        AI RESPONSE
                |
                v
       STREAMLIT CHAT UI
                |
                v
          USER OUTPUT
```

## Project Structure

```text
Gemini-AI-Assistant/
│
├── geminiAI.py
│
├── requirements.txt
│
├── README.md
│
└── .gitignore
```

## Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_REPOSITORY_URL
```

### 2. Navigate to the Project

```bash
cd Gemini-AI-Assistant
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate Virtual Environment

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure Gemini API Key

Get an API key from Google AI Studio.

PowerShell:

```powershell
$env:GEMINI_API_KEY = "YOUR_API_KEY"
```

Keep your API key private. Never upload it to GitHub.

### 7. Run the Application

```bash
python -m streamlit run geminiAI.py
```

Open your browser:

```text
http://localhost:8501
```

## Requirements

Create a `requirements.txt` file:

```text
streamlit
google-genai
```

## User Interface

The application features:

* Dark navy background.
* Purple gradient header.
* Custom Gemini AI branding.
* Interactive chat interface.
* User and assistant message separation.
* Loading indicator during response generation.

## Core Implementation

The application uses Google's GenAI client:

```python
from google import genai

client = genai.Client()

interaction = client.interactions.create(
    model="gemini-3.6-flash",
    input=prompt
)

answer = interaction.output_text
```

The generated response is displayed using Streamlit.

## Future Enhancements

* Conversation memory using previous interaction IDs.
* Chat export functionality.
* Multiple Gemini model selection.
* Voice input and output.
* Image understanding.
* File upload and document analysis.
* Custom AI assistant personalities.
* Chat reset and conversation management.

## Developer Skills Demonstrated

* Python Programming
* Generative AI
* Large Language Models (LLMs)
* Google Gemini API Integration
* Prompt Engineering
* Streamlit Application Development
* API Integration
* HTML and CSS Customization
* Session State Management
* Exception Handling

---

<div align="center">

### Built with Python and Google Gemini

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:202b55,50:493b79,100:101426&height=120&section=footer&animation=fadeIn" width="100%"/>

**Exploring the possibilities of Generative AI.**

</div>
