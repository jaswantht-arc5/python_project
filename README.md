# Python Quiz Pro Max 🎯

Python Quiz Pro Max is a command-line based quiz application developed using Python.  
The project is designed to test users’ Python programming knowledge through different difficulty levels while also maintaining user profiles, quiz history, and high scores.

This project is beginner-friendly and demonstrates important Python concepts such as:

- Functions
- File Handling
- JSON Data Storage
- Loops
- Conditional Statements
- Lists & Dictionaries
- Randomization
- Time Management
- User Input Handling

---

# 📖 Project Overview

The application allows users to:

1. Create/Login into an account
2. Choose quiz difficulty
3. Answer timed quiz questions
4. View their scores and performance
5. Store progress permanently using JSON files

The program uses a menu-driven approach, making it easy to navigate and user-friendly.

---

# ✨ Features

## 👤 User Login System

- Users can create new accounts automatically.
- Existing users can log in again.
- User data is stored permanently.

Example:

```text
Enter your name: Jaswanth
Welcome back Jaswanth 👋
```

---

## 🎚 Difficulty Levels

The quiz contains 3 levels:

| Level | Description |
|------|-------------|
| Easy | Basic Python questions |
| Medium | Intermediate concepts |
| Hard | Advanced Python logic |

Users can select the level before starting the quiz.

---

## 🔀 Randomized Questions

Questions are shuffled every time using Python’s `random.shuffle()` function.

This prevents the quiz from appearing in the same order repeatedly.

---

## ⏳ Timer-Based Quiz

Each question must be answered within **10 seconds**.

If the user exceeds the time limit:

```text
⏰ Time up!
```

The answer is skipped automatically.

---

## ✅ Instant Result Feedback

After every answer:

- Correct answers show:
  
```text
Correct ✅
```

- Wrong answers show:

```text
Wrong ❌
```

This improves user interaction.

---

## 📊 Score & Percentage Calculation

At the end of the quiz, the program calculates:

- Total Score
- Total Questions
- Percentage

Example:

```text
===== RESULT =====
Score: 2/3
Percentage: 66.67%
```

---

## 🏆 High Score Tracking

The program automatically saves the highest score achieved by each user.

If a user beats their previous record:

```text
🎉 New High Score!
```

---

## 📜 Quiz History

Every quiz attempt is stored inside the user profile.

Example:

```text
All Scores: [1, 2, 3]
```

This helps users track improvement over time.

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3 | Main programming language |
| JSON | Data storage |
| Random Module | Shuffle questions |
| Time Module | Quiz timer |
| OS Module | File checking |

---

# 📂 Project Structure

```bash
Python-Quiz-Pro-Max/
│
├── quiz.py
├── quiz_data.json
└── README.md
```

---

# 📁 File Description

## 1. `quiz.py`

Main Python program containing:

- Login system
- Quiz logic
- Menu system
- Result calculation
- Profile management

---

## 2. `quiz_data.json`

Stores user information permanently.

Example:

```json
{
  "Jaswanth": {
    "high_score": 3,
    "history": [2, 3, 1]
  }
}
```

---

## 3. `README.md`

Contains project documentation and instructions.

---

# ⚙️ Installation Guide

## Step 1: Install Python

Download Python from:

https://www.python.org/downloads/

Verify installation:

```bash
python --version
```

---

## Step 2: Download or Copy the Code

Save the code as:

```bash
quiz.py
```

---

## Step 3: Run the Program

Open terminal or command prompt.

Execute:

```bash
python quiz.py
```

---

# ▶️ Working of the Program

## 1. Program Starts

The `menu()` function is executed.

```python
menu()
```

---

## 2. User Login

The user enters their name.

If the user is new:

- A new profile is created.

If the user already exists:

- Previous data is loaded.

---

## 3. Menu Display

```text
=== PYTHON QUIZ PRO MAX ===
1. Start Quiz
2. View Profile
3. Logout
4. Exit
```

---

## 4. Quiz Starts

The user selects difficulty level.

Questions are loaded using:

```python
get_questions(level)
```

---

## 5. Timer Starts

For every question:

```python
start = time.time()
```

The answer time is measured.

---

## 6. Answer Validation

If the answer matches:

```python
if ans == q["a"]:
```

Score increases.

---

## 7. Results Generated

At the end:

- Score displayed
- Percentage calculated
- High score updated
- History saved

---

# 🧠 Python Concepts Used

This project demonstrates many important Python concepts.

## Functions

Example:

```python
def login():
```

Functions improve code reusability.

---

## Dictionaries

Questions are stored using dictionaries.

Example:

```python
{
  "q": "Output: print(2+3)?",
  "a": "1"
}
```

---

## Lists

Questions are stored inside lists.

---

## Conditional Statements

Used for menu choices and answer checking.

Example:

```python
if choice == "1":
```

---

## Loops

Used to display questions repeatedly.

Example:

```python
for i, q in enumerate(questions, 1):
```

---

## File Handling

Used for storing data permanently.

Example:

```python
with open(DATA_FILE, "r") as f:
```

---

## JSON Handling

Used to save and load user data.

Example:

```python
json.load(f)
```

---

# 📸 Sample Execution

```text
Enter your name: Jaswanth

=== PYTHON QUIZ PRO MAX ===
1. Start Quiz
2. View Profile
3. Logout
4. Exit

Enter choice: 1

Select Difficulty:
1. Easy
2. Medium
3. Hard

Q1: Output: print(2+3)?
1. 5
2. 6
3. 4
4. 23

Answer within 10s: 1

Correct ✅
```

---

# 🚀 Future Enhancements

The project can be improved further by adding:

## 🎨 GUI Version

Using:

- Tkinter
- PyQt

---

## 🌐 Online Database

Store data online using:

- Firebase
- MySQL
- MongoDB

---

## 🏅 Leaderboard System

Global ranking for players.

---

## 📚 More Question Categories

Add quizzes for:

- C Programming
- Java
- Data Structures
- Aptitude

---

## 🔊 Sound Effects

Add sounds for:

- Correct answer
- Wrong answer
- Timer alerts

---

# ❗ Limitations

- Works only in terminal/command prompt
- Limited number of questions
- No multiplayer support
- Timer is basic

---

# 🤝 Contribution

Contributions are welcome.

You can improve the project by:

- Adding more questions
- Improving UI
- Optimizing code
- Adding new features

---

# 📜 License

This project is open-source and free to use for educational purposes.

---

# 👨‍💻 Author

Developed using Python ❤️

Python Quiz Pro Max — Learning Python through fun quizzes 🎯
