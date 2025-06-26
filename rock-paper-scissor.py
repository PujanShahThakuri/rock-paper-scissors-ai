import random
import os

SCORE_FILE = "score.txt"
user_move_history = {"rock": 0, "paper": 0, "scissors": 0}

# Load score from file
def load_score():
    if os.path.exists(SCORE_FILE):
        with open(SCORE_FILE, "r") as f:
            line = f.readline().strip()
            if line:
                parts = line.split(',')
                return {"user": int(parts[0]), "computer": int(parts[1])}
    return {"user": 0, "computer": 0}

# Save score to file
def save_score(score):
    with open(SCORE_FILE, "w") as f:
        f.write(f"{score['user']},{score['computer']}")

# Get the user's choice
def get_user_choice():
    while True:
        choice = input("Choose [rock, paper, scissors] or 'q' to quit: ").lower()
        if choice in ["rock", "paper", "scissors", "q"]:
            return choice
        print("Invalid input. Please try again.")

# Predict user move based on frequency
def predict_user_move():
    if sum(user_move_history.values()) == 0:
        return random.choice(["rock", "paper", "scissors"])
    return max(user_move_history, key=user_move_history.get)

# Computer chooses a move to beat predicted user move
def get_computer_choice():
    predicted = predict_user_move()
    if predicted == "rock":
        return "paper"
    elif predicted == "paper":
        return "scissors"
    else:  # predicted == "scissors"
        return "rock"

# Determine the winner
def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

# Game loop
def play():
    score = load_score()
    print("🎮 Welcome to Rock-Paper-Scissors with Smart Computer!")
    print(f"📊 Previous Score - You: {score['user']} | Computer: {score['computer']}")

    while True:
        user = get_user_choice()
        if user == "q":
            break

        user_move_history[user] += 1

        computer = get_computer_choice()
        print(f"🧠 Computer predicted you'll play '{predict_user_move()}', so it chose: {computer}")

        winner = determine_winner(user, computer)

        if winner == "tie":
            print("🤝 It's a tie!")
        elif winner == "user":
            print("✅ You win this round!")
            score["user"] += 1
        else:
            print("❌ Computer wins this round!")
            score["computer"] += 1

        print(f"📈 Current Score - You: {score['user']} | Computer: {score['computer']}\n")
        save_score(score)

    print("👋 Thanks for playing! Final score saved.")

# Run the game
if __name__ == "__main__":
    play()
