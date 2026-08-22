#  Week 1 Project: Rule-Based Chatbot

A simple, deterministic chatbot built in Python for Project 1 of the DecodeLabs AI Internship. It follows an **Input → Process → Output** model, using a dictionary (hash map) for fast, exact-match responses instead of an if-elif chain.

## How It Works

- Runs in a `while True` loop, reading user input each cycle.
- Sanitizes input (strips whitespace, lowercases it).
- Looks up the input in a dictionary via `.get(key, default)` — matched inputs get an instant response, unmatched ones get a fallback.
- Exits cleanly on `bye`, `exit`, or `quit`.

## Run It

```bash
python chatbot.py
```

```
Chatbot: Hello! Type 'bye', 'exit', or 'quit' to end our chat.
You: hello
Chatbot: Hi there! How can I help you today?
You: bye
Chatbot: Goodbye! Have a great day.
```

## Intents

| Input | Response |
|---|---|
| `hello`, `hi` | Greeting |
| `how are you` | Status check |
| `what is your name` | Identity |
| `help` | Lists commands |
| `bye`, `exit`, `quit` | Ends chat |

Anything else returns a default fallback message.

---
Project 1 — DecodeLabs AI Internship
