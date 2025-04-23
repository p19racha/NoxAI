import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Default tone settings
tone_settings = {
    "rate": 175,   # Speech speed (default casual)
    "volume": 1.0, # Max volume
    "voice": None  # System default voice
}

def set_voice_tone(persona_description):
    """
    Adjust voice tone (rate, optionally volume/voice) based on personality description.
    Called when Nox switches modes.
    """
    global tone_settings

    description = persona_description.lower()

    # Adjust speaking rate based on tone keywords
    if "sarcastic" in description:
        tone_settings["rate"] = 150
    elif "professional" in description or "efficient" in description:
        tone_settings["rate"] = 195
    elif "funny" in description or "witty" in description:
        tone_settings["rate"] = 180
    elif "chill" in description or "relaxed" in description:
        tone_settings["rate"] = 145
    elif "pirate" in description:
        tone_settings["rate"] = 155
    else:
        tone_settings["rate"] = 175  # Default casual

    # Apply new settings to the engine
    engine.setProperty('rate', tone_settings["rate"])
    engine.setProperty('volume', tone_settings["volume"])

    # Optionally handle voice selection here in the future
    # engine.setProperty('voice', tone_settings["voice"])

    print(f"🎛 Voice tone set to: {tone_settings['rate']} WPM (based on persona)")

def speak(text):
    """Speak the given text using current tone settings."""
    print(f"🗣️ Nox says: {text}")
    engine.say(text)
    engine.runAndWait()
