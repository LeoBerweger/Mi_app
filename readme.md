# 🧠 TrackIt! – A Simple Habit Tracker (Flask App)

Welcome to **TrackIt!**, a lightweight web app that helps users build better habits and track their progress over time. This project is perfect for learning Flask, Python, and full-stack web development basics.

---

## 🚀 Project Overview

TrackIt! allows users to:
- Add and manage personal habits
- Mark them as completed each day
- Track daily progress and streaks
- View habit history in a clean dashboard

---

## 🛠️ Tech Stack

- **Python 3**
- **Flask** – lightweight backend framework
- **SQLite + SQLAlchemy** – for storing habits and check-ins
- **HTML + Jinja2** – templates for dynamic pages
- **Bootstrap** – for styling (optional)
- *(Optional: Chart.js or similar for graphs)*

---

## 🧩 Core Features (MVP)

| Feature | Description |
|--------|-------------|
| ✅ Add Habit | Create a new habit to track daily |
| 📅 Daily Tracker | Mark which habits were completed today |
| 🔄 Edit/Delete Habit | Change or remove a habit |
| 📊 View Streaks | See how consistent you've been |
| 🗓️ Habit History | Visualize which days you completed each habit |

---

## 🧭 Roadmap

### Phase 1: Setup & Basics
- [ ] Initialize Flask app
- [ ] Set up routes and templates
- [ ] Connect to SQLite database with SQLAlchemy

### Phase 2: Habit Management
- [ ] Add Habit form
- [ ] Display list of habits on homepage
- [ ] Delete/Edit a habit

### Phase 3: Daily Tracking
- [ ] Mark habits as complete/incomplete per day
- [ ] Track dates completed (use `HabitLog` model)
- [ ] Show daily progress

### Phase 4: Streaks & History
- [ ] Calculate current streak per habit
- [ ] Show longest streak
- [ ] Visualize history (optional calendar-style view or graph)

### Phase 5: Polish & Stretch Goals
- [ ] Add user authentication (Flask-Login)
- [ ] Use Chart.js or a simple graph to show trends
- [ ] Mobile-friendly layout
- [ ] Dark mode (just for fun 😎)

---

## 📁 Suggested Project Structure

```
trackit/
├── app.py
├── models.py
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── add_habit.html
│   └── history.html
├── static/
│   └── style.css
├── requirements.txt
└── README.md
```

---

## 🧪 How to Run It

1. Clone the repo
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the app:
    ```bash
    python app.py
    ```
4. Visit `http://127.0.0.1:5000` in your browser

---

## 🧠 What You'll Learn

- Building and routing Flask apps
- Working with templates and dynamic data
- Using databases with SQLAlchemy
- Handling forms and user input
- Structuring a real Python web project

---

Happy habit tracking! 💪
