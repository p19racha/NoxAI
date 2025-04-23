from wake_word import wait_for_wake_word
from speech_to_text import record_and_transcribe
from ai_engine import get_ai_response, get_command_from_gemini
from system_controller import run_command
from text_to_speech import speak

def main():
    print("🚀 Nox is ready. Say 'Hey Nox' to wake me up!")

    while True:
        try:
            wait_for_wake_word()
            query = record_and_transcribe(duration=6)

            # Ask Gemini for system command
            command_json = get_command_from_gemini(query)
            if command_json:
                result = run_command(command_json)
                if result:
                    speak(result)
                    continue

            # Fallback: use Gemini as a chatbot
            response = get_ai_response(query)
            speak(response)

        except KeyboardInterrupt:
            print("\n👋 Session ended by user. Goodbye!")
            break
        except Exception as e:
            print(f"⚠️ Unexpected error: {e}")
            speak("Sorry, something went wrong.")

if __name__ == "__main__":
    main()
