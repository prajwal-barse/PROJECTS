# Python Learning Projects

A collection of small Python projects that document my hands-on progress with core programming concepts. Each project builds on the skills from the previous one and focuses on writing practical, understandable programs.

## Projects

### 1. Calculator

A command-line calculator for performing basic arithmetic operations.

**Concepts used:**

- Functions for arithmetic operations: addition, subtraction, division, multiplication, powers, square roots, and percentages
- A menu-driven program using `while` loops and `if` / `elif` / `else`
- Input validation and exception handling with `try` / `except ValueError`
- File handling with `open()` and context managers (`with`) to save, view, and clear calculation history
- Basic arithmetic and comparison operators, including a zero-division check

### 2. Expense Tracker v1

An initial expense-tracking application for recording and managing expenses.

**Concepts used:**

- Nested dictionaries to store expense records in memory
- Loops for creating records, searching entries, and calculating total spending
- Lists, dictionary methods, and the `clear()` method
- Functions and menu-driven control flow
- Input validation with `try` / `except ValueError`
- Text-file storage with append, read, and write modes
- Searching expenses by product name or category

### 3. File Organizer

A utility that organizes files into appropriate folders based on their type or extension.

**Concepts used:**

- The `os` module for filesystem automation
- Directory and file checks with `os.path.isdir()`, `os.path.isfile()`, and `os.path.exists()`
- Listing and changing directories with `os.listdir()` and `os.chdir()`
- Building paths safely with `os.path.join()`
- Creating folders with `os.mkdir()` and moving/renaming files with `os.rename()`
- Categorizing files by extension using lists, loops, and conditional logic
- Handling duplicate filenames and producing an organization summary
- Parallel iteration with `zip()`

### 4. Expense Tracker v2

An improved version of the expense tracker with persistent structured storage.

**Concepts used:**

- JSON data persistence with the `json` module (`json.load()` and `json.dump()`)
- File-existence and file-size checks using the `os` module
- Dictionaries stored as structured expense records in a JSON file
- Lists and sets to calculate totals, per-category spending, highest/lowest expenses, and averages
- Sorting and generating the next expense ID
- Input cleaning with `strip()` and `lower()`
- CRUD-style operations: create, view, search, and delete expenses
- Functions, loops, conditions, and exception handling

### 5. Bank Account Management System

A program for managing bank-account operations such as account details, deposits, withdrawals, and balances.

**Concepts used:**

- Object-oriented programming with the `bank_account` and `bank` classes
- Constructors (`__init__`), instance attributes, objects, and methods
- Encapsulation conventions through private attributes such as `__pin` and `__balance`
- JSON-based account and transaction persistence
- Nested dictionaries for account details and transaction histories
- Random account-number generation with `random.randint()` and collision checking
- Date and time stamps with `datetime`
- File handling, `os` module checks, input validation, exception handling, loops, and conditional logic
- Account creation, login verification, deposits, withdrawals, transfers, account updates, and deletion

## Purpose

This repository is a record of my learning journey in Python. The projects focus on applying concepts through practice, improving problem-solving skills, and gradually writing more organized and reusable code.

## Technologies

- Python 3
