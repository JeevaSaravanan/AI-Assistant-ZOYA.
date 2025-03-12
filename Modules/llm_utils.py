# llm_utils.py

import openai
from constants import OPENAI_API_KEY
from speech_utils import speak

openai.api_key = OPENAI_API_KEY

def ask_llm(prompt, model="gpt-3.5-turbo"):
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.6,
            max_tokens=150
        )
        answer = response.choices[0].message['content'].strip()
        speak(answer)
        return answer
    except Exception as e:
        speak("I'm having trouble connecting to the language model.")
        return None
