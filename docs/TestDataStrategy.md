# Test Data Strategy

## Objective

Provide reusable, maintainable, and version-controlled test data that supports data-driven testing across multiple environments.

---

# Data Sources

JSON

YAML

CSV

Mock APIs

Configuration Files

---

# Voice Commands

weather_commands.json

```json
[
  "What's the weather today?",
  "Will it rain tomorrow?",
  "Weather in Cupertino"
]
```

timer_commands.json

```json
[
  "Set a timer for five minutes",
  "Cancel my timer"
]
```

music_commands.json

```json
[
  "Play Jazz",
  "Pause Music"
]
```

---

# Localization Data

English

Spanish

French

German

Japanese

Chinese

---

# Invalid Test Data

Empty Commands

Unsupported Languages

Random Characters

Long Sentences

Profanity

---

# Environment Data

Simulator

Real Device

Development

QA

Staging

Production

---

# Test Data Principles

- No hardcoded data inside tests
- Reusable datasets
- Environment-specific configuration
- Version-controlled alongside source code
- Easily extendable for new Siri capabilities