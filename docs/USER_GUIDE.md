# User Guide — JARVIS AI

## Requirements
Windows 11, Python, microphone, speakers/headphones, and internet for current online speech recognition.

## Install and run
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python src\main.py
```
If activation is blocked, run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` in that PowerShell window and activate again.

## Example commands
“What is the time?”, “What is today's date?”, “Who are you?”, “Help”, “Open YouTube”, “Open Notepad”, “Take a note”, “Read my notes”, “Calculate 25 times 4”, “Random number”, “Stop Jarvis”. Exact phrases depend on the current code.

## Troubleshooting
- Check Windows Settings → System → Sound → Input if microphone is unavailable.
- Check internet access for speech recognition.
- Check speaker volume and Windows speech settings if output is silent.
- Speak clearly in a quiet environment and add tested aliases for repeated misrecognitions.
- Activate `.venv` before installing dependencies.

## Privacy
Current speech recognition sends audio to an online provider for transcription. Do not speak passwords or confidential data. Notes are stored locally in `jarvis_notes.txt`.
