# PSHS Workshop Registration Validator

name = input("Enter student name: ")
age_input = input("Enter age: ")
grade = input("Enter grade level: ")
email = input("Enter email: ")
code = input("Enter registration code: ")

valid = True

# Student Name Validation
if name.strip() == "":
    print("Student name is required.")
    valid = False

# Age Validation
try:
    age = int(age_input)
    if age < 11 or age > 18:
        print("Age must be from 11 to 18.")
        valid = False
except ValueError:
    print("Age must be a number.")
    valid = False

# Grade Level Validation
if grade not in ["7", "8", "9", "10", "11", "12"]:
    print("Invalid grade level.")
    valid = False

# Email Validation
if "@" not in email or "." not in email:
    print("Invalid email address.")
    valid = False

# Registration Code Validation
if len(code) != 6:
    print("The registration code must contain exactly 6 characters.")
    valid = False

# Final Output
if valid:
    print("------------------------------")
    print("REGISTRATION ACCEPTED")
    print("------------------------------")
    print(f"Student: {name}")
    print(f"Age: {age}")
    print(f"Grade Level: {grade}")
    print(f"Email: {email}")
    print(f"Registration Code: {code}")
else:
    print("REGISTRATION NOT ACCEPTED")
