"""Manual acceptance checklist; not an automated pytest suite yet."""
VOICE_COMMAND_CASES = [
    ("what is the time", "time"),
    ("what time is it", "time"),
    ("who are you", "identity"),
    ("what is your name", "identity"),
    ("help", "help"),
    ("help help", "help"),
    ("open youtube", "open_website"),
    ("calculate 25 times 4", "calculate"),
    ("stop jarvis", "exit"),
]
