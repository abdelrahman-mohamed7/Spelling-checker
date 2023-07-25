# Spell Checker

The `spell_checker` class is a Python implementation of a spell checker using a trie data structure. The class provides three main operations:

1. Store a dictionary of words in a trie data structure.
2. Find the nearest 4 words to a given input word if it is not in the dictionary.
3. Add a new word to the dictionary.

## Getting Started

To use the `spell_checker` class, you need to create an instance of the class by providing a file path to a text file containing the dictionary of words. The dictionary file should contain one word per line.

```python
checking = spell_checker("dictionary.txt")
```

## Operations

### Store a dictionary in a trie data structure

To store a dictionary in the trie data structure, you just need to create an instance of the `spell_checker` class, passing the file path to the dictionary file as a parameter. The constructor will read the file and add each word to the trie.

```python
checking = spell_checker("dictionary.txt")
```

### Find the nearest 4 words to a given input word

To find the nearest 4 words to a given input word, you can call the `find_nearest_words` method of the `spell_checker` class, passing the word as a parameter. If the word exists in the dictionary, it will be returned. Otherwise, the method will return the 2 words before and the 2 words after the input word in lexicographic order, if they exist.

```python
nearest_words = checking.find_nearest_words("findaa")
```

### Add a new word to the dictionary

To add a new word to the dictionary, you can call the `add_word` method of the `spell_checker` class, passing the word as a parameter.

```python
checking.add_word("findaa")
```

## Example

Here is an example of how to use the `spell_checker` class.

```python
checking = spell_checker("dictionary.txt")

# Find the nearest 4 words to "findaa"
nearest_words = checking.find_nearest_words("findaa")
print(nearest_words)

# Add the word "findaa" to the dictionary
checking.add_word("findaa")

# Now find_nearest_words should return only "findaa"
nearest_words = checking.find_nearest_words("findaa")
print(nearest_words)
```

## Complexity

The time and space complexity of the main operations of the `spell_checker` class are as follows:

- Store a dictionary in a trie data structure:
  - Time complexity: O(n), where n is the number of words in the dictionary.
  - Space complexity: O(n).

- Find the nearest 4 words to a given input word:
  - Time complexity: O(n), where n is the length of the input word.
  - Space complexity: O(n).

- Add a new word to the dictionary:
  - Time complexity: O(n), where n is the length of the input word.
  - Space complexity: O(n).
