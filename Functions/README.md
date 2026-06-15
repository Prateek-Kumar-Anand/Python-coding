# 🔁 Functions — Loops, Input & Web Scraping

A set of small interactive Python programs exploring **functions, loops, conditionals, user input**, and a first look at **web scraping** with BeautifulSoup. 🧠🌐

---

## 📦 What's Inside

| File | Description |
|---|---|
| 📝 **`student_regester.py`** | An interactive student name collector. Repeatedly asks for student names using a `while True` loop, appending each to a list until the user enters nothing (empty input), then prints out the full roster. |
| 📋 **`survey.py`** | A console-based survey program wrapped in a function. Asks for name, age, gender, job, salary, and number of siblings — with an **age-gate check** for users under 18 (asks them to confirm minor status) and an opt-in/opt-out at the start (`Y`/`N`). |
| 🌐 **`beautysoup object for HTML.py`** | A minimal web-scraping starter — fetches a webpage (`nostarch.com`) using `requests`, checks the response status with `raise_for_status()`, and parses it into a `BeautifulSoup` object for further extraction. |

---

## 🔍 Concept Breakdown

### 📝 Student Register (`student_regester.py`)
```python
Student = []
while True:
    name = input()
    if name == '':
        break
    Student = Student + [name]
```
Demonstrates **`while True` loops with a break condition**, list building, and basic string formatting for prompts.

### 📋 Survey (`survey.py`)
```python
def survey():
    ...
    if int(age) < 18:
        # age-gate confirmation logic
```
Covers **function definitions**, **nested conditionals**, **type casting** (`int(age)`), and a simple **opt-in flow** before running the survey.

### 🌐 BeautifulSoup Basics (`beautysoup object for HTML.py`)
```python
import requests, bs4
res = requests.get('https://nostarch.com')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
```
The classic **first step of web scraping**: fetch a page, validate the response, and create a parseable `BeautifulSoup` object — ready for `.find()`, `.select()`, etc.

---

## 🛠️ Requirements

```bash
pip install requests beautifulsoup4
```

> ℹ️ `student_regester.py` and `survey.py` use only built-in Python — no extra packages needed.

## ▶️ Running

```bash
python "student_regester.py"
python "survey.py"
python "beautysoup object for HTML.py"
```

Both `student_regester.py` and `survey.py` are **interactive** — they'll prompt you for input directly in the terminal.

---

## 📌 Notes

- 🌱 `beautysoup object for HTML.py` only creates the soup object — it doesn't extract or print anything yet. A great base to extend with `.find_all()`, `.title`, link extraction, etc.
- 🔢 `survey.py` casts age input with `int()` — entering non-numeric text will raise an error (a good script to practice adding input validation to!).

---

✨ Small scripts, big fundamentals — loops, functions, input handling, and the gateway to web scraping.
