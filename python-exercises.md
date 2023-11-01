# Python Exercises

## Reading Code

Guess what each of these code snippets output, you can verify your guess by running it in a python shell or editor.

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
    print(f"{a} {b}")
```

I think you have not seen this yet, no to worry, but can you guess what this _could_ do?

```python
fruits = ["apple", "pineapple", "raspberry", "strawberry", "mango", "passionfruit"]

a = [fruit.upper() for fruit in fruits if "berry" in fruit]
b = [fruit.capitalize() for fruit in fruits if "apple" in fruit]

print(b)
print(a)
```

### List Operations Puzzle

Given the following list and sequence of operations, try to guess the final state of the list after each operation:

If you do not know one of the list methods, try to look them up in your editor or google, before giving your final guess :)

```python
my_list = [1, 2, 3, 4, 5]

# Operation 1
my_list.append(6)

# Operation 2
my_list.insert(2, 7)

# Operation 3
my_list.pop(4)

# Operation 4
sliced_list = my_list[1:4]

# Operation 5
my_list.extend([8, 9])

# Operation 6
my_list.remove(2)
```

### Dictionary Lookups

```python
sentence = "The quick brown fox jumps over the lazy dog"

words = sentence.split()
characters = list(sentence)

word_lengths = {}

for word in words:
    word_lengths[word] = len(word)

jumps_length = word_lengths["jumps"]
print("Length of 'jumps':", jumps_length)

is_elephant_present = "elephant" in word_lengths
print("Is 'elephant' present in the dictionary?", is_elephant_present)
```

### NLTK example

```python
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter

nltk.download('punkt')
nltk.download('stopwords')

text = """
Natural Language Processing (NLP) is a fascinating field that focuses on the interaction between humans and computers using natural language. It involves the development of algorithms and models to enable machines to understand, interpret, and generate human language.

NLP has numerous applications, such as sentiment analysis, chatbots, language translation, and more. In this exercise, you will explore a basic NLP task: counting word frequencies.

Your task is to count the frequency of words in the given text. First, tokenize the text into words. Then, convert the words to lowercase and remove common stopwords. Finally, count and display the frequency of each word.

NLP has a wide range of tools and libraries to work with, and NLTK is one of the most popular ones. It provides various resources and functionalities for text analysis. Remember to install NLTK if you haven't already and download the required data.

Feel free to experiment with different texts and explore the world of NLP further. Enjoy the exercise!
"""

words = word_tokenize(text)
stop_words = set(stopwords.words('english'))
filtered_words = []

for word in words:
    if word.isalnum() and word.lower() not in stop_words:
        filtered_words.append(word.lower())

word_count = Counter(filtered_words)

for word, count in word_count.items():
    print(f"{word}: {count}")
```

## Finding Bugs

Find common errors/issues, if you do not see the error straight away, you may also run it in a python shell or editor, try to spot or guess the error first though :)

```
for i in range(5)
    print(i)
```

```
x = y + 5
print(x)
```

```
if = 10
print(if)
```

```
message = 'Hi Upsi."
print(message)
```

```python
count = 0
while count < 5
    print("Count:", count)
    count += 1
```

```python
count = 0
while count >= 5:
    print("Count:", count)
```

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

Given `[1, 2, 3, 4]`, it should return `[4, 3, 2, 1]`.

Given `['a', 'b', 'c']`, it should return `['c', 'b', 'a']`.

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

### Updating a dictionary

Given an aggregated POS tag counter, update the counters with a new list of tokens.
Print out the newly updated tag counters in the format of `NN: 20` for each tag.

```python
pos_tags = {
    "NN": 15,
    "NNP": 8,
    "VB": 10,
    "JJ": 7,
    "RB": 5
}

# Sample pre-tokenized sentence
new_sentence_tokens = ["NN", "JJ", "NN", "VB", "NN", "NNP", "NN"]

# Update the counts in the dictionary using the new sentence tokens


# Print the updated POS tag counts
```

### Domain from Email

Given a list of emails, uniquely print all the different domains.

```python
emails = [
    "john.doe@example.com",
    "jane.smith@gmail.com",
    "michael.jackson@yahoo.com",
    "susan.williams@outlook.com",
    "david.jones@hotmail.com",
    "emily.davis@gmail.com",
    "robert.white@yahoo.com",
    "laura.miller@example.com",
    "william.brown@hotmail.com",
    "olivia.wilson@outlook.com"
]
```

### Ellipsis

You are given a list of sentences, to be used in a small window. This window only displays up to 80 characters and the text should be cut off at the last character.

Strip any whitespace character from the cut-off sentence before printing the ellipsis.

Print each sentence properly cut-off, example:

```python
# A string like this
"In the quiet forest, the leaves rustled as the wind whispered secrets among the trees."

# Should print this
"In the quiet forest, the leaves rustled as the wind whispered secrets among the…"
```

```python
limit = 80
ellipsis = "…"
sentences = [
    "In the serene beauty of the moonlit night, the stars sparkled like diamonds, casting a gentle glow upon the tranquil lake below, where the world seemed to find solace.",
    "The sun set over the horizon, painting the sky in shades of pink and orange.",
    "In the quiet forest, the leaves rustled as the wind whispered secrets among the trees.",
    "She gazed at the old photo, reminiscing about the good times with a bittersweet smile.",
    "The waves crashed against the rocky shore, their rhythmic sound calming the soul.",
    "The ancient oak tree, with its gnarled branches, stood tall and proud in the heart of the forest, a silent guardian of the woods.",
    "As the city lights twinkled, he felt a sense of belonging in the bustling streets.",
    "Amidst the chaos, a single act of kindness can illuminate even the darkest of times.",
    "The ancient castle stood in silent grandeur, a testament to a bygone era.",
]

# Cut and print out sentences up to 80 characters
```

Bonus: Instead of cutting of at the specific character index, cut off after the last word within the first 80 characters.

Example:

```python
# Instead of printing
"Amidst the chaos, a single act of kindness can illuminate even the darkest of ti…"

# The new code should print this instead:
"Amidst the chaos, a single act of kindness can illuminate even the darkest of…"
```

Hint: You can use the string method `.rfind()` which is like `.find()` but searches backwards in a string ;)

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

### Sentence Split and Dictionary Lookups

Given the following sentence as a string:

```python
sentence = "The quick brown fox jumps over the lazy dog"
```

Perform the following operations:

1. Split the sentence into words and store them in a list.
1. Split the sentence into individual characters and store them in a list.
1. Create a dictionary where the keys are words from the sentence, and the values are the lengths of those words.
1. Use the dictionary to look up and print the length of the word "quick".
1. Check if the word "fox" exists in the dictionary and print the result.

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

4. After adding an entry, ask the user if they want to add another entry.
