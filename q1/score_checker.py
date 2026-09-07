# PSHS Student Score Checker
# This program validates a student's score and assigns
# a performance classification based on the score range.

# Ask the user to enter a student score.
score = int(input("Enter student score (0-100): "))

# Validate that the score is within the allowed range.
# Scores below 0 or above 100 are considered invalid.
if score < 0 or score > 100:
    print("Invalid Score.")

# Classify valid scores using multiple decision paths.
elif score >= 90:
    print("Outstanding")
elif score >= 80:
    print("Very Satisfactory")
elif score >= 75:
    print("Satisfactory")
else:
    print("Needs Improvement")

# 3. Why is it useful to plan the program using a flowchart
# and pseudocode before writing the code?
# A flowchart and pseudocode help organize the program's logic
# before coding. They make it easier to identify decisions,
# possible outputs, and errors before writing the actual program.
