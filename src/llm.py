# llm.py

from openai import OpenAI
from pepper.dialog import OngoingDialogManager
from pepper.tts_eleven_labs import text_to_speech_file
import re

class LargeLanguageModel:
    """Facilitates interaction with a large language model (LLM) to generate responses for Pepper."""
    
    def __init__(self, API: str, language: str, max_response_length=150):
        self.client = OpenAI(api_key="API_KEY")  # Placeholder for OpenAI API key
        self.API = API
        self.max_response_length = max_response_length
        self.language = language

    def llm_openAI(self, user_message: str, dialog: OngoingDialogManager) -> str:
        """Generates a response from the LLM and processes it into sentences."""
        pepper_response = ""
        buffer = ""
        user = {
            "role": "user",
            "content": f"{user_message}. REMINDER: You are acting as the social robot Pepper, you cannot see or walk. Keep your responses with empathy, brief and friendly. Ask open questions to keep the conversation engaging and show interest like a empathic human be will do."
        }
        dialog.add_user_message(user)
        response = self.client.chat.completions.create(
            model=self.API,
            messages=dialog.get_ongoing_dialog,
            max_tokens=self.max_response_length,
            temperature=0.7,
            stream=True
        )

        for event in response:
            event_text = event.choices[0].delta
            if event_text.content:
                buffer += event_text.content
                pepper_response += event_text.content

        pepper_message = {"role": "assistant", "content": pepper_response}
        dialog.add_pepper_message(pepper_message)
        return pepper_response
