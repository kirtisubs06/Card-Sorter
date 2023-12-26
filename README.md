# Sorting Cards - Playing Card Class in Python

## Assignment Information
- **Assignment**: 10
- **Author**: Kirti Subramanian
- **CWID**: 20531478
- **Date**: 12/4/2022

## Program Description
This Python program introduces a `PlayingCard` class for creating and handling playing card objects. It allows the creation of card objects with specified ranks and suits, and it can return the full name of the card in word form. The program provides functionality to compare two cards to check if they are the same or determine which one is greater based on the bridge game's rules. Additionally, the program demonstrates object serialization using Python's `pickle` module by storing and retrieving a card object.

## Features

**Playing Card Creation:**
- Allows creation of playing card objects with a specific rank and suit.

**Card Comparison:**
- Implements methods to compare two cards, either checking for equality or determining which card is greater.

**Bridge Game Orderings:**
- Supports comparison based on the orderings of the bridge card game, treating Ace as the highest rank.

**Serialization and Deserialization:**
- Demonstrates how to serialize a card object to a file and deserialize it back to a Python object using `pickle`.

**Formatted Card Representation:**
- Provides a string representation of cards, showing their full names in word form.

## Usage

1. Import the `PlayingCard` class from the script.
2. Create card objects and perform operations like comparison and serialization.

Example usage:
```python
from assignment10 import PlayingCard

card1 = PlayingCard(5, "h")
card2 = PlayingCard(1, "c")

print(card1)  # Output: 5 of Hearts
print(card2 < card1)  # Output: False
