# Workshop Validator
def get_user_name():
    while True:
        try:
            name = input("Please enter your name: ")
            if not name.strip():
                raise ValueError("Name cannot be blank.")
            return name.strip()
        except ValueError as e:
            print(f"Invalid input: {e} Please try again.\n")

def get_user_age():
    while True:
        age_input = input("Please enter your age (11-18): ").strip()
        if age_input.isdigit() and 11 <= int(age_input) <= 18:
            return int(age_input)
        print("Invalid input: Please enter a number between 11 and 18.\n")

def get_grade_level():
    while True:
        grade = input("Enter your grade level (7-12): ").strip()
        if grade.isdigit() and 7 <= int(grade) <= 12:
            return int(grade)
        print("Invalid input: Please enter a grade between 7 and 12.\n")

def get_user_email():
    while True:
        email = input("Please enter your email: ").strip()
        if email.endswith("@brc.pshs.edu.ph") and len(email.split("@")[0]) > 0:
            return email
        print("Invalid email. Must be your unique handle followed by @brc.pshs.edu.ph\n")

def get_registration_code():
    while True:
        code = input("Please enter your 6-character registration code: ").strip()
        if len(code) == 6:
            return code
        print("Invalid code. Registration code must be exactly 6 characters long.\n")

# --- Execution Sequence ---
print("--- PSHS BRC Student Registration ---\n")
user_name = get_user_name()
user_age = get_user_age()
user_grade = get_grade_level()
user_email = get_user_email()
user_code = get_registration_code() # Ensures the registration code executes

print("\n--- Registration Complete ---")
print(f"Name: {user_name}")
print(f"Age: {user_age}")
print(f"Grade: {user_grade}")
print(f"Email: {user_email}")
print(f"Registration Code: {user_code}")
