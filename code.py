import random
import time
import os
import json

DATA_FILE = "quiz_data.json"

# Load data
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

# Save data
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

# Questions
def get_questions(level):
    easy = [
        {"q": "Extension of Python file?", "o": ["1. .py", "2. .txt", "3. .java", "4. .cpp"], "a": "1"},
        {"q": "Keyword to define function?", "o": ["1. func", "2. def", "3. function", "4. define"], "a": "2"},
        {"q": "Output: print(2+3)?", "o": ["1. 5", "2. 6", "3. 4", "4. 23"], "a": "1"}
    ]

    medium = [
        {"q": "Output: print(type(10))?", "o": ["1. int", "2. <class 'int'>", "3. number", "4. integer"], "a": "2"},
        {"q": "Loop for sequences?", "o": ["1. while", "2. for", "3. loop", "4. repeat"], "a": "2"},
        {"q": "len() does what?", "o": ["1. length", "2. add", "3. print", "4. delete"], "a": "1"}
    ]

    hard = [
        {"q": "Output: print(2**3**2)?", "o": ["1. 64", "2. 512", "3. 256", "4. 16"], "a": "2"},
        {"q": "Mutable data type?", "o": ["1. tuple", "2. list", "3. str", "4. int"], "a": "2"},
        {"q": "What does 'pass' do?", "o": ["1. skip", "2. stop", "3. error", "4. print"], "a": "1"}
    ]

    if level == "1":
        return easy
    elif level == "2":
        return medium
    else:
        return hard

# Login
def login():
    name = input("Enter your name: ").strip()
    data = load_data()

    if name not in data:
        print("New user created ✅")
        data[name] = {"high_score": 0, "history": []}
        save_data(data)
    else:
        print(f"Welcome back {name} 👋")

    return name

# Quiz
def start_quiz(user):
    print("\nSelect Difficulty:")
    print("1. Easy\n2. Medium\n3. Hard")
    level = input("Enter choice: ")

    questions = get_questions(level)
    random.shuffle(questions)

    score = 0
    time_limit = 10

    for i, q in enumerate(questions, 1):
        print(f"\nQ{i}: {q['q']}")
        for opt in q["o"]:
            print(opt)

        start = time.time()
        ans = input(f"Answer within {time_limit}s: ")
        end = time.time()

        if end - start > time_limit:
            print("⏰ Time up!")
            continue

        if ans == q["a"]:
            print("Correct ✅")
            score += 1
        else:
            print("Wrong ❌")

    total = len(questions)
    percent = (score / total) * 100

    print("\n===== RESULT =====")
    print(f"Score: {score}/{total}")
    print(f"Percentage: {percent:.2f}%")

    # Update data
    data = load_data()
    data[user]["history"].append(score)

    if score > data[user]["high_score"]:
        print("🎉 New High Score!")
        data[user]["high_score"] = score

    save_data(data)

# View Profile
def view_profile(user):
    data = load_data()
    print("\n=== PROFILE ===")
    print("Name:", user)
    print("High Score:", data[user]["high_score"])
    print("All Scores:", data[user]["history"])

# Menu
def menu():
    user = login()

    while True:
        print("\n=== PYTHON QUIZ PRO MAX ===")
        print("1. Start Quiz")
        print("2. View Profile")
        print("3. Logout")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            start_quiz(user)
        elif choice == "2":
            view_profile(user)
        elif choice == "3":
            user = login()
        elif choice == "4":
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice!")

# Run
menu()
