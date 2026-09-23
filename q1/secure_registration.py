# PSHS Secure Club Registration System

VALID_SECTION = "Dahlia"
VALID_CLUBS = ["Robotics", "Science", "Mathematics", "Programming"]
VALID_ATTENDANCE = ["Present", "Absent", "Late"]

student_name = input("Student Name: ").strip()

if student_name == "":
    print("Error: Student name is required.")
    exit()

section = input("Section: ").strip()

if section != VALID_SECTION:
    print("Error: Please enter a valid section.")
    exit()

club = input("Club Choice: ").strip()

if club not in VALID_CLUBS:
    print("Error: Please choose a valid club.")
    exit()

email = input("School Email: ").strip()

if "@" not in email or "." not in email:
    print("Error: Please enter a valid email address.")
    exit()

attendance = input("Attendance Status: ").strip()

if attendance not in VALID_ATTENDANCE:
    print("Error: Please enter a valid attendance status.")
    exit()

print("--------------------------------")
print("REGISTRATION ACCEPTED")
print("--------------------------------")
print("Student:", student_name)
print("Section:", section)
print("Club:", club)
print("Email:", email)
print("Attendance:", attendance)
