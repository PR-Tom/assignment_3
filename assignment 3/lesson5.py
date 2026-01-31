# Credentials
CORRECT_USER = "python"
CORRECT_PASS = "rules"

attempts = 5

print("--- System Login ---")

while attempts > 0:
    user = input("Username: ")
    pw = input("Password: ")

    if user == CORRECT_USER and pw == CORRECT_PASS:
        print("\nWelcome!")
        break

    attempts -= 1

    if attempts > 0:
        print(f"Login failed. {attempts} attempts remaining.\n")
    else:
        print("\nAccess denied. Please contact your administrator.")
