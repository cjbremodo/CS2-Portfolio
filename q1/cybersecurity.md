# Fundamentals of Cybersecurity and Data Privacy

**Activity:** PSHS Secure Club Registration System
**Name:** Cassandra Jade B. Remodo
**Section:** 8 - Dahlia
**Quarter:** 1

---

# Part A - Cybersecurity Threat Analysis

## Assigned Case

**Case Number:** 1
**Case Title:** Fake Login Alert

> A message claims that the student's account will be disabled and asks them to click a link and enter their username and password.

### 1. What cybersecurity threat is shown?

> The threat is phishing. The attacker pretends to be an organization or company to trick users into giving their login credentials.

### 2. What warning signs make the situation suspicious?

> The message creates urgency, threatens account deactivation, asks for sensitive information, and contains a suspicious link.

### 3. What may be affected?

* Data
* Account
* Device
* Network

> If the user enters their credentials, attackers may gain access to personal information and school accounts. Malware could also be installed on the device.

### 4. What information could be exposed or misused?

> Usernames, passwords, personal information, school records, and account data could be exposed or stolen.

### 5. What should the user do to reduce the risk?

> The user should not click the link, should verify the message through official channels, and should report the suspicious message.

### 6. What mitigation can reduce the risk?

> User awareness training, strong passwords, multi-factor authentication, and careful verification of links can reduce the risk.

---

# Part B - Data Privacy and Secure Data Capture

A proposed Club Registration System wants to collect the following information.

| Data                | Collect / Do Not Collect | Reason                                                             |
| ------------------- | ------------------------ | ------------------------------------------------------------------ |
| Student Name        | Collect                  | Needed to identify the student.                                    |
| Section             | Collect                  | Needed to determine the student's section.                         |
| Club Choice         | Collect                  | Needed for club registration.                                      |
| School Email        | Collect                  | Needed for communication and verification.                         |
| Attendance Status   | Collect                  | Needed for activity records.                                       |
| Password            | Do Not Collect           | Not necessary for club registration and may create security risks. |
| OTP                 | Do Not Collect           | Not required for the activity and should remain private.           |
| Home Address        | Do Not Collect           | Unnecessary for a simple registration activity.                    |
| Parent Bank Account | Do Not Collect           | Sensitive financial information that is not needed.                |

## Privacy Question

Why is it safer to collect only information that the program actually needs?

> Collecting only necessary information reduces privacy risks and limits the amount of sensitive data that could be exposed if a security incident occurs.

---

# Part C - Security-Focused Validation Rules

| Data Captured     | Expected Input                              | Possible Risk                 | Invalid Input Example | Validation Rule                 | Error Message                           |
| ----------------- | ------------------------------------------- | ----------------------------- | --------------------- | ------------------------------- | --------------------------------------- |
| Student Name      | Valid student name                          | Missing identification        | Blank input           | Must not be blank               | Student name is required.               |
| Section           | Dahlia                                      | Incorrect records             | Rose                  | Must match allowed section      | Please enter a valid section.           |
| Club Choice       | Robotics, Science, Mathematics, Programming | Incorrect registration        | Gaming                | Must be from approved club list | Please choose a valid club.             |
| School Email      | Valid school email                          | Incorrect contact information | studentpshs.edu.ph    | Must contain @ and .            | Please enter a valid email address.     |
| Attendance Status | Present, Absent, Late                       | Incorrect attendance records  | Excused               | Must match approved values      | Please enter a valid attendance status. |

## Secure Data Capture Questions

### 1. What should your program accept?

> The program should accept only valid student names, approved sections, approved club choices, valid school emails, and valid attendance statuses.

### 2. What should your program reject?

> The program should reject blank names, invalid sections, unapproved clubs, improperly formatted emails, and invalid attendance statuses.

### 3. How do your validation rules help reduce incorrect or unsafe input?

> Validation rules ensure that only expected and appropriate information is accepted, reducing mistakes and improving data quality.

---

# Part D - Secure Program Implementation

## Program

### Source Code File: secure_registration.py

```python
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
```

## Security Practices Applied

### Required Input

> Blank student names are rejected to ensure that every registration identifies a student.

### Allowed Values

> The section, club choice, and attendance status are limited to predefined values.

### Format Check

> The email must contain both "@" and "." to meet the required format.

### Error Messages

> Clear error messages help users understand what needs to be corrected.

### Data Minimization

> The program intentionally does not collect passwords, OTPs, banking information, or home addresses because they are unnecessary for the activity.

---

# Part E - Testing and Reflection

## Testing

| Test | Input Situation           | Expected Output       | Actual Output         | Result |
| ---: | ------------------------- | --------------------- | --------------------- | ------ |
|    1 | All data valid            | Registration accepted | Registration accepted | PASS   |
|    2 | Blank student name        | Rejected              | Rejected              | PASS   |
|    3 | Invalid section           | Rejected              | Rejected              | PASS   |
|    4 | Invalid club choice       | Rejected              | Rejected              | PASS   |
|    5 | Email missing @           | Rejected              | Rejected              | PASS   |
|    6 | Email missing .           | Rejected              | Rejected              | PASS   |
|    7 | Invalid attendance status | Rejected              | Rejected              | PASS   |
|    8 | Different valid inputs    | Accepted              | Accepted              | PASS   |

# Reflection

### 1. What is one cybersecurity threat that can affect an application or user?

> Phishing is a cybersecurity threat that tricks users into revealing sensitive information like login credentials.

### 2. How can users reduce the risk of phishing or suspicious messages?

> Users should verify messages, avoid clicking suspicious links, and never share passwords or usernames to sources they don't know.

### 3. How can validation rules improve the security of user input?

> Validation rules help ensure that only correct and expected information is accepted.

### 4. Why should a program avoid collecting unnecessary personal information?

> Collecting unnecessary information increases privacy and security risks.

### 5. How did SG7's input validation concepts become security practices in SG8?

> Input validation became a security practice by helping ensure that only appropriate, expected, and safe data is accepted by the program.

