# Python Exercises

## Reading Code

```python
fruits = ["apple", "pineapple", "raspberry", "strawberry", "mango", "passionfruit"]

print("apple" in fruits)
```

```python
fruits = ["apple", "pineapple", "raspberry", "strawberry", "mango", "passionfruit"]

for fruit in fruits:
    print("apple" in fruit)
```

```python
fruits = ["apple", "pineapple", "raspberry", "strawberry", "mango", "passionfruit"]

for fruit in fruits:
    if "apple" in fruit:
      print(fruit)
```

```python
fruits = ["apple", "pineapple", "raspberry", "strawberry", "mango", "passionfruit"]

for a, b in enumerate(fruits):
    print(f"{a} {b})
```

```python
fruits = ["apple", "pineapple", "raspberry", "strawberry", "mango", "passionfruit"]

a = [fruit.upper() for fruit in fruits if "berry" in fruit]
b = [fruit.capitalize() for fruit in fruits if "apple" in fruit]

print(b)
print(a)
```

## Finding Bugs

Guess what output of the next program should be, there is a bug hidden, what are some options to fix it?

```python
damian = {
  "name": "Damian",
  "likes": ["Pineapple", "Mango", "Strawberry", "Passionfruit"],
}

mariana = {
  "name": "Mariana",
  "likes": ["Strawberry", "Passionfruit"]
}

people = [mariana, damian]
fruits = ["apple", "pineapple", "raspberry", "strawberry", "mango", "passionfruit"]

for person in people:
    for fruit in fruits:
        if fruit in person["likes"]:
            print(f"{person['name']} likes {fruit}")
```

## Writing Your Own Code

### Working with lists

```python
fruits = ["apple", "pineapple", "raspberry", "strawberry", "mango", "passionfruit"]

# Add more fruits to the list `fruits`

# Sort the fruits alphabetically

# Remove the first two and last two fruits

# Print the resulting fruits list
```

### Print Even Numbers

Write a program that prints all even numbers from 1 to 20 using a for loop.

### Sum of Integers

Write a program that calculates the sum of all integers from 1 to a user-specified (`input`) number using a while loop.

### Reverse a List

Given [1, 2, 3, 4], it should return [4, 3, 2, 1].
Given ['a', 'b', 'c'], it should return ['c', 'b', 'a'].

### Update List in Place

```python
numbers = list(range(1, 20))

# Update and replace all even numbers with their squared value

print(numbers)
```

### Find the highest number in a list

```python
import random

numbers = [random.randint(1, 100) for _ in range(5)]

# Define a variable `highest_number`, the random numbers start at 1,
# which initial value for `highest_number` makes the most sense?

# Find the highest number in the list `numbers` which contains random integers

print(highest_number)
```

### Find the highest AND lowest number in a list

You can reuse your existing code from above and modify it to achieve this, or write it from scratch ;)

### Count the vowels in a user-entered string

```python
user_input = input("Text: ")
vowel_count = 0

print(f"I found {vowel_count} vowels!")
```

### Split and join

Create a program that takes a sentence as input, splits it into words, and then joins the words into a single string with hyphens between them.

### Command Line Arguments

Write a Python script that accepts command line arguments using sys.argv. For example, create a program that calculates the sum of two numbers provided as arguments.

### Password Checker

Create a function that checks if a user-entered password meets the following criteria:

- least 8 characters
- containing both upper- and lowercase letters as well as numbers
- shall not contain three or more consecutive characters
- shall not contain common passwords like "password1" or "123456"

### Word Counter

Write a Python program that reads a text file and counts the number of words in it. You can use the `split()` method to split the text into words. Make sure to handle any punctuation marks or special characters that might be attached to the words.

### Advanced Word Counter

Similar to the previous exercise, but instead count each occurrence of a word seperately and print how many times each word was found within the text file.

Bonus: Sort the output by the amount of times a word was found.

### Print a leaderboard

Print out a leaderboard of an imaginary contest, in the format of:

```
+----+-Score-+-Name----+
|  1 |    25 | Upsi    |
|  2 |    14 | Lou     |
|  3 |     3 | Winston |
+----+-------+---------+
```

Note: Rank and score are right aligned, while the Name is left aligned. Look/search for the f-string documentation on how to align text in formatted strings.

Hint: To find the proper alignment of the pipes and dashes, you need to find the longest name/string within the list of contestants. You can assume that rank and score are below 100 (always two digits).

```python
from operator import itemgetter

contestants = [
    {"score": 85, "name": "Alice"},
    {"score": 92, "name": "Bob"},
    {"score": 78, "name": "Charlie"},
    {"score": 96, "name": "David"},
    {"score": 62, "name": "Eva"},
    {"score": 89, "name": "Frank"},
    {"score": 75, "name": "Grace"},
    {"score": 70, "name": "Hannah"},
    {"score": 82, "name": "Isabel"},
    {"score": 91, "name": "John"}
]

# Sorts list by score
contestants.sort(key=itemgetter("score"))

# Widths of the columns, in other words, the amount of "-" or spaces/padding needed for each row.
rank_width = 3
score_width = 7
# Minimum size of column is 6 due to "-Name-",
# increase the size to the longest name (but keep it at 6 if there's no name longer than 6).
name_width = 6

print(f"+---+-Score-+-Name-{'-' * (name_width - 6)}+")

# Print each contestant row here :)

print(f"+{'-' * rank_width}+{'-' * score_width}+{'-' * name_width}+")
```

### CSV Reader

Create a program that reads a CSV (Comma-Separated Values) file. Each line of the file contains data separated by commas. Your program should read the file and print each row as a list. For example, if the CSV file contains:

```csv
Name, Age, Country
Alice, 25, USA
Bob, 30, Canada
```

Your program should read and print:

```python
['Name', ' Age', ' Country']
['Alice', '25', 'USA']
['Bob', '30', 'Canada']
```

### File Analyzer

Write a Python program that reads a text file and performs the following tasks:

- Count the number of lines in the file.
- Count the number of words in the file.
- Determine the average word length.
- Find the most common word in the file.

### Personal Diary

Write a Python program that allows the user to create a personal diary. The program should do the following:

- Prompt the user to enter a diary entry for the day.
- Append the entry, along with the date and time, to a text file named "diary.txt."

Here's an outline of how the exercise can be structured:

1. Ask the user for a diary entry. For example: `Enter your diary entry for today:`
1. Get the current date and time and format it as a timestamp. You may search and google on how to get the current date and how to format a date.
1. Append the diary entry, along with the timestamp, to the "diary.txt" file. Each entry should be on a new line and formatted like this:

```
Date: {timestamp}
{diary_entry}
```

4. After adding an entry, ask the user if they want to add another entry or view their previous entries.