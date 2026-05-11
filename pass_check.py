import re

common_passwords = ["123456", "password", "admin", "qwerty"]

password = input("Enter Password: ")

score = 0

# Length Check
if len(password) >= 8:
    score += 1

# Uppercase Check
if re.search(r"[A-Z]", password):
    score += 1

# Lowercase Check
if re.search(r"[a-z]", password):
    score += 1

# Number Check
if re.search(r"[0-9]", password):
    score += 1

# Special Character Check
if re.search(r"[@$!%*?&]", password):
    score += 1

# Common Password Check
if password.lower() in common_passwords:
    score = 0

# Result
if score <= 2:
    print("Weak Password")
elif score == 3 or score == 4:
    print("Medium Password")
else:
    print("Strong Password")