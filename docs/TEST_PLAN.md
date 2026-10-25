# Test Plan — JARVIS AI

## Approach
- Unit: normalization, aliases, arithmetic validation, and individual skills.
- Integration: router with mocked speech, browser, and OS calls.
- Manual: real microphone, Windows SAPI, and actual app launching.
- Regression: rerun tests whenever aliases/routing change.
- Acceptance: verify requirements for the current sprint.

## Environment
Windows 11, project virtual environment, installed requirements, microphone/speaker for manual tests. Automated tests should not require real audio or internet; mock online speech recognition.

## Test cases
| ID | Input/scenario | Expected result | Test type |
|---|---|---|---|
| TC-01 | Start app | Greeting appears and is spoken | Manual |
| TC-02 | “What time is it?” | Current local time | Unit/manual |
| TC-03 | “What is today's date?” | Correct date and weekday | Unit/manual |
| TC-04 | “Who are you?” / “What is your name?” | Identity response | Unit |
| TC-05 | “Help” / “Help help” | Help list | Unit/manual |
| TC-06 | “Open YouTube” | Browser opens approved site | Integration |
| TC-07 | “Open Notepad” | Notepad launches | Manual |
| TC-08 | Save/read notes | Local notes saved/read | Unit/integration |
| TC-09 | “Calculate 25 times 4” | Result 100 | Unit |
| TC-10 | Invalid arithmetic | Safe rejection; no code execution | Security |
| TC-11 | Unknown phrase | Fallback; app continues | Unit/manual |
| TC-12 | Exit phrase | Clean shutdown | Unit/manual |
| TC-13 | Missing microphone | Clear error/safe shutdown | Manual |
| TC-14 | Unclear speech | Ask to repeat; no skill runs | Integration |
| TC-15 | No internet for STT | Clear error; no crash | Integration |
| TC-16 | Similar unrelated phrase | No unintended skill activation | Regression |
| TC-17 | Ctrl+C | Graceful shutdown | Manual |

## Security/non-functional tests
- No arbitrary shell execution from speech.
- No hard-coded API keys in repository.
- Network/audio errors do not crash the main loop.
- Notes remain local in this release.
- Fuzzy matching does not trigger unrelated commands.

## Exit criteria
Relevant Must tests pass, no known critical/high defects remain, and documentation is current. File bugs with reproduction steps, expected/actual results, environment, and redacted logs.
