# Voice-Controlled Assistant

## Description
This is a Python-based voice-controlled virtual assistant that can perform basic interactions, open websites, and answer queries using speech recognition and text-to-speech functionalities. It leverages Google Speech Recognition and text-to-speech via `pyttsx3`, integrates OpenAI's GPT models, and uses Wolfram Alpha for computational queries. It provides interactive, natural responses and randomized greetings.

## Features
- Speech recognition using Google API
- Text-to-speech functionality using pyttsx3
- Open popular websites (Instagram, Twitter, Facebook, Wikipedia, Google)
- Query resolution using Wolfram Alpha
- Intelligent fallback answers using OpenAI's GPT model
- Interactive and randomized greetings

## Requirements
- Python 3.x
- SpeechRecognition
- pyttsx3
- OpenAI API
- Wolfram Alpha API

Install necessary packages using:

```bash
pip install speechrecognition pyttsx3 wolframalpha openai webbrowser
```

## Setup

### API Keys
Replace placeholders in your script with your API keys:
- Wolfram Alpha (`appId ='YOUR_WOLFRAM_APP_ID'`)
- OpenAI (`openai.api_key = 'YOUR_OPENAI_API_KEY'`)

### Microphone Configuration
Adjust microphone configuration to match your system settings:

```python
mic_name = "Your microphone's exact name"
```

## Running the Assistant
Execute your script to start the assistant:
```bash
python main.py
```

## Project Configuration

```
project-root/
│
├── README.md
└── Modules/
    │
    ├── main.py
    ├── assistant.py
    ├── web_utils.py
    ├── speech_utils.py
    ├── wolfram_utils.py
    └── constants.py
```

### Example Commands
- **Greet:** "Hello", "Hey"
- **Open Websites:** "Open Google", "Open Instagram"
- **Queries:** "Define photosynthesis", "What is the capital of Spain?"

## Troubleshooting
- **Microphone Detection:** Ensure correct microphone device is set.
- **Wolfram/OpenAI Errors:** Double-check API keys.

## Dependencies
Install dependencies using:
```bash
pip install speechrecognition pyttsx3 wolframalpha openai
```


<div align="center">

<a href="https://jeevasaravanan.medium.com/" target="_blank">![Medium](https://img.shields.io/badge/Medium-000000?style=for-the-badge&logo=medium&logoColor=white)</a> <a href="https://www.linkedin.com/in/jeeva-saravanan/" target="_blank">![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)</a> <a href="https://jeeva-saravana-bhavanandam.web.app" target="_blank">![Portfolio](https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=GoogleChrome&logoColor=white)</a>


</div>