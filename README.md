# 🔐 Password Strength Checker

A Python-based tool that evaluates password strength and explains **why**
a password is weak or strong, along with practical suggestions to improve it.

This project is designed to demonstrate how password policies work in real
authentication systems and why weak passwords remain a major security risk.

> ⚠️ For learning and demonstration purposes only  
> Do **not** test real or sensitive passwords

---

## 🎯 What This Project Demonstrates

- How password strength is evaluated programmatically
- Common weaknesses users introduce in passwords
- Why relying only on password length is insufficient
- How feedback can guide users toward safer credentials

This mirrors basic logic used in real-world systems before hashing and storage.

---

## 🚀 Features

- Scores password strength based on multiple factors:
  - Length
  - Uppercase & lowercase usage
  - Digits
  - Special characters
- Detects common weak patterns
- Provides **human-readable suggestions** for improvement
- Simple CLI-based interface (runs in any terminal)

---

## 🧠 How Strength Is Evaluated

Each password is analyzed using rule-based checks:
- Short or predictable passwords reduce the score
- Variety in character types increases strength
- Common patterns and weak structures are penalized

The final output explains both the **score** and the **reasoning** behind it.

---

## ▶️ How to Run

```bash
python password_strength_checker.py
