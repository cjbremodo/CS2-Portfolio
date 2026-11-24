# Python Programming Exercises

## Exercise 1: My School Bag

### Python Code

```python
# Create a list containing five school supplies
school_items = ["Notebook", "Pen", "Calculator", "Laptop", "Book"]

# Display each school supply using its index position
print("School Supplies:")
print(school_items[0])
print(school_items[1])
print(school_items[2])
print(school_items[3])
print(school_items[4])

# Display the first item in the list
print("\nFirst item:", school_items[0])

# Display the last item in the list
print("Last item:", school_items[4])
```

### Example

```text
School Supplies:
Notebook
Pen
Calculator
Laptop
Book

First item: Notebook
Last item: Book
```

### Explanation
- A list named `school_items` stores five school supplies.
- Index positions are used to access individual items. Python indexing starts at 0.
- `school_items[0]` displays the first item.
- `school_items[4]` displays the last item.
- No loops are used, as required by the exercise.



## Exercise 2: Travel Destination Manager


### Python Code

```python
# Create a list containing five travel destinations
destinations = ["Cebu", "Manila", "Davao", "Baguio", "Palawan"]

# Display all destinations using a for loop
print("Travel Destinations:")
for destination in destinations:
    print(destination)

# Use slicing to display items from index 1 up to index 3
print("\nDestinations from index 1 to 3:")
print(destinations[1:4])

# Ask the user to enter a destination to search for
search = input("\nEnter a destination to search for: ")

# Check whether the entered destination exists in the list
if search in destinations:
    print(search, "is in the destination list.")
else:
    print(search, "is not in the destination list.")

# Replace the item at index 2 with Iloilo
destinations[2] = "Iloilo"

# Display the updated destination list
print("\nUpdated Destinations:")
print(destinations)
```

### Example

```text
Travel Destinations:
Cebu
Manila
Davao
Baguio
Palawan

Destinations from index 1 to 3:
['Manila', 'Davao', 'Baguio']

Enter a destination to search for: Cebu
Cebu is in the destination list.

Updated Destinations:
['Cebu', 'Manila', 'Iloilo', 'Baguio', 'Palawan']
```

### Explanation
- The list stores five school supplies.
- Indexing is used to display each item.
- Index `0` is the first item, while index `4` is the last item.
- No loops are used.

- The list stores five travel destinations.
- A `for` loop displays all destinations.
- Slicing (`[1:4]`) displays items from index 1 to 3.
- `input()` lets the user enter a destination.
- The `in` operator checks if the destination exists.
- Index `2` is replaced with `"Iloilo"`.
- The updated list is displayed.

## Concepts Learned

1. **Lists** – Store multiple items in one variable.
2. **Indexing** – Access items by position.
3. **Slicing** – Get part of a list.
4. **For Loops** – Display items one by one.
5. **Searching** – Check if an item exists.
6. **Updating** – Replace an item in a list.

