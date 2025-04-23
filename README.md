
# 🎙️ Nox – Your AI-Powered Voice Assistant

Nox is a fully local, extensible desktop voice assistant powered by **Gemini Pro**, **Whisper**, and **Porcupine**. It listens, understands, responds intelligently, and can even control your operating system.

---

## ✨ Features

- 🔊 Wake word activation – “Hey Nox”
- 🎙️ Speech-to-text using Whisper
- 🤖 Gemini-powered conversational AI
- 🧠 Memory: “Remember my name is...” works!
- 💬 Persona switching: “Be sarcastic” changes tone
- 💻 System control: Open apps, URLs, screenshots, shutdown
- 🗃️ Last 10 interactions cached in `nox_cache.json`
- 🗣️ Text-to-speech replies using pyttsx3

---

## 🧠 Tech Stack

| Layer | Technology |
|-------|------------|
| AI/LLM | Gemini 1.5 Pro (Google) |
| STT | Whisper (OpenAI) |
| TTS | pyttsx3 |
| Wake Word | Porcupine by Picovoice |
| Core | Python 3.10+ |
| Config | python-dotenv |
| Optional GUI | Flask or Tkinter (future) |

---

## 📁 Folder Structure



## 🧠 Tech Stack

| Layer | Technology |
|-------|------------|
| AI/LLM | Gemini 1.5 Pro (Google) |
| STT | Whisper (OpenAI) |
| TTS | pyttsx3 |
| Wake Word | Porcupine by Picovoice |
| Core | Python 3.10+ |
| Config | python-dotenv |
| Optional GUI | Flask or Tkinter (future) |

---

## 📁 Folder Structure
```
nox-assistant/
├── nox/
│   ├── main.py
│   ├── ai_engine.py
│   ├── speech_to_text.py
│   ├── text_to_speech.py
│   ├── wake_word.py
│   ├── memory.py
│   ├── cache.py
│   ├── system_controller.py
│   └── __init__.py
├── assets/                  # wake word files
├── .env.example             # API keys template
├── requirements.txt
├── README.md
└── .gitignore

```

## ⚙️ Installation Guide

### 📦 Requirements

- Python 3.10+
- A working microphone
- An internet connection (for Gemini/Whisper)
- A [Gemini API key](https://makersuite.google.com/app/apikey)
- A [Picovoice access key](https://console.picovoice.ai/)



### 🧪 Setup Steps

#### 1. Clone the repo
```bash
git clone https://github.com/yourusername/nox-assistant.git
cd nox-assistant
```

#### 2. Create a virtual environment
```bash
python -m venv venv
venv\\Scripts\\activate     # Windows
source venv/bin/activate    # macOS/Linux
```

#### 3. Install dependencies
```bash
pip install -r requirements.txt
```

#### 4. Add your `.env` file
Copy the example and add your own keys:
```bash
cp .env.example .env
```

Edit `.env`:
```
GEMINI_API_KEY=your_google_gemini_api_key
PICOVOICE_ACCESS_KEY=your_picovoice_key
```

---

## 🚀 Usage

```bash
python nox/main.py
```

Say:
- “Hey Nox” (wake word)
- “What’s the capital of Japan?”
- “Open Notepad”
- “Remember my name is Alice”
- “What’s my name?”
- “Be sarcastic”

---

## 🗃 .env Configuration

```env
GEMINI_API_KEY=your_key_here
PICOVOICE_ACCESS_KEY=your_key_here
```

---

## 🧠 Memory & Cache

- Stores your name, facts, etc. in `nox_memory.json`
- Caches last 10 interactions in `nox_cache.json`

---

## 🛠 Troubleshooting

- ✅ Mic not detected? Check audio device permissions.
- ✅ Wake word not triggering? Ensure `.ppn` file path is correct.
- ✅ Keys not loading? Make sure `.env` is in `%AppData%\\Nox` or local.

---

## 🛡 License

MIT License – you’re free to use, modify, and distribute Nox.

---

## 📌 Roadmap

- [ ] Web-based GUI (Flask)
- [ ] LLM fallback via LLaMA (offline)
- [ ] Real-time streaming STT
- [ ] Auto-installable `.exe` for Windows
- [ ] Chat log viewer
