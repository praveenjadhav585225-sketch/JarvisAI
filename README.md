# JARVIS AI — Level 1 Voice Assistant

A beginner-friendly Python voice assistant built for Windows 11.

## Features

- Voice input using SpeechRecognition
- Spoken responses using Windows SAPI
- Current time, date, and day
- Open Notepad, Calculator, and Paint
- Open YouTube, Google, and GitHub
- Save and read local notes
- Basic arithmetic calculations
- Random number generation
- Voice commands to exit

## Technologies

- Python
- SpeechRecognition
- PyAudio
- Windows SAPI / pywin32

## Setup

1. Install Python on Windows.
2. Clone this repository.
3. Open a terminal in the project directory.
4. Create and activate a virtual environment:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

5. Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

6. Start the assistant:

```powershell
python src\main.py
```

## Example Commands

- "What is the time?"
- "What is today's date?"
- "Open YouTube"
- "Open Notepad"
- "Take a note"
- "Calculate 25 times 4"
- "Random number"
- "Help"
- "Stop Jarvis"

## Notes

- Speech recognition uses Google's online recognition service and requires internet access.
- Voice output uses Windows SAPI.
- Notes are saved locally in `jarvis_notes.txt`.
- This project currently supports predefined commands rather than general AI conversations.

## Future Improvements

- AI-powered question answering
- Wake-word detection
- Improved speech recognition
- More computer automation skills
