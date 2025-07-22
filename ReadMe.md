# Flask CRUD Web Application

> ✅ A beginner-to-intermediate level Flask project demonstrating **user authentication**, **CRUD operations**, and **session handling** — fully designed and developed from scratch as part of my portfolio for Werkstudent (student job) applications in the IT field in Germany.

---

## 📌 Project Overview

This is a **fully functional CRUD (Create, Read, Update, Delete)** web app built using **Python Flask**. It allows users to:

- Create an account with validations
- Log in securely
- Add, view, and update their own task list
- Maintain user sessions
- Save and retrieve user data from a file-based system (text file)

This project was **built entirely by me** — without using frameworks like Django, database tools like SQLAlchemy, or pre-built templates. The goal was to understand every line of code and logic behind web applications.

---

## 🛠️ Technologies Used

| Tool | Purpose |
|------|---------|
| Python | Core programming language |
| Flask | Lightweight web framework |
| HTML + CSS | User interface and styling |
| `session` | Handle user sessions |
| File I/O | Simulated database for users and tasks |
| Google Fonts | For beautiful typography |

---

## 💡 Features

### 🔐 User Authentication
- Secure sign-up form with validation rules:
  - Unique email, username, phone
  - Password must include special characters and meet minimum length
- Log in with persistent session
- Error messages for invalid or duplicate input

### 📋 Task Management
- Users can:
  - Add tasks
  - View their personal task list
  - Update task names
- All tasks are stored and linked to the user in `details.txt`

### 🎨 UI/UX Design
- Hand-coded frontend using HTML + inline CSS
- Use of Lobster font and color palettes to make it visually attractive
- Minimalist, clear, and readable layout for beginners and employers

---

## ✅ What I Learned

- The full flow of a Flask application from homepage to dashboard  
- Difference between GET and POST methods  
- Handling form data securely  
- Managing and storing data using files  
- Using session to persist user state  
- How to implement real-world user validations  

---

## 🛡️ Next Features

- 🔐 Encrypt passwords using `hashlib.sha256()`  
- 🔄 Refactor into modular files (blueprints or MVC)  
- 📦 Replace file storage with SQLite  
- 🧪 Write tests for routes and forms  

---

## 🎯 Why This Project Matters

This project shows:

- My ability to write clean and working code  
- My persistence in learning backend logic  
- My skills in turning a concept into a full product  
- That I can build useful web tools even without a team or full-stack experience  

I made this completely on my own, taking help only where absolutely needed to understand the logic — not to copy code.

---

## 📧 Contact Me

**Muhammad Ali Raffay**  
📩 [aliraffayofficial@gmail.com](mailto:aliraffayofficial@gmail.com)  
🌍 Based in Pakistan — looking for Werkstudent roles in Germany 🇩🇪  
💼 Fluent in Python, HTML, Flask, C++, and learning more every day.

---

## 📂 Project Files

```bash
├── CRUD Flask.py        # Full application logic and routing
├── details.txt          # Stores all user data and task lists
└── (Static/Template folders may be added in the future)
