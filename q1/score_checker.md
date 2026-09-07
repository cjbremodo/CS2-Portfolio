## Clean Decision Code Makeover: Student Score Checker

**Name:** Cassandra Jade B. Remodo
**Section:** 8 - Dahlia

## Activity Overview

I improved a Student Score Checker program using selection structures and proper coding practices.

| Score  | Classification    |
| ------ | ----------------- |
| 90-100 | Outstanding       |
| 80-89  | Very Satisfactory |
| 75-79  | Satisfactory      |
| 0-74   | Needs Improvement |

Scores below 0 or above 100 are invalid.

## Part 1 - Analyze the Logic

### Input

> A student's score.

### Valid Range

**Minimum:** 0

**Maximum:** 100

### Possible Outputs

1. Invalid Score.
2. Outstanding
3. Very Satisfactory
4. Satisfactory
5. Needs Improvement

### Boundary Condition

> The score must be between 0 and 100.

### Multiple Decision Paths

> The program uses if-elif-else statements to determine the correct classification.

## Part 2 - Flowchart

Paste your flowchart image here.

## Part 3 - Pseudocode

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

## Part 4 - Clean Code Implementation

Insert your Python source code or screenshot here.

## Part 5 - Testing

| Test | Input | Expected Output   | Actual Output     | Result |
| ---- | ----: | ----------------- | ----------------- | ------ |
| 1    |    -1 | Invalid Score.    | Invalid Score.    | PASS   |
| 2    |     0 | Needs Improvement | Needs Improvement | PASS   |
| 3    |    74 | Needs Improvement | Needs Improvement | PASS   |
| 4    |    75 | Satisfactory      | Satisfactory      | PASS   |
| 5    |    80 | Very Satisfactory | Very Satisfactory | PASS   |
| 6    |    90 | Outstanding       | Outstanding       | PASS   |
| 7    |   100 | Outstanding       | Outstanding       | PASS   |
| 8    |   101 | Invalid Score.    | Invalid Score.    | PASS   |

### Testing Reflection

1. Why is it important to test 0 and 100?

> They are the boundary values of the valid range.

2. Why test -1 and 101?

> They check if invalid scores are detected.

3. Which test helped you understand boundary conditions the most?

> The tests using 0, 75, 80, 90, and 100.

4. Did any tests fail?

> No. All tests passed.

## Reflection

1. How did selection structures make the program more useful?

> They allow different outputs for different scores.

2. How did comments and formatting improve the program?

> They made the code easier to read.

3. Why use a flowchart and pseudocode first?

> They help plan the program before coding.
