# Tests
Keep automated tests independent from microphone hardware and online speech services.

- `unit/`: normalization, intent matching, arithmetic validation, and skill logic.
- `integration/`: command router with speech input/output and OS/browser calls mocked.
- `test_voice_commands.py`: acceptance checklist until command parsing becomes importable and side-effect-free.

Install pytest when ready: `python -m pip install pytest`, then run `python -m pytest -q`.

Do not call this a passing automated test suite until actual pytest tests have been implemented and run.
