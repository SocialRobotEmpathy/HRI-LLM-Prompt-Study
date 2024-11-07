# prompt_manager.py

from datetime import datetime
import pytz

class PromptManager:
    """Manages prompt creation and customization based on user info and past interactions."""
    
    def __init__(self, location: str, user_info: str, past_interactions: str, user_name: str) -> object:
        # Initialize with user-specific information for prompt personalization
        self.main_prompt = self.get_base_prompt(location=location, user_info=user_info, 
                                                past_interactions=past_interactions, user_name=user_name)

    def get_base_prompt(self, location: str, user_info: str, user_name: str, past_interactions: str, language: str):
        """Generates the base prompt based on location, user info, and past conversations."""
        now = datetime.now(pytz.timezone('Europe/Brussels'))
        return {
            "role": "system",
            "content": f"You are Pepper, a social robot. Your friend, {user_name}, speaks {language}. "
                       f"Here’s what you know about them: {user_info}. Past interactions include: {past_interactions}. "
                       f"The current date and time is {now.strftime('%m/%d/%Y %H:%M')} in {location}."
                       f" Your goal is to engage warmly and empathetically with {user_name}."
        }
