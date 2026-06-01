"""
=================================================
  DecodeLabs Cybersecurity Internship - Project 1
  Password Strength Checker
  Batch: 2026
=================================================
"""

import re

# ── Helpers ──────────────────────────────────────────────────────────────────

def check_length(password):
    """Returns True if password is at least 8 characters long."""
    return len(password) >= 8

def check_uppercase(password):
    """Returns True if password contains at least one uppercase letter."""
    return bool(re.search(r'[A-Z]', password))

def check_digit(password):
    """Returns True if password contains at least one digit (0-9)."""
    return bool(re.search(r'\d', password))

def check_symbol(password):
    """Returns True if password contains at least one special character."""
    return bool(re.search(r'[!@#$%^&*()_+\-=\[\]{};:\'",.<>?/\\|`~]', password))

def check_common(password):
    """Returns True if password is NOT in the list of common weak passwords."""
    common_passwords = [
        "password", "123456", "password123", "admin", "letmein",
        "welcome", "monkey", "dragon", "master", "qwerty",
        "abc123", "iloveyou", "sunshine", "princess", "football",
    ]
    return password.lower() not in common_passwords

# ── Core Logic ────────────────────────────────────────────────────────────────

def check_password_strength(password):
    """
    Evaluates a password and returns a dict with:
      - strength : 'Weak' | 'Medium' | 'Strong'
      - score    : number of criteria met (0-5)
      - feedback : list of tips for improvement
      - criteria : dict showing which checks passed/failed
    """
    criteria = {
        "At least 8 characters":          check_length(password),
        "Contains uppercase letter":       check_uppercase(password),
        "Contains a number":               check_digit(password),
        "Contains a special symbol":       check_symbol(password),
        "Not a commonly used password":    check_common(password),
    }

    score = sum(criteria.values())

    # Determine overall strength
    if not criteria["Not a commonly used password"]:
        strength = "Weak"          # always weak if it's a known bad password
    elif score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    # Build personalised feedback
    feedback = []
    if not criteria["At least 8 characters"]:
        feedback.append("→ Make it longer (8+ characters recommended).")
    if not criteria["Contains uppercase letter"]:
        feedback.append("→ Add at least one uppercase letter (A-Z).")
    if not criteria["Contains a number"]:
        feedback.append("→ Include at least one digit (0-9).")
    if not criteria["Contains a special symbol"]:
        feedback.append("→ Use a special character like !, @, #, $, etc.")
    if not criteria["Not a commonly used password"]:
        feedback.append("→ Avoid common passwords — they are easily guessed.")
    if not feedback:
        feedback.append("✓ Your password meets all recommended criteria!")

    return {
        "strength": strength,
        "score":    score,
        "criteria": criteria,
        "feedback": feedback,
    }

# ── Display ───────────────────────────────────────────────────────────────────

STRENGTH_STYLES = {
    "Weak":   ("🔴", "WEAK   ", "High Risk  "),
    "Medium": ("🟡", "MEDIUM ", "Moderate   "),
    "Strong": ("🟢", "STRONG ", "Low Risk   "),
}

def display_result(password, result):
    icon, label, risk = STRENGTH_STYLES[result["strength"]]

    print("\n" + "=" * 50)
    print("  DecodeLabs · Password Strength Checker")
    print("=" * 50)

    # Mask the password for display
    masked = password[0] + "*" * (len(password) - 2) + password[-1] if len(password) > 2 else "***"
    print(f"  Password  : {masked}")
    print(f"  Strength  : {icon}  {label}  |  Risk: {risk}")
    print(f"  Score     : {result['score']} / 5 criteria met")
    print("-" * 50)

    print("  Criteria Check:")
    for criterion, passed in result["criteria"].items():
        status = "✅" if passed else "❌"
        print(f"    {status}  {criterion}")

    print("-" * 50)
    print("  Feedback:")
    for tip in result["feedback"]:
        print(f"    {tip}")
    print("=" * 50 + "\n")

# ── Main Program ──────────────────────────────────────────────────────────────

def main():
    print("\n╔══════════════════════════════════════════════╗")
    print("║   DecodeLabs · Cybersecurity Internship 2026  ║")
    print("║   Project 1: Password Strength Checker        ║")
    print("╚══════════════════════════════════════════════╝\n")

    while True:
        password = input("Enter a password to test (or 'quit' to exit): ").strip()

        if password.lower() in ("quit", "exit", "q"):
            print("\nExiting. Keep building secure systems! 🛡\n")
            break

        if not password:
            print("  ⚠  Please enter a password.\n")
            continue

        result = check_password_strength(password)
        display_result(password, result)

        another = input("Test another password? (y/n): ").strip().lower()
        if another != "y":
            print("\nDone! Stay secure. 🔐\n")
            break
        print()

if __name__ == "__main__":
    main()