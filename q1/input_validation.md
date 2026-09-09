### Workshop Validator
#### Part A







#### Part B
Pseudocode
START Program

  OUTPUT "--- PSHS BRC Student Registration ---"

  WHILE True
INPUT user_name
IF user_name is blank THEN
OUTPUT "Error: Name cannot be blank."
ELSE
 BREAK loop
 ENDIF
ENDWHILE

  WHILE True
INPUT user_age
IF user_age is a number AND user_age is between 11 and 18 THEN
BREAK loop
ELSE
 OUTPUT "Error: Age must be between 11 and 18."
ENDIF
ENDWHILE

  WHILE True
  INPUT user_grade
IF user_grade is a number AND user_grade is between 7 and 12 THEN
 BREAK loop
 ELSE
 OUTPUT "Error: Grade must be between 7 and 12."
ENDIF
ENDWHILE

  WHILE True
        INPUT user_email
        IF user_email ends with "@brc.pshs.edu.ph" AND has a handle THEN
            BREAK loop
        ELSE
            OUTPUT "Error: Invalid school email domain."
        ENDIF
    ENDWHILE

  WHILE True
        INPUT registration_code
        IF length of registration_code equals 6 THEN
            BREAK loop
        ELSE
            OUTPUT "Error: Code must be exactly 6 characters."
        ENDIF
    ENDWHILE

  OUTPUT "--- Registration Complete ---"
    PRINT user_name, user_age, user_grade, user_email, registration_code

END Programc

### Part C
[workshop_validator.py](workshop_validator.py)
