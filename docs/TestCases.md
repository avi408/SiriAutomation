# Test Cases

---

## TC-001 Launch Siri

Requirement

FR-001

Priority

P0

Suite

Smoke

Preconditions

Siri Enabled

Device Ready

Steps

1. Press Side Button

2. Wait for Siri

Expected Result

Siri launches successfully.

---

## TC-002 Ask Weather

Requirement

FR-006

Priority

P0

Suite

Smoke

Steps

1. Launch Siri

2. Ask "What's the weather today?"

Expected Result

Weather card displayed.

Voice response generated.

---

## TC-003 Invalid Command

Requirement

FR-009

Priority

P1

Suite

Regression

Steps

Ask

"asdfghjkl"

Expected

Siri displays an appropriate error message.

---

## TC-004 Network Failure

Requirement

FR-010

Priority

P0

Suite

Regression

Steps

Disable Wi-Fi

Launch Siri

Ask weather

Expected

Graceful network error displayed.

---

## TC-005 Localization

Requirement

FR-011

Priority

P1

Suite

Localization

Steps

Change device language to Spanish

Ask weather

Expected

Spanish response displayed.

---

## TC-006 Accessibility

Requirement

FR-012

Priority

P1

Suite

Accessibility

Steps

Enable VoiceOver

Launch Siri

Expected

VoiceOver correctly announces controls.

---

## TC-007 Performance

Requirement

NFR-001

Priority

P1

Suite

Performance

Steps

Measure response time

Expected

Response <2 seconds.

---

## TC-008 Long Conversation

Requirement

NFR-008

Priority

P2

Suite

Reliability

Steps

Execute 50 consecutive Siri commands

Expected

No crash

No memory leak

Consistent response