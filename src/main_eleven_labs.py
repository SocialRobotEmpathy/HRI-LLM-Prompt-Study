# main_eleven_labs.py

from pepper.pepper_connection import PepperConnection
from user.background_knowledge import UserInfo
from pepper.prompt_manager import PromptManager
from pepper.dialog import OngoingDialogManager
from pepper.stt import SpeechToText
from curando.pepper.llm_eleven_labs import LargeLanguageModel
import threading as th

conversation_going = True

def key_capture_thread():
    """Allows the conversation to be stopped by user input."""
    global conversation_going
    input()
    conversation_going = False

def main():
    """Main function to initiate and manage conversation with Pepper."""
    API = "gpt-4o"  # Simplified API model configuration
    pepper_connection = PepperConnection(port=5002)
    user = UserInfo()  # Load user information
    user_info = user.load_user_information()
    
    # Set up prompt manager and dialog manager
    prompt_manager = PromptManager(location="x", user_info=user_info["user_info"],
                                   past_interactions=user_info["past_interactions"], user_name=user_info["name"], language=user_info["language"])
    dialog_manager = OngoingDialogManager(prompt_manager.main_prompt, user_name=user_info["name"])
    llm_OpenAI = LargeLanguageModel(API=API, language=user_info["language"])
    speech_to_text = SpeechToText(region="eastus", language=user_info["language_id"], llm=llm_OpenAI,
                                  dialog=dialog_manager)

    # Start a thread to capture exit input
    key_capture = th.Thread(target=key_capture_thread, args=(), name='key_capture_thread', daemon=True)
    key_capture.start()

    try:
        while conversation_going:
            pepper_is_talking = pepper_connection.recv_message()
            if pepper_is_talking == "listening":
                recognized_speech, response_stream = speech_to_text.speech_recognize_continuous_from_microphone()
                llm_response = llm_OpenAI.do_everything_else(user_message=recognized_speech, response_stream=response_stream,
                                                             dialog=dialog_manager, pepper_connection= pepper_connection)
                dialog_manager.conversation(user_utterance=recognized_speech, pepper_response=llm_response)
                pepper_connection.send_message("_done")

        key_capture.join()
        pepper_connection.send_message("_final")
        pepper_connection.close_socket()
    except KeyboardInterrupt:
        print("Ctrl+C detected. Exiting...")
    finally:
        summary = summary_conversation.generate_summary(dialog_manager.get_conversation())
        user.update_user_information(summary=summary)
        print("Conversation ended.")

if __name__ == "__main__":
    main()
