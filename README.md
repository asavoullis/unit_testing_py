# Unit Testing Repository

Welcome to my Unit Testing Repository! This repository contains a collection of Python scripts designed to demonstrate various functionalities and utilize the `unittest` library to perform assertive unit tests, ensuring the reliability and correctness of the implemented code.

## Repository Structure

The project is organized as follows:

```
Unit_Testing_Repository/
|
├── src/
│   ├── employee.py
│   ├── calculator.py
│   ├── find_anagram.py
│   ├── slap_that_like_button.py
│   └── colors.py
|
├── tests/
│   ├── test_calculator.py
│   ├── test_employee.py
│   ├── test_find_anagram.py
│   ├── test_slapping.py
│   └── test_colors.py
|
├── .gitignore
|
└── word_list.txt
```

### To Run Tests

Use one of the following commands to execute the tests:

- Run all tests in the `tests` folder:
  ```
  python -m unittest discover -s tests
  ```

- Run tests using `pytest`:
  ```
  pytest tests/
  ```

- Run a specific test file, e.g., `Test_colors.py`:
  ```
  pytest tests/test_colors.py
  ```

## Scripts

### 1. employee.py

`employee.py` contains the implementation of a simple `Employee` class with methods such as `give_promotion` and `attribute_length`. This class is designed to manage employee information and explore various object-oriented programming concepts.

### 2. calculator.py

`Calculator.py` provides basic calculator functionalities, including arithmetic operations like addition, subtraction, multiplication, and division.

### 3. find_anagram.py

`find_anagram.py` identifies anagrams from a list of words stored in `word_list.txt`. An anagram is a word or phrase formed by rearranging the letters of another word or phrase.

### 4. slap_that_like_button.py

`slap_that_like_button.py` defines functionality for toggling states (`liked`, `disliked`, and `empty`) using the following:

- Enum class `LikeState` with states: `empty`, `liked`, and `disliked`.
- Functions:
  - `slap_like`: Toggles between states `empty`, `liked`, and back.
  - `slap_dislike`: Toggles between states `empty`, `disliked`, and back.
  - `slaps_many`: Applies a sequence of state transitions based on input commands (`l` for like, `d` for dislike).

Example usage:
```python
from slap_button import LikeState, slaps_many
state = LikeState.empty
result = slaps_many(state, "lld")  # Applies transitions
print(result)  # Final state
```

### 5. colors.py

`colors.py` demonstrates an Enum-based implementation for color management:

- Enum class `Color` with values: `RED`, `GREEN`, and `BLUE`.
- Features include:
  - `describe`: Provides a descriptive text for each color.
  - `color_to_hex`: Maps colors to their hexadecimal representations.
  - `print_all_colors`: Iterates and prints all color names and values.

Example usage:
```python
from colors import Color, color_to_hex
print(Color.RED)  # Output: Color.RED
print(color_to_hex(Color.RED))  # Output: #FF0000
```

## Testing

Each script includes dedicated test files in the `tests` folder that utilize the `unittest` library.

### Test Files

1. `test_calculator.py`
   - Tests functionalities in `calculator.py`.
   - Ensures arithmetic operations are performed correctly.

2. `test_employee.py`
   - Tests methods in `employee.py`.
   - Validates class behavior and data manipulation.

3. `test_find_anagram.py`
   - Tests the functionality of `find_anagram.py`.
   - Verifies accurate identification of anagrams.

4. `test_slapping.py`
   - Tests state transitions in `slap_that_like_button.py`.
   - Ensures proper toggling of `liked`, `disliked`, and `empty` states.

5. `test_colors.py`
   - Tests the functionalities in `colors.py`.
   - Verifies color-to-hex mappings and descriptions.

## Additional Files

### word_list.txt

`word_list.txt` contains a list of words used as input for `find_anagram.py` to demonstrate its functionality.

