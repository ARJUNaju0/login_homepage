# 🔐 Django Custom Login System

This is a basic Django web application that implements user **registration**, **login**, **logout**, and a **home page** displaying other registered users. It uses a **custom `Login` model** instead of Django's default `User` model.

---

## 📌 Features

- Register new users with password confirmation
- Secure password hashing using Django's `make_password` and `check_password`
- Manual session management (stores user ID and username in session)
- Redirect users to a personalized home page after login
- Logout functionality to clear user sessions
- Displays other users (excluding the currently logged-in one)

---

## 🛠️ Tech Stack

- **Backend:** Django
- **Database:** Default SQLite (can be swapped with MySQL/PostgreSQL)
- **Frontend:** HTML (Django Templates), CSS (optional)
