# Software Requirements Specification (SRS) — JARVIS AI
Version 1.0 | Windows 11 | Python

## 1. Purpose and scope
JARVIS is a Windows desktop voice assistant developed incrementally from Level 1 commands toward Levels 2–4. Level 1 covers speech input/output, time/date, approved app and website launching, local notes, basic arithmetic, random numbers, help, and graceful exit.

## 2. Users and environment
- Primary user: individual Windows 11 desktop user.
- Python runtime and a virtual environment.
- Microphone and speakers/headphones.
- Current online speech recognition requires internet access.
- Windows SAPI provides speech output.

## 3. Functional requirements
| ID | Requirement | Priority | Acceptance criteria |
|---|---|---|---|
| FR-01 | Capture microphone speech | Must | Phrase is captured or a clear timeout/device error is shown. |
| FR-02 | Recognize speech | Must | Recognized text is normalized; network/recognition failures do not crash the app. |
| FR-03 | Speak responses | Must | Responses are printed and spoken through Windows speech output. |
| FR-04 | Time/date/day | Must | Correct local time/date/day returned. |
| FR-05 | Open approved apps | Must | Notepad, Calculator, Paint launch only for supported commands. |
| FR-06 | Open websites | Must | YouTube, Google, GitHub open in the default browser. |
| FR-07 | Notes | Must | Notes can be saved/read locally. |
| FR-08 | Arithmetic | Must | Basic arithmetic uses a restricted parser, never unrestricted eval. |
| FR-09 | Help and identity | Must | “help help”, “who are you?”, and common aliases work. |
| FR-10 | Graceful exit | Must | Exit phrases stop the loop safely. |
| FR-11 | Unknown command | Must | Polite fallback; assistant continues listening. |
| FR-12 | Testability | Must | Core routing can be tested without microphone/network hardware. |
| FR-13 | Future API secrets | Must | API keys come from environment configuration, never committed. |

## 4. Non-functional requirements
- Reliability: handle missing microphone, unclear speech, network errors, and missing notes.
- Usability: short spoken responses and visible console status.
- Security: allow-listed actions only; never execute arbitrary speech as shell commands.
- Privacy: disclose online transcription; notes remain local in current release.
- Maintainability: separate input/output, command routing, and skills as the project grows.
- Testability: automated tests should mock audio, network, and operating-system actions.

## 5. Constraints and exclusions
Level 1 does not include always-on wake word, unrestricted automation, guaranteed offline speech recognition, or autonomous consequential actions. Recognition can mishear accents/noise; fuzzy matching must be conservative.

## 6. Future levels
- Level 2: optional AI Q&A, API configuration, timeout/fallback behavior.
- Level 3: preferences, reminders, task management, persistent settings.
- Level 4: approved integrations, permissions, confirmations, action logs, stop mechanism.

## 7. Acceptance
A release is accepted when the target-level Must requirements pass, setup works on Windows 11, and known limitations are documented.
