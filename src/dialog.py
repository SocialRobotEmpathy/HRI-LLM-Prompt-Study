# dialog.py

from typing import List, Dict

class OngoingDialogManager:
    """Manages ongoing conversation history between user and Pepper."""
    
    def __init__(self, main_prompt: Dict[str, str], user_name: str):
        self.ongoing_dialog = [main_prompt]  # Initializes with the main prompt
        self.user_name = user_name
        self.ongoing_conversation = []

    def add_pepper_message(self, pepper: Dict[str, str]) -> None:
        """Adds Pepper's response to the conversation history."""
        self.ongoing_dialog.append(pepper)

    def add_user_message(self, user: Dict[str, str]) -> None:
        """Adds the user's input to the conversation history."""
        self.ongoing_dialog.append(user)

    def conversation(self, user_utterance: str, pepper_response: str) -> None:
        """Records each turn in the ongoing conversation."""
        self.ongoing_conversation.append(f"{self.user_name}: {user_utterance}")
        self.ongoing_conversation.append(f"Pepper: {pepper_response}")

    def get_conversation(self) -> List[str]:
        """Returns the full conversation history."""
        return self.ongoing_conversation
