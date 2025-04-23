import os
import json
from dotenv import load_dotenv
import google.generativeai as genai
from text_to_speech import set_voice_tone
from memory import store_memory, get_memory
from cache import save_to_cache

# Load API keys from AppData or .env
env_path = os.path.expanduser("~\\AppData\\Roaming\\Nox\\.env")
load_dotenv(dotenv_path=env_path)

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-pro-latest")

# Default casual personality
system_persona = """
You are Nox, a casual and laid-back voice assistant. 
Be helpful, friendly, and speak like a human friend. 
Keep answers short and natural. Never say you're an AI, Gemini, or made by Google.
"""

def detect_if_mode_change(prompt):
    """Use Gemini to detect personality change request."""
    try:
        response = model.generate_content(f"""
You are a classifier for a voice assistant named Nox.
Classify this input as either "mode-change" or "normal".

User: "{prompt}"
        """)
        result = response.text.strip().lower()
        return result == "mode-change"
    except Exception as e:
        print("⚠️ Error in intent classification:", e)
        return False

def handle_memory_request(prompt):
    """Handle memory-based instructions like storing or recalling the user's name."""
    prompt = prompt.lower()

    if "remember" in prompt and "my name is" in prompt:
        name = prompt.split("my name is")[-1].strip().strip(".")
        store_memory("name", name)
        return f"Got it. I'll remember your name is {name}."

    elif "what's my name" in prompt or "what is my name" in prompt:
        name = get_memory("name")
        if name:
            return f"You told me your name is {name}."
        else:
            return "I don't know your name yet. Tell me and I’ll remember!"

    return None

def get_ai_response(prompt):
    """Get AI response from Gemini. Handles memory, mode, and caching."""
    global system_persona

    # Step 1: Handle memory
    mem_response = handle_memory_request(prompt)
    if mem_response:
        save_to_cache(prompt, mem_response)
        return mem_response

    # Step 2: Handle personality change
    if detect_if_mode_change(prompt):
        print("🔄 Gemini thinks you're changing Nox's personality...")
        try:
            response = model.generate_content(f"""
You are Nox. Based on this instruction: "{prompt}", generate a short vivid personality description.

Do NOT mention Gemini, Google, or being an AI.
            """)
            persona = response.text.strip()
            system_persona = persona
            set_voice_tone(system_persona)
            save_to_cache(prompt, persona)
            print("✅ Nox's personality updated.")
            return "Alright, I’ve switched my vibe. Let’s go!"
        except Exception as e:
            print(f"⚠️ Error updating personality: {e}")
            return "Sorry, I couldn’t change my vibe right now."

    # Step 3: Normal conversation
    try:
        print("🤖 Nox is thinking...")
        response = model.generate_content([
            {"role": "user", "parts": [system_persona + "\nUser: " + prompt]}
        ])
        reply = response.text.strip()
        save_to_cache(prompt, reply)
        return reply

    except Exception as e:
        print(f"⚠️ Gemini Error: {e}")
        return "Sorry, I couldn't process that."

def get_command_from_gemini(prompt):
    """Convert prompt into system action using Gemini. Returns dict or None."""
    try:
        print("🧠 Interpreting as system command...")
        response = model.generate_content(f"""
You are a system-level assistant named Nox. Convert this user input into a JSON object to trigger system actions.

Examples:
"Open Notepad" → {{"action": "launch_app", "app": "notepad"}}
"Search for cats" → {{"action": "open_url", "url": "https://www.google.com/search?q=cats"}}
"Take a screenshot" → {{"action": "screenshot"}}
"Shutdown" → {{"action": "shutdown"}}
"Tell me the time" → {{"action": "get_time"}}

Respond ONLY with a raw JSON object. Do NOT include explanation, code formatting, or extra text.

User: "{prompt}"
        """)
        reply_text = response.text.strip()
        save_to_cache(prompt, reply_text)
        return json.loads(reply_text)

    except json.JSONDecodeError:
        print("⚠️ Gemini returned invalid JSON. Falling back to chat mode.")
        return None

    except Exception as e:
        print(f"⚠️ Command parsing failed: {e}")
        return None
