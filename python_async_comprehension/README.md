# Python - Variable Annotations

## Description

This project explores **type annotations** in Python 3, a feature that allows developers to explicitly specify the expected types of variables, function parameters, and return values. Through a series of tasks, we cover basic type hints, complex types using the `typing` module, duck typing principles, and static type validation with `mypy`.

---

## Learning Objectives

By the end of this project, you should be able to explain:

- What type annotations are in Python 3 and how to use them
- How to specify function signatures and variable types with annotations
- What duck typing is and how Python leverages it
- How to validate your code with `mypy`

---

## Requirements

- Python 3.9 (Ubuntu 20.04 LTS)
- `pycodestyle` 2.5
- All files must be executable
- All files must end with a new line
- First line of every file: `#!/usr/bin/env python3`
- All modules, classes, and functions must have a docstring

---

## Tasks

### 0. Basic annotations — add
**File:** `0-add.py`

Type-annotated function `add` that takes two floats and returns their sum as a float.

```python
def add(a: float, b: float) -> float:
```

---

### 1. Basic annotations — concat
**File:** `1-concat.py`

Type-annotated function `concat` that takes two strings and returns their concatenation.

```python
def concat(str1: str, str2: str) -> str:
```

---

### 2. Basic annotations — floor
**File:** `2-floor.py`

Type-annotated function `floor` that takes a float and returns its floor value as an integer.

```python
def floor(n: float) -> int:
```

---

### 3. Basic annotations — to string
**File:** `3-to_str.py`

Type-annotated function `to_str` that takes a float and returns its string representation.

```python
def to_str(n: float) -> str:
```

---

### 4. Define variables
**File:** `4-define_variables.py`

Define and annotate the following variables:

| Variable | Type | Value |
|---|---|---|
| `a` | `int` | `1` |
| `pi` | `float` | `3.14` |
| `i_understand_annotations` | `bool` | `True` |
| `school` | `str` | `"Holberton"` |

---

### 5. Complex types — list of floats
**File:** `5-sum_list.py`

Type-annotated function `sum_list` that takes a list of floats and returns their sum as a float.

```python
def sum_list(input_list: List[float]) -> float:
```

---

### 6. Complex types — mixed list
**File:** `6-sum_mixed_list.py`

Type-annotated function `sum_mixed_list` that takes a list of integers and floats and returns their sum as a float.

```python
def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
```

---

### 7. Complex types — string and int/float to tuple
**File:** `7-to_kv.py`

Type-annotated function `to_kv` that takes a string `k` and an int or float `v`, and returns a tuple `(k, v²)` where the square is annotated as a float.

```python
def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
```

---

### 8. Complex types — functions
**File:** `8-make_multiplier.py`

Type-annotated function `make_multiplier` that takes a float and returns a function that multiplies a float by that value.

```python
def make_multiplier(multiplier: float) -> Callable[[float], float]:
```

---

### 9. Let's duck type an iterable object
**File:** `9-element_length.py`

Annotate the parameters and return values of `element_length` using duck typing.

```python
def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
```

---

### 10. Duck typing — first element of a sequence *(Advanced)*
**File:** `100-safe_first_element.py`

Augment `safe_first_element` with correct duck-typed annotations. The element types are unknown.

```python
def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
```

---

### 11. More involved type annotations *(Advanced)*
**File:** `101-safely_get_value.py`

Add type annotations using `TypeVar` to a function that safely retrieves a value from a dictionary.

```python
T = TypeVar('T')

def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Union[T, None] = None
) -> Union[Any, T]:
```

---

### 12. Type Checking *(Advanced)*
**File:** `102-type_checking.py`

Use `mypy` to validate and fix a broken piece of code until the following output is reached:

```bash
$ mypy 102-type_checking.py
Success: no issues found in 1 source file
```

---

## Type Annotations Cheat Sheet

| Annotation | Meaning | Import needed |
|---|---|---|
| `int`, `float`, `str`, `bool` | Built-in types | None |
| `List[X]` | List of elements of type X | `from typing import List` |
| `Tuple[X, Y]` | Tuple with typed positions | `from typing import Tuple` |
| `Union[X, Y]` | Either type X or type Y | `from typing import Union` |
| `Optional[X]` | Type X or None | `from typing import Optional` |
| `Callable[[X], Y]` | Function taking X, returning Y | `from typing import Callable` |
| `Iterable[X]` | Anything iterable over X | `from typing import Iterable` |
| `Sequence[X]` | Anything indexable with len() | `from typing import Sequence` |
| `Mapping` | Dict-like object | `from typing import Mapping` |
| `Any` | Any type (disables checking) | `from typing import Any` |
| `TypeVar('T')` | Generic type variable | `from typing import TypeVar` |

---

## Running mypy

```bash
# Install
pip install mypy

# Validate a single file
mypy <filename>.py

# Validate all files in the project
mypy *.py
```

---

## Repository

- **GitHub repository:** `holbertonschool-web_back_end`
- **Directory:** `python_variable_annotations`

---

## Author

Project by **REBATI SARA**, holbertonschool Student.