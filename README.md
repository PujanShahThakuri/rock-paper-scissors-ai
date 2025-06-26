# 🪨📄✂️ Rock-Paper-Scissor AI (Python Terminal Game)

A smart, terminal-based **Rock-Paper-Scissor game** built using Python.  
The computer uses **basic AI logic** to analyze your behavior and tries to beat you using prediction.

---

## 🚀 Features

- 🎮 Play against a smart computer in the terminal
- 🧠 Simple AI: predicts your move based on your previous choices
- 📈 Score saved locally in `score.txt` across game sessions
- ✅ Written using pure Python — no external libraries required
- 🔁 Loop-based gameplay (play as long as you like, or quit anytime)

---

## 🧠 How the AI Works

Instead of random choices, the computer learns your habits:
1. It tracks how often you play **rock**, **paper**, or **scissors**
2. Then it **predicts your next move**
3. It picks the move that beats your predicted choice

> Example: If you've played “rock” more often, the computer will choose “paper” to beat it.

This is **frequency-based prediction**, a basic form of **rule-based AI**.

---

## 📂 Project Structure

📁 rock-paper-scissors-ai/
├── rock-paper-scissor.py # Main Python game file
└── score.txt # Score file (auto-created after first play)

yaml
Copy
Edit

---

## ▶️ How to Run

### Requirements:
- Python 3.x

### To start the game:
```bash
python rock-paper-scissor.py
You’ll be prompted to enter:

rock, paper, or scissors to play

q to quit

Your score and the computer's score will be shown and saved after each round.

📚 What This Project Covers
Python conditionals and loops

Dictionaries and basic data analysis

File handling for saving state

Randomness and AI-style decision-making

Clean function-based structure

🔧 Future Improvements
🎨 Add colors or emojis for a more fun terminal UI

🖼️ Add a GUI using Tkinter

🌐 Multiplayer mode or LAN support

📊 Analyze patterns, not just frequency

☁️ Save scores online or in a database

🧑‍💻 Author
Pujan Shahi Thakuri
Python Developer • AI Explorer • Student from Nepal 🇳🇵

📜 License
This project is released under the MIT License.
Feel free to use, modify, or contribute!

⭐️ Tip
Most people choose rock as their first move. Try starting with paper 😉
