import string

def evaluate_password(password: str):
    score = 0
    suggestions = []

    length = len(password)

    # Length check
    if length >= 16:
        score += 3
    elif length >= 12:
        score += 2
    elif length >= 8:
        score += 1
    else:
        suggestions.append("Use at least 12 characters (16+ is ideal).")

    # Character sets
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

    # Repetition / simple patterns
    if password.lower() in ("password", "qwerty", "123456", "admin"):
        score -= 3
        suggestions.append("Avoid common passwords or simple patterns.")

    if len(set(password)) <= 3:
        score -= 2
        suggestions.append("Avoid repeating the same few characters.")

    # Final strength label
    if score >= 7:
        strength = "Very Strong 💪"
    elif score >= 5:
        strength = "Strong ✅"
    elif score >= 3:
        strength = "Medium ⚠️"
    else:
        strength = "Weak ❌"

    return strength, score, suggestions


def main():
    print("🔐 Password Strength Checker")
    print("-" * 32)
    print("This tool is for learning only. Do not paste real passwords here.")
    print()

    password = input("Enter a test password: ")

    if not password:
        print("No input provided. Exiting.")
        return

    strength, score, suggestions = evaluate_password(password)

    print("\n🔎 Result")
    print(f"Score   : {score}/8")
    print(f"Strength: {strength}")

    if suggestions:
        print("\n💡 Suggestions to improve:")
        for s in suggestions:
            print(f"- {s}")
    else:
        print("\nNice! Your test password already looks strong.")


if __name__ == "__main__":
    main()
