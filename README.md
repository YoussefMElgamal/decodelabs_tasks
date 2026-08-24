# 🤖 Week 1 Project: Rule-Based Chatbot

A simple, deterministic chatbot built in Python for Project 1 of the DecodeLabs AI Internship — available both as a console app and as a live web app built with Streamlit. It follows an **Input → Process → Output** model, using a dictionary (hash map) for fast, exact-match responses instead of an if-elif chain.

## Demo

🔗 **Live app:** _add your Streamlit Community Cloud link here_

## How It Works

- Sanitizes user input (strips whitespace, lowercases it).
- Looks up the input in a dictionary via `.get(key, default)` — matched inputs get an instant response, unmatched ones get a fallback.
- The console version (`Decode_labs_chatbot.py`) runs in a `while True` loop and exits cleanly on `bye`, `exit`, or `quit`.
- The web version (`app.py`) reuses the exact same logic through a shared `get_response()` function — no duplicated code.

## Project Structure

```
.
├── Decode_labs_chatbot.py   # Core logic (knowledge base + get_response()) + console chatbot
├── app.py                   # Streamlit web interface, imports get_response()
├── requirements.txt         # Dependencies
└── README.md
```

## Run It — Console Version

```bash
python Decode_labs_chatbot.py
```

```
Chatbot: Hello! Type 'bye', 'exit', or 'quit' to end our chat.
You: hello
Chatbot: Hi there! How can I help you today?
You: bye
Chatbot: Goodbye! Have a great day.
```

## Run It — Web Version (Streamlit)

```bash
pip install -r requirements.txt
streamlit run app.py
```

This opens a chat UI in your browser at `http://localhost:8501`.

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
