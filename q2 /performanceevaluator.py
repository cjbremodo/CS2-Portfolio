def calculate_average(score1, score2, score3):
    return (score1 + score2 + score3) / 3


def get_performance(average):
    if average >= 85:
        return "Mastery"
    elif average >= 70:
        return "Developing"
    else:
        return "Needs Review"


def is_eligible(average, completed_tasks):
    return average >= 85 and completed_tasks >= 3


score1 = float(input("Enter Score 1: "))
score2 = float(input("Enter Score 2: "))
score3 = float(input("Enter Score 3: "))
completed_tasks = int(input("Completed Tasks: "))

average = calculate_average(score1, score2, score3)
performance = get_performance(average)
eligible = is_eligible(average, completed_tasks)

print(f"Average: {average:.2f}")
print(f"Performance: {performance}")
print(f"Eligible for Challenge: {eligible}")

# DOCUMENTATION

# 1. calculate_average() returns a number, get_performance() returns a string, and is_eligible() returns True or False.

# 2. calculate_average() returns the average, which is passed to get_performance().

# 3. The student is not eligible because they completed fewer than 3 tasks.

# 4. return lets the program reuse the result, while print() only displays it.
