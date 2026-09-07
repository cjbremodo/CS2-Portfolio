### Clean Decision Code Makeover: Student Score Checker

**Name:** Cassandra Jade B. Remodo  
**Section:** 8 - Dahlia



### Activity Overview

In this activity, I improved a Student Score Checker program by applying proper coding standards and selection structures.

The program accepts a student score from 0 to 100 and determines the appropriate classification.

The classifications are:

| Score | Classification |
|--------|----------------|
| 90–100 | Outstanding |
| 80–89 | Very Satisfactory |
| 75–79 | Satisfactory |
| 0–74 | Needs Improvement |

Scores below 0 or above 100 are considered invalid.



### Part 1 - Analyze the Logic

#### Input

What information does the program need?

> The program needs a student's score.

#### Valid Range

**Minimum valid score:**

> 0

**Maximum valid score:**

> 100

#### Possible Outputs

List all possible outputs of the program.

1. Invalid Score.
2. Outstanding
3. Very Satisfactory
4. Satisfactory
5. Needs Improvement

#### Boundary Condition

What condition will you use to determine whether the score is valid?

> The score must be between 0 and 100 inclusive. If the score is less than 0 or greater than 100, it is invalid.

#### Multiple Decision Paths

Explain how the program decides which classification should be displayed.

> The program uses an if-elif-else structure to compare the score against different score ranges and display the correct classification.



### Part 2 - Flowchart

#### Flowchart

```text
 ┌───────┐
 │ START │
 └───┬───┘
     │
     ▼
┌──────────────┐
│ Input Score  │
└──────┬───────┘
       │
       ▼
┌──────────────────┐
│ Score < 0 OR     │
│ Score > 100 ?    │
└───┬─────────┬────┘
   Yes        No
    │          │
    ▼          ▼
┌──────────┐  ┌─────────────┐
│ Invalid  │  │ Score >= 90?│
│ Score    │  └───┬─────┬───┘
└────┬─────┘     Yes    No
     │            │      │
     ▼            ▼      ▼
    END    Outstanding  Score >= 80?
                          │
                   ┌──────┴─────┐
                  Yes          No
                   │            │
                   ▼            ▼
         Very Satisfactory   Score >= 75?
                               │
                       ┌───────┴──────┐
                      Yes            No
                       │              │
                       ▼              ▼
                 Satisfactory   Needs Improvement
                       │              │
                       └──────┬───────┘
                              ▼
                             END
```



### Part 3 - Pseudocode

```text
START

INPUT score

IF score < 0 OR score > 100 THEN
    DISPLAY "Invalid Score."

ELSE IF score >= 90 THEN
    DISPLAY "Outstanding"

ELSE IF score >= 80 THEN
    DISPLAY "Very Satisfactory"

ELSE IF score >= 75 THEN
    DISPLAY "Satisfactory"

ELSE
    DISPLAY "Needs Improvement"

END
```



### Part 4 - Clean Code Implementation

#### Source Code

```python
# PSHS Student Score Checker
# This program validates a student's score and
# displays the appropriate performance classification.

student_score = int(input("Enter student score (0-100): "))

if student_score < 0 or student_score > 100:
    print("Invalid Score.")

elif student_score >= 90:
    print("Outstanding")

elif student_score >= 80:
    print("Very Satisfactory")

elif student_score >= 75:
    print("Satisfactory")

else:
    print("Needs Improvement")
```



### Part 5 - Testing

| Test | Input | Purpose | Expected Output | Actual Output | Result |
|------|------:|----------|----------------|---------------|--------|
| 1 | -1 | Below minimum | Invalid Score. | Invalid Score. | PASS |
| 2 | 0 | Minimum boundary | Needs Improvement | Needs Improvement | PASS |
| 3 | 74 | Below Satisfactory boundary | Needs Improvement | Needs Improvement | PASS |
| 4 | 75 | Satisfactory boundary | Satisfactory | Satisfactory | PASS |
| 5 | 80 | Very Satisfactory boundary | Very Satisfactory | Very Satisfactory | PASS |
| 6 | 90 | Outstanding boundary | Outstanding | Outstanding | PASS |
| 7 | 100 | Maximum boundary | Outstanding | Outstanding | PASS |
| 8 | 101 | Above maximum | Invalid Score. | Invalid Score. | PASS |



#### Testing Reflection

##### 1. Why is it important to test the values 0 and 100?

> They are the minimum and maximum valid scores, so testing them ensures the program handles boundary values correctly.

####3 2. Why did you also test -1 and 101?

> They are outside the valid range and help verify that invalid scores are detected properly.

##### 3. Which test helped you understand boundary conditions the most?

> The tests using 0, 75, 80, 90, and 100 helped me understand how boundary values affect classification.

##### 4. Did any of your tests initially fail? If yes, what did you change in your program?

> No. All tests passed after adding score validation and proper decision structures.



### Reflection

##### 1. How did selection structures make the program more useful?

> Selection structures allowed the program to display different outputs based on the user's score.

##### 2. How did proper comments and readable formatting improve your program?

> They made the code easier to read, understand, and maintain.

##### 3. Why is it useful to plan the program using a flowchart and pseudocode before writing the code?

> They help organize the program logic and reduce mistakes before coding.
