
**Name:** Cassandra Jade B. Remodo
**Section:** 8 - Dahlia

**Activity Overview**

I improved a Student Score Checker program using selection structures and proper coding practices. The program accepts a score from 0 to 100 and displays the correct classification. Scores outside this range are invalid.

| Score  | Classification    |
| ------ | ----------------- |
| 90-100 | Outstanding       |
| 80-89  | Very Satisfactory |
| 75-79  | Satisfactory      |
| 0-74   | Needs Improvement |

**Part 1 - Analyze the Logic**

**Input:** A student's score.

**Valid Range**

* Minimum: 0
* Maximum: 100

**Possible Outputs**

1. Invalid Score.
2. Outstanding
3. Very Satisfactory
4. Satisfactory
5. Needs Improvement

**Boundary Condition:** The score must be between 0 and 100 inclusive.

**Multiple Decision Paths:** The program uses if-elif-else statements to determine the correct classification.

**Part 2 - Flowchart**

![Score Checker Flowchart](./score_checker_flowchart.png)

**Part 3 - Pseudocode**

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

**Part 4 - Clean Code Implementation**

# PSHS Student Score Checker
# This program validates a student's score and
# displays the appropriate performance classification.

# Ask the user to enter a score
student_score = int(input("Enter student score (0-100): "))

# Validate that the score is within the allowed range
if student_score < 0 or student_score > 100:
    print("Invalid Score.")

# Determine the performance classification
elif student_score >= 90:
    print("Outstanding")

elif student_score >= 80:
    print("Very Satisfactory")

elif student_score >= 75:
    print("Satisfactory")

else:
    print("Needs Improvement")

**Part 5 - Testing**

| Test | Input | Purpose                     | Expected Output   | Actual Output     | Result |
| ---- | ----: | --------------------------- | ----------------- | ----------------- | ------ |
| 1    |    -1 | Below minimum               | Invalid Score.    | Invalid Score.    | PASS   |
| 2    |     0 | Minimum boundary            | Needs Improvement | Needs Improvement | PASS   |
| 3    |    74 | Below Satisfactory boundary | Needs Improvement | Needs Improvement | PASS   |
| 4    |    75 | Satisfactory boundary       | Satisfactory      | Satisfactory      | PASS   |
| 5    |    80 | Very Satisfactory boundary  | Very Satisfactory | Very Satisfactory | PASS   |
| 6    |    90 | Outstanding boundary        | Outstanding       | Outstanding       | PASS   |
| 7    |   100 | Maximum boundary            | Outstanding       | Outstanding       | PASS   |
| 8    |   101 | Above maximum               | Invalid Score.    | Invalid Score.    | PASS   |

**Testing Reflection**

**1. Why is it important to test 0 and 100?**
They are the minimum and maximum valid scores.

**2. Why did you also test -1 and 101?**
They check whether invalid scores are handled correctly.

**3. Which test helped you understand boundary conditions the most?**
The tests using 0, 75, 80, 90, and 100.

**4. Did any tests initially fail? If yes, what did you change?**
No. All tests passed.

**Reflection**

**1. How did selection structures make the program more useful?**
They allow different outputs based on the score entered.

**2. How did proper comments and formatting improve your program?**
They made the code easier to read and understand.

**3. Why is it useful to plan with a flowchart and pseudocode first?**
They help organize the logic before coding.
