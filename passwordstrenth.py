"""
=========================================================
Project Title : Password Strength Checker
Author        : avinash kumar mandal
Internship    : Python / Cyber Security Internship
Language      : Python 3.x

Description:
------------
This program evaluates the strength of a password based
on commonly accepted security rules.

Features:
---------
1. Checks minimum password length.
2. Checks for uppercase letters.
3. Checks for lowercase letters.
4. Checks for digits.
5. Checks for special characters.
6. Provides password strength rating.
7. Suggests improvements to create a stronger password.

Note:
-----
This project is intended for educational purposes.
=========================================================
"""

import re
import getpass


# -------------------------------------------------------
# Function: Check Password Strength
# -------------------------------------------------------

def check_password_strength(password):
    """
    Evaluates password strength.

    Parameters:
        password (str): User entered password

    Returns:
        score (int): Password score
        feedback (list): Suggestions and analysis
    """

    score = 0
    feedback = []

    # Check password length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check uppercase letter
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Check lowercase letter
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Check digit
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    # Check special character
    if re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>/?]", password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    return score, feedback


# -------------------------------------------------------
# Function: Display Password Strength
# -------------------------------------------------------

def display_result(score, feedback):

    print("\n===================================")
    print("Password Analysis")
    print("===================================")

    if score == 5:
        print("Password Strength : VERY STRONG")
    elif score == 4:
        print("Password Strength : STRONG")
    elif score == 3:
        print("Password Strength : MEDIUM")
    elif score == 2:
        print("Password Strength : WEAK")
    else:
        print("Password Strength : VERY WEAK")

    print("\nSuggestions:")

    if not feedback:
        print("Excellent! Your password follows all recommended security rules.")
    else:
        for item in feedback:
            print(f"- {item}")


# -------------------------------------------------------
# Main Function
# -------------------------------------------------------

def main():

    print("=" * 45)
    print("        PASSWORD STRENGTH CHECKER")
    print("=" * 45)

    # Password will not be visible while typing
    password = getpass.getpass("Enter Password: ")

    score, feedback = check_password_strength(password)

    display_result(score, feedback)


# -------------------------------------------------------
# Program Entry Point
# -------------------------------------------------------

if __name__ == "__main__":
    main()