import re

def assess_password_strength(password):
    # Initialize strength score
    strength_score = 0

    # Criteria weights
    length_weight = 1
    uppercase_weight = 1
    lowercase_weight = 1
    number_weight = 1
    special_char_weight = 2

    # Check length
    if len(password) >= 8:
        strength_score += length_weight
    if len(password) >= 12:
        strength_score += length_weight

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength_score += uppercase_weight

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength_score += lowercase_weight

    # Check for numbers
    if re.search(r'[0-9]', password):
        strength_score += number_weight

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength_score += special_char_weight

    # Determine strength level
    if strength_score >= 6:
        strength_level = "Strong"
    elif strength_score >= 4:
        strength_level = "Moderate"
    else:
        strength_level = "Weak"

    # Provide feedback
    feedback = []
    if len(password) < 8:
        feedback.append("Password should be at least 8 characters long.")
    if not re.search(r'[A-Z]', password):
        feedback.append("Password should contain at least one uppercase letter.")
    if not re.search(r'[a-z]', password):
        feedback.append("Password should contain at least one lowercase letter.")
    if not re.search(r'[0-9]', password):
        feedback.append("Password should contain at least one number.")
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        feedback.append("Password should contain at least one special character.")

    return strength_level, feedback

def main():
    password = input("Enter your password: ")
    strength_level, feedback = assess_password_strength(password)
    print(f"Password Strength: {strength_level}")
    if feedback:
        print("Feedback:")
        for item in feedback:
            print(f"- {item}")

if __name__ == "__main__":
    main()
