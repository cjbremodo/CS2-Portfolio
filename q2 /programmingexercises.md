# Python Loop Exercises

## Exercise 1: Count Even Numbers

Task: Display even numbers from 2 to 20 using a for loop.

```python
# Print even numbers from 2 to 20
for number in range(2, 21, 2):
    print(number)
```

Explanation:
- `range(2, 21, 2)` counts by 2, starting from 2.
- `print()` displays each number.

## Exercise 2: The Countdown Timer

Task: Count down from 10 to 1, then display "Time is up!"

```python
# Start at 10
number = 10

# Count down until 1
while number >= 1:
    print(number)
    number -= 1

# Show the final message
print("Time is up!")
```

Explanation:
- The while loop keeps running while the number is at least 1.
- `number -= 1` subtracts 1 after each count.
- After the countdown, it prints "Time is up!"

## Exercise 3: Skip Multiples

Task: Display numbers from 1 to 15, skipping multiples of 3.

```python
# Check numbers from 1 to 15
for number in range(1, 16):

    # Skip numbers divisible by 3
    if number % 3 == 0:
        continue

    print(number)
```

Explanation:
- The for loop checks numbers from 1 to 15.
- `%` checks the remainder when dividing.
- `continue` skips numbers that are multiples of 3.

## Exercise 4: Multiplication Table Generator

Task: Create a function that prints the multiplication table of a number from 1 to 10.

```python
# Create the multiplication table function
def show_table(number):

    # Multiply the number by 1 to 10
    for i in range(1, 11):
        result = number * i
        print(f"{number} x {i} = {result}")


# Ask the user for a number
user_number = int(input("Enter a number: "))

# Run the function
show_table(user_number)
```

Explanation:
- `def show_table(number)` creates a function.
- The for loop multiplies the number from 1 to 10.
- `input()` asks the user to enter a number.
- `show_table(user_number)` runs the function using the entered number.

## What I Learned

- How to use for and while loops.
- How to skip numbers using `continue`.
- How to use the modulo (`%`) operator.
- How to create and use functions.
- How to get input from the user.
