 🧠 Smart Daily Hub

A multi-tool desktop productivity app built with Python's `tkinter` library — featuring a motivation quote generator, focus timer, calculator, and a notes manager, all in one clean GUI window.

 📋 About

Smart Daily Hub is a step up from terminal projects — it's a proper graphical desktop application with a main menu and multiple mini-tools accessible from one place. Think of it as a lightweight daily companion app, built from scratch using Python.

 ✨ Features

 💬 Motivation
- Displays a random motivational quote with a single click
- Comes with 5 built-in quotes to keep you going

 ⏱️ Focus Timer
- Enter any duration in seconds, minutes, or hours
- Countdown displayed live in `HH:MM:SS` format
- Great for Pomodoro-style focus sessions

 🔢 Calculator
- Takes two numbers and performs addition, subtraction, multiplication, or division
- Handles division by zero gracefully

 📝 Notes
- Type and save notes to a local `notes.txt` file
- Load previously saved notes back into the app
- Notes are appended and separated with `---` for clean formatting

 🚀 How to Run

Make sure you have Python installed (tkinter comes built-in with standard Python installations).

```bash
python main.py
```

A 600×600 desktop window will launch with the main menu.

 🛠️ Built With

- Python 3
- `tkinter` (GUI)
- `random` module
- File I/O (`notes.txt`)

 📁 File Structure

```
Smart-Daily-Hub/
├── main.py
└── notes.txt
```

 💡 Concepts Used

- `tkinter` window, frames, labels, buttons, entry, text widgets
- Multi-screen navigation using `pack_forget()` and `pack()`
- `root.after()` for the real-time countdown timer
- Global variables for timer state management
- File I/O (append and read modes)
- Lambda functions for button commands
- Error handling with try/except

 🆚 What's Different About This Project

Unlike the previous terminal-based projects, Smart Daily Hub is a GUI application — a major milestone! Instead of `print()` and `input()`, everything runs through buttons, labels, and text boxes in a real desktop window.

---
Part of my Python beginner projects series 🐍
