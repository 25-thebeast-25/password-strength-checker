"""
Password Strength Checker

Evaluates password strength using rule-based heuristics
and provides suggestions for improvement.

This tool does NOT store, hash, or transmit passwords.
It is intended for educational and demonstration purposes only.
"""

import string

# =========================
# Configuration Constants
# =========================
MIN_LENGTH = 8
GOOD_LENGTH = 12
STRONG_LENGTH = 16

MAX_SCORE = 8

COMMON_PASSWORDS = {
    "password",
    "qwerty",
    "123456",
    "admin"
}


def evaluate_password(password: str):
    """
    Evaluate the strength of a given password and return
    a strength label, score, and improvement suggestions.
    """
    score = 0
    suggestions = []

    length = len(password)

    # -------------------------
    # Length Check
    # -------------------------
    if length >= STRONG_LENGTH:
        score += 3
    elif length >= GOOD_LENGTH:
        score += 2
    elif length >= MIN_LENGTH:
        score += 1
    else:
        suggestions.append(
            f"Use at least {GOOD_LENGTH} characters ({STRONG_LENGTH}+ is ideal)."
        )

    # -------------------------
    # Character Variety Checks
    # -------------------------
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    if has_lower:
        score += 1
    else:
        suggestions.append("Add some lowercase letters (a–z).")

    if has_upper:
        score += 1
    else:
        suggestions.append("Add some uppercase letters (A–Z).")

    if has_digit:
        score += 1
    else:
        suggestions.append("Include digits (0–9).")

    if has_symbol:
        score += 2
    else:
        suggestions.append("Include special characters (e.g. !@#$%^&*).")

    # -------------------------
    # Weak Pattern Detection
    # -------------------------
    if password.lower() in COMMON_PASSWORDS:
        score -= 3
        suggestions.append("Avoid common passwords or simple patterns.")

    if len(set(password)) <= 3:
        score -= 2
        suggestions.append("Avoid repeating the same few characters.")

    # -------------------------
    # Score Normalization
    # -------------------------
    score = max(0, min(score, MAX_SCORE))

    # -------------------------
    # Strength Classification
    # -------------------------
    if score >= 7:
        strength = "Very Strong 💪"
    elif score >= 5:
        strength = "Strong ✅"
    elif score >= 3:
        strength = "Medium ⚠️"
    else:
        strength = "Weak ❌"

    # In real systems, password strength checks should be combined
    # with secure hashing (bcrypt/argon2), rate limiting, and MFA.
    return strength, score, suggestions


def main():
    print("🔐 Password Strength Checker")
    print("-" * 32)
    print("This tool is for learning only. Do not paste real passwords here.\n")

    password = input("Enter a test password: ").strip()

    if not password:
        print("No input provided. Exiting.")
        return

    strength, score, suggestions = evaluate_password(password)

    print("\n🔎 Result")
    print(f"Score   : {score}/{MAX_SCORE}")
    print(f"Strength: {strength}")

    if suggestions:
        print("\n💡 Suggestions to improve:")
        for suggestion in suggestions:
            print(f"- {suggestion}")
    else:
        print("\nNice! Your test password already looks strong.")


if __name__ == "__main__":
    main()
