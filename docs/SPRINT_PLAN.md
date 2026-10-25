# Sprint Plan — JARVIS AI
Assumption: one-week sprints; adjust as needed. Create GitHub issues for individual tasks and group them by milestone/sprint.

## Sprint 1 — Level 1 foundation
- [ ] Verify clean setup from README.
- [ ] Add and review project documentation/diagrams.
- [ ] Verify microphone input and Windows SAPI output.
- [ ] Verify time/date, identity, help, and exit.
- [ ] Verify allow-listed app/site launch, notes, and safe arithmetic.
- [ ] Record manual test evidence and known limitations.
**Exit:** core Level 1 paths work; errors do not crash the loop; docs match actual behavior.

## Sprint 2 — Command reliability
- [ ] Add tested normalization and aliases.
- [ ] Support repeated words and identity/help variations.
- [ ] Handle timeout, unclear speech, and network errors.
- [ ] Separate command parsing from I/O.
- [ ] Add unit tests for aliases and false-positive cases.

## Sprint 3 — Level 2 AI integration
- [ ] Choose provider and document privacy implications.
- [ ] Load key from environment; never commit secrets.
- [ ] Add timeout, failure handling, and fallback.
- [ ] Route known local commands before general AI Q&A.
- [ ] Test missing/invalid key and mocked responses.

## Sprint 4 — Level 3 personal assistant
- [ ] Preferences and local settings.
- [ ] Reminders and task management.
- [ ] Persistence, validation, and privacy tests.

## Sprint 5 — Level 4 controlled automation
- [ ] Permission-scoped skills and approved integrations.
- [ ] Confirm consequential actions.
- [ ] Add action logging and global stop mechanism.
- [ ] Test failures and permissions.

## Sprint 6 — Quality and release
- [ ] Run automated and manual acceptance tests.
- [ ] Resolve critical/high defects.
- [ ] Review dependencies and secret handling.
- [ ] Update docs, release notes, and setup instructions.

## Definition of Done
Acceptance criteria and relevant tests pass; documentation is updated; no secrets/personal data are committed; changes are reviewed.
