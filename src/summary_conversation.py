# summary_conversation.py

from openai import OpenAI
from config import api_key

class InfoConversationEnglish:
    """Handles conversation summary generation, translation, and storage."""

    def __init__(self, past_interactions: str, user_name: str, api: str, language: str, interaction: str):
        self.past_interactions = past_interactions
        self.user_name = user_name
        self.client = OpenAI(api_key=api_key)  # Initialize OpenAI client with placeholder API key
        self.API = api
        self.language = language
        self.interaction = interaction

    def generate_summary(self, conversation: list):
        """Generates a summary of the current conversation in English."""
        text_english = self.language_to_english(conversation)
        prompt = self.build_summary_prompt(text_english, self.past_interactions)
        summary = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "system", "content": prompt}],
            temperature=0.9,
        )
        conversation_summary = summary.choices[0].message.content
        # Save conversation in the specified language
        text = "\n".join(conversation)
        self.saving_conversation(language=self.language, conversation_language=text)
        print(conversation_summary)
        return conversation_summary

    def language_to_english(self, text):
        """Translates the conversation text to English."""
        prompt = f"Translate this conversation to English: {text}"
        traduction = self.client.chat.completions.create(
            model="gpt-4o",
            messages=[{"role": "system", "content": prompt}],
            temperature=0.9,
            frequency_penalty=0,
            presence_penalty=0.6
        )
        conversation_english = traduction.choices[0].message.content.strip()
        self.saving_conversation(language="english", conversation_language=conversation_english)
        return conversation_english

    def build_summary_prompt(self, text_english, last_conversation):
        """Builds the prompt for generating a detailed conversation summary."""
        return (
            f"Provide a comprehensive summary of our current conversation. "
            f"The summary should include:\n"
            f"- Key points discussed\n"
            f"- Important details that emerged\n"
            f"- Relevant interests and aspects related to {self.user_name}\n"
            f"- Any action items agreed upon\n"
            f"Consider both today's conversation and prior information: {last_conversation}.\n"
            f"Here is the current conversation: {text_english}."
        )

    def format_summary(self, conversation_summary):
        """Formats the generated conversation summary with additional information."""
        conversation_summary = conversation_summary.strip()
        info = conversation_summary + f"\n" + self.get_conversation_details()
        return info

    def get_conversation_details(self):
        """Provides the date, time, and location details."""
        return (
            f" Date and Time: {self.now.strftime('%m/%d/%Y %H:%M')}\n"
            f" Location: {self.location}"
        )

    def saving_conversation(self, language: str, conversation_language: str):
        """Saves the conversation text to a file for record-keeping."""
        conversation_file = f"participants/{self.user_name}_conversation_{language}_interaction_{self.interaction}.txt"
        with open(conversation_file, "w") as archivo:
            archivo.write(conversation_language)
