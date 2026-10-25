
import ast
import datetime
import operator
import random
import subprocess
import webbrowser
from pathlib import Path

import speech_recognition as sr
import win32com.client


BASE_DIR = Path(__file__).resolve().parent.parent
NOTES_FILE = BASE_DIR / "jarvis_notes.txt"


class JarvisAssistant:
    def __init__(self):
        self.engine = win32com.client.Dispatch("SAPI.SpVoice")
        self.engine.Rate = 1
        self.engine.Volume = 100

        self.recognizer = sr.Recognizer()
        self.running = True
        self.last_response = ""

    def speak(self, text):
        """Speak a message using Windows speech."""
        self.last_response = str(text)
        print(f"\nJARVIS: {text}")

        try:
            self.engine.Speak(str(text), 0)
        except Exception as error:
            print(f"Voice output error: {error}")

    def listen(self):
        """Listen through the microphone and recognize speech."""
        try:
            with sr.Microphone() as source:
                print("\nListening...")
                self.recognizer.adjust_for_ambient_noise(
                    source, duration=0.4
                )
                audio = self.recognizer.listen(
                    source, timeout=5, phrase_time_limit=10
                )

            command = self.recognizer.recognize_google(audio)
            command = command.lower().strip()
            print(f"You: {command}")
            return command

        except sr.WaitTimeoutError:
            print("No speech detected.")
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand.")
        except sr.RequestError:
            self.speak(
                "Speech recognition is unavailable. Please check your internet."
            )
        except (OSError, AttributeError) as error:
            print(f"Microphone error: {error}")

        return ""

    def open_app(self, name):
        """Open a supported Windows application."""
        apps = {
            "notepad": ["notepad.exe"],
            "calculator": ["calc.exe"],
            "paint": ["mspaint.exe"],
        }

        try:
            subprocess.Popen(apps[name])
            self.speak(f"Opening {name}.")
        except (OSError, KeyError):
            self.speak(f"I couldn't open {name}.")

    def save_note(self, note):
        """Save a note to a local text file."""
        timestamp = datetime.datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        with NOTES_FILE.open("a", encoding="utf-8") as file:
            file.write(f"[{timestamp}] {note}\n")

        self.speak("Your note has been saved.")

    def read_notes(self):
        """Display and speak saved notes."""
        if not NOTES_FILE.exists():
            self.speak("You have no saved notes.")
            return

        notes = NOTES_FILE.read_text(encoding="utf-8").strip()

        if not notes:
            self.speak("Your notes file is empty.")
            return

        print("\nYour saved notes:")
        print(notes)

        for line in notes.splitlines():
            self.speak(line)

    def calculate(self, expression):
        """Safely calculate basic arithmetic expressions."""
        operations = {
            ast.Add: operator.add,
            ast.Sub: operator.sub,
            ast.Mult: operator.mul,
            ast.Div: operator.truediv,
            ast.FloorDiv: operator.floordiv,
            ast.Mod: operator.mod,
            ast.Pow: operator.pow,
            ast.UAdd: operator.pos,
            ast.USub: operator.neg,
        }

        def evaluate(node):
            if (
                isinstance(node, ast.Constant)
                and type(node.value) in (int, float)
            ):
                if abs(node.value) > 10**12:
                    raise ValueError("Number too large")
                return node.value

            if isinstance(node, ast.BinOp) and type(node.op) in operations:
                left = evaluate(node.left)
                right = evaluate(node.right)

                if isinstance(node.op, ast.Pow) and abs(right) > 10:
                    raise ValueError("Exponent too large")

                result = operations[type(node.op)](left, right)

                if isinstance(result, (int, float)) and abs(result) > 10**15:
                    raise ValueError("Result too large")

                return result

            if isinstance(node, ast.UnaryOp) and type(node.op) in operations:
                return operations[type(node.op)](evaluate(node.operand))

            raise ValueError("Unsupported expression")

        try:
            tree = ast.parse(expression, mode="eval")
            result = evaluate(tree.body)

            if isinstance(result, float) and result.is_integer():
                result = int(result)

            self.speak(f"The answer is {result}.")

        except (
            ValueError,
            SyntaxError,
            TypeError,
            ZeroDivisionError,
            OverflowError,
        ):
            self.speak(
                "I couldn't calculate that. Please try a simple calculation."
            )

    def show_help(self):
        """Display supported voice commands."""
        print("""
============= JARVIS COMMANDS =============

CONVERSATION
  Hello Jarvis
  How are you?
  Who are you?
  Can you speak?
  What can you do?

TIME AND DATE
  What is the time?
  What is today's date?
  What day is it?

WINDOWS APPLICATIONS
  Open Notepad
  Open Calculator
  Open Paint

WEBSITES
  Open YouTube
  Open Google
  Open GitHub

NOTES
  Take a note
  Read my notes

UTILITIES
  Calculate 25 times 4
  Random number
  Repeat
  Help
  Stop Jarvis

===========================================
""")
        self.speak("These are my available commands.")

    def process_command(self, command):
        """Choose the appropriate skill for a command."""
        if not command:
            return

        # Exit
        if any(phrase in command for phrase in (
            "stop jarvis",
            "exit jarvis",
            "quit jarvis",
            "goodbye jarvis",
            "shut down jarvis",
        )):
            self.speak("Goodbye. JARVIS is shutting down.")
            self.running = False
            return

        # Conversation
        if (
            "hello" in command
            or "hi jarvis" in command
            or "hey jarvis" in command
        ):
            self.speak("Hello! How can I help you?")

        elif "how are you" in command:
            self.speak("I am running and ready to help.")

        elif "your name" in command or "who are you" in command:
            self.speak("I am JARVIS, your personal voice assistant.")

        elif "can you speak" in command or "speak to me" in command:
            self.speak("Yes, I can speak to you.")

        elif "what can you do" in command or command == "help":
            self.show_help()

        elif command in ("repeat", "repeat that", "say that again"):
            previous = self.last_response
            self.speak(previous or "Nothing to repeat yet.")

        # Time
        elif "time" in command:
            now = datetime.datetime.now()
            self.speak(f"The time is {now.strftime('%I:%M %p')}.")

        # Date
        elif (
            "date" in command
            or "today" in command
            or "what day" in command
        ):
            now = datetime.datetime.now()
            day = now.day

            if 11 <= day <= 13:
                suffix = "th"
            else:
                suffix = {
                    1: "st",
                    2: "nd",
                    3: "rd",
                }.get(day % 10, "th")

            self.speak(
                f"Today is {now.strftime('%A')}, "
                f"{day}{suffix} of {now.strftime('%B')}, "
                f"{now.year}."
            )

        # Windows applications
        elif "open notepad" in command:
            self.open_app("notepad")

        elif "open calculator" in command or "open calc" in command:
            self.open_app("calculator")

        elif "open paint" in command:
            self.open_app("paint")

        # Websites
        elif "open youtube" in command:
            webbrowser.open("https://www.youtube.com")
            self.speak("Opening YouTube.")

        elif "open google" in command:
            webbrowser.open("https://www.google.com")
            self.speak("Opening Google.")

        elif "open github" in command:
            webbrowser.open("https://github.com")
            self.speak("Opening GitHub.")

        # Notes
        elif "take a note" in command or "make a note" in command:
            self.speak("What would you like me to write down?")
            note = self.listen()

            if note:
                try:
                    self.save_note(note)
                except OSError as error:
                    print(f"Note saving error: {error}")
                    self.speak("I couldn't save your note.")

        elif "read my notes" in command or "show my notes" in command:
            self.read_notes()

        # Calculator
        elif command.startswith("calculate "):
            expression = command[len("calculate "):]

            replacements = [
                ("multiplied by", "*"),
                ("divided by", "/"),
                ("times", "*"),
                ("plus", "+"),
                ("minus", "-"),
            ]

            for phrase, symbol in replacements:
                expression = expression.replace(phrase, symbol)

            self.calculate(expression)

        # Random number
        elif "random number" in command:
            number = random.randint(1, 100)
            self.speak(f"Your random number is {number}.")

        else:
            self.speak(
                "I don't know that command yet. Say help to see my skills."
            )

    def run(self):
        """Start JARVIS."""
        self.speak("Hello! JARVIS is ready.")
        self.show_help()

        while self.running:
            command = self.listen()
            self.process_command(command)


if __name__ == "__main__":
    try:
        assistant = JarvisAssistant()
        assistant.run()

    except KeyboardInterrupt:
        print("\nJARVIS stopped by keyboard.")

    except Exception as error:
        print(f"JARVIS encountered an error: {error}")
