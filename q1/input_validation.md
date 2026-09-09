### Workshop Validator
#### Part A
| Data Captured     | Expected Input | Validation Type              | Invalid Input Example | Validation Rule                   | Error Message                                            |
| ----------------- | -------------- | ---------------------------- | --------------------- | --------------------------------- | -------------------------------------------------------- |
| Student Name      | Text           | Presence Validation          | Blank input           | Must not be empty                 | Student name is required.                                |
| Age               | Integer        | Data Type & Range Validation | fourteen              | Must be a number from 11–18       | Age must be a number.                                    |
| Age               | Integer        | Range Validation             | 25                    | Must be between 11 and 18         | Age must be from 11 to 18.                               |
| Grade Level       | 7–12           | Acceptable Value Validation  | 13                    | Only 7–12 accepted                | Invalid grade level.                                     |
| Email Address     | Email          | Pattern Validation           | studentpshs.edu.ph    | Must contain @ and .              | Invalid email address.                                   |
| Registration Code | 6 characters   | Length Validation            | ABC                   | Must contain exactly 6 characters | The registration code must contain exactly 6 characters. |


#### Part B
Pseudocode
START

Input student name
Input age
Input grade level
Input email
Input registration code

Set valid = TRUE

IF student name is blank
    Display "Student name is required."
    Set valid = FALSE
END IF

TRY
    Convert age to integer

    IF age < 11 OR age > 18
        Display "Age must be from 11 to 18."
        Set valid = FALSE
    END IF

CATCH error
    Display "Age must be a number."
    Set valid = FALSE
END TRY

IF grade level is not 7, 8, 9, 10, 11, or 12
    Display "Invalid grade level."
    Set valid = FALSE
END IF

IF email does not contain '@' OR '.'
    Display "Invalid email address."
    Set valid = FALSE
END IF

IF registration code length is not 6
    Display "The registration code must contain exactly 6 characters."
    Set valid = FALSE
END IF

IF valid = TRUE
    Display "REGISTRATION ACCEPTED"
    Display student information
ELSE
    Display "REGISTRATION NOT ACCEPTED"
END IF

END

### Part C
[workshop_validator.py](workshop_validator.py)

### Part D and E
| Test | Input / Condition                                                                               | Validation Being Tested | Expected Output                                          | Actual Output                                            | Result |
| ---: | ----------------------------------------------------------------------------------------------- | ----------------------- | -------------------------------------------------------- | -------------------------------------------------------- | ------ |
|    1 | Name=Cassandra, Age=14, Grade=8, Email=[cass@example.com](mailto:cass@example.com), Code=CS2026 | Normal case             | REGISTRATION ACCEPTED                                    | REGISTRATION ACCEPTED                                    | PASS   |
|    2 | Blank student name                                                                              | Presence                | Student name is required.                                | Student name is required.                                | PASS   |
|    3 | Age = fourteen                                                                                  | Data type               | Age must be a number.                                    | Age must be a number.                                    | PASS   |
|    4 | Age = 11                                                                                        | Minimum boundary        | REGISTRATION ACCEPTED                                    | REGISTRATION ACCEPTED                                    | PASS   |
|    5 | Age = 18                                                                                        | Maximum boundary        | REGISTRATION ACCEPTED                                    | REGISTRATION ACCEPTED                                    | PASS   |
|    6 | Age = 10                                                                                        | Range                   | Age must be from 11 to 18.                               | Age must be from 11 to 18.                               | PASS   |
|    7 | Grade Level = 13                                                                                | Acceptable Value        | Invalid grade level.                                     | Invalid grade level.                                     | PASS   |
|    8 | Email = studentpshs.edu.ph                                                                      | Pattern                 | Invalid email address.                                   | Invalid email address.                                   | PASS   |
|    9 | Registration Code = ABC                                                                         | Length                  | The registration code must contain exactly 6 characters. | The registration code must contain exactly 6 characters. | PASS   |
|   10 | Registration Code = CS2026                                                                      | Valid length            | REGISTRATION ACCEPTED                                    | REGISTRATION ACCEPTED                                    | PASS   |

