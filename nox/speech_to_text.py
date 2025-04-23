import os
import time
import wave
import pyaudio
import numpy as np
import scipy.io.wavfile as wav
import whisper
import tempfile

# Load Whisper model (you can switch to 'large' for even better accuracy)
model = whisper.load_model("medium")

def record_audio(filename="temp_command.wav", duration=6, rate=16000):
    """Record and normalize audio using PyAudio, save as WAV."""
    chunk = 1024
    fmt = pyaudio.paInt16
    channels = 1

    audio = pyaudio.PyAudio()

    stream = audio.open(format=fmt,
                        channels=channels,
                        rate=rate,
                        input=True,
                        frames_per_buffer=chunk)

    print("🎙️ Recording in 0.5s... Speak clearly.")
    time.sleep(0.5)

    frames = []

    for _ in range(0, int(rate / chunk * duration)):
        data = stream.read(chunk, exception_on_overflow=False)
        frames.append(data)

    stream.stop_stream()
    stream.close()
    audio.terminate()

    print("🔊 Normalizing audio...")

    # Convert audio to numpy array (int16 → float32)
    audio_data = b''.join(frames)
    audio_np = np.frombuffer(audio_data, dtype=np.int16).astype(np.float32)

    # Normalize to [-1.0, 1.0]
    max_val = np.max(np.abs(audio_np))
    if max_val > 0:
        audio_np /= max_val

    # Scale back to int16 and save
    audio_np = (audio_np * 32767).astype(np.int16)
    wav.write(filename, rate, audio_np)

    print("✅ Recording complete.")
    return filename

def transcribe_audio(file_path):
    """Transcribe audio using Whisper with language set to English."""
    print("🧠 Transcribing (language='en')...")
    result = model.transcribe(file_path, language="en")
    print(f"📝 Transcribed: {result['text']}")
    return result['text']

def record_and_transcribe(duration=6):
    """Record, normalize, transcribe, and delete temp audio."""
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp:
        temp_filename = tmp.name

    record_audio(temp_filename, duration)
    time.sleep(0.2)  # ensure file is closed

    text = transcribe_audio(temp_filename)

    try:
        os.remove(temp_filename)
    except:
        print("⚠️ Couldn’t delete temp file.")

    return text
