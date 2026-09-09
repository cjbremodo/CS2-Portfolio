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

Set valid to TRUE

IF student name is blank
    Display "Student name is required."
    Set valid to FALSE
END IF

Try converting age to integer
    IF age is less than 11 OR greater than 18
        Display "Age must be from 11 to 18."
        Set valid to FALSE
    END IF
Catch error
    Display "Age must be a number."
    Set valid to FALSE
END TRY

IF grade level is not 7,8,9,10,11,12
    Display "Invalid grade level."
    Set valid to FALSE
END IF

IF email does not contain @ OR .
    Display "Invalid email address."
    Set valid to FALSE
END IF

IF registration code length is not 6
    Display "The registration code must contain exactly 6 characters."
    Set valid to FALSE
END IF

IF valid is TRUE
    Display REGISTRATION ACCEPTED
    Display student information
ELSE
    Display REGISTRATION NOT ACCEPTED
END IF

END

### Part C
[workshop_validator.py](workshop_validator.py)
