import pvporcupine
import pyaudio
import struct
import os
from dotenv import load_dotenv

# 🔐 Your Picovoice Access Key (replace this with your actual key)
load_dotenv()
porcupine_key = os.getenv("PICOVOICE_ACCESS_KEY")


def wait_for_wake_word(keyword_path="assets/hey_nox.ppn"):
    porcupine = pvporcupine.create(
        access_key=porcupine_key,
        keyword_paths=[keyword_path]
    )

    audio = pyaudio.PyAudio()

    stream = audio.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length
    )

    print("🔊 Listening for 'Hey Nox'...")

    try:
        while True:
            pcm = stream.read(porcupine.frame_length, exception_on_overflow=False)
            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

            if porcupine.process(pcm) >= 0:
                print("🟢 Wake word detected!")
                break
    finally:
        stream.stop_stream()
        stream.close()
        audio.terminate()
        porcupine.delete()
