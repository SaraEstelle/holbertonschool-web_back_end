# Python Async Comprehension

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.9-blue?style=flat-square&logo=python" alt="Python 3.9"/>
  <img src="https://img.shields.io/badge/asyncio-async%2Fawait-teal?style=flat-square" alt="asyncio"/>
  <img src="https://img.shields.io/badge/PEP_530-Async_Comprehensions-purple?style=flat-square" alt="PEP 530"/>
  <img src="https://img.shields.io/badge/pycodestyle-2.5.x-green?style=flat-square" alt="pycodestyle"/>
  <img src="https://img.shields.io/badge/Ubuntu-20.04_LTS-orange?style=flat-square&logo=ubuntu" alt="Ubuntu"/>
</p>

---

## Table of Contents

- [About the Project](#about-the-project)
- [Learning Objectives](#learning-objectives)
- [Key Concepts](#key-concepts)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Installation & Setup](#installation--setup)
- [Tasks](#tasks)
  - [Task 0 – Async Generator](#task-0--async-generator)
  - [Task 1 – Async Comprehensions](#task-1--async-comprehensions)
  - [Task 2 – Run Time for Four Parallel Comprehensions](#task-2--run-time-for-four-parallel-comprehensions)
- [How to Run](#how-to-run)
- [Code Style](#code-style)
- [Why Async? Performance Explained](#why-async-performance-explained)
- [Real-World Applications](#real-world-applications)
- [Resources](#resources)
- [Author](#author)

---

## About the Project

This project is part of the **Holberton School Web Back End** curriculum and focuses on **asynchronous Python programming** — specifically asynchronous generators, async comprehensions, and concurrent execution with `asyncio.gather()`.

By completing this project, you gain a solid understanding of how Python handles non-blocking I/O operations using the `asyncio` event loop, and how to write clean, type-annotated asynchronous code following modern Python standards (PEP 530).

> **Designed and assigned by:** Emmanuel Turlay, Staff Software Engineer at [Cruise](https://getcruise.com)

---

## Learning Objectives

By the end of this project, you will be able to explain the following **without the help of Google**:

- ✅ How to write an **asynchronous generator** using `async def` and `yield`
- ✅ How to use **async comprehensions** to collect values from async iterables
- ✅ How to properly **type-annotate** generators and coroutines
- ✅ Why executing 4 async coroutines with `asyncio.gather()` takes **~10 seconds** and not ~40 seconds
- ✅ The difference between **synchronous generators** and **asynchronous generators**

---

## Key Concepts

### Asynchronous Generator

A function declared with `async def` that contains a `yield` statement. It can suspend its execution both while waiting (`await`) and while producing a value (`yield`).

```python
async def async_generator():
    for _ in range(10):
        await asyncio.sleep(1)   # non-blocking pause
        yield random.uniform(0, 10)  # produces a value
```

It is consumed using `async for`:

```python
async for value in async_generator():
    print(value)
```

---

### Async Comprehension (PEP 530)

Introduced in Python 3.6 via [PEP 530](https://peps.python.org/pep-0530/), async comprehensions allow you to collect results from an asynchronous iterable using a concise one-liner — just like regular list comprehensions but with `async for`:

```python
# Regular list comprehension
result = [x for x in range(10)]

# Async list comprehension (inside a coroutine)
result = [x async for x in async_generator()]

# With a filter
result = [x async for x in async_generator() if x > 5.0]
```

---

### asyncio.gather() — Concurrent Execution

`asyncio.gather()` schedules multiple coroutines to run **concurrently** on the same event loop. While one coroutine is waiting (e.g., `await asyncio.sleep(1)`), the others continue making progress.

```python
# Run 4 coroutines in parallel — total time ≈ 10s, not 40s
await asyncio.gather(
    async_comprehension(),
    async_comprehension(),
    async_comprehension(),
    async_comprehension(),
)
```

---

### Type Annotations for Async Generators

```python
from typing import AsyncGenerator, List

# Async generator that yields floats
async def async_generator() -> AsyncGenerator[float, None]:
    ...

# Coroutine that returns a list of floats
async def async_comprehension() -> List[float]:
    ...

# Coroutine that returns a float
async def measure_runtime() -> float:
    ...
```

`AsyncGenerator[YieldType, SendType]`:
- `YieldType` — the type of values produced by `yield`
- `SendType` — almost always `None` unless using `.send()`

---

## Project Structure

```
holbertonschool-web_back_end/
└── python_async_comprehension/
    ├── README.md                    # This file
    ├── 0-async_generator.py         # Task 0: Async Generator
    ├── 0-main.py                    # Test runner for Task 0
    ├── 1-async_comprehension.py     # Task 1: Async Comprehension
    ├── 1-main.py                    # Test runner for Task 1
    ├── 2-measure_runtime.py         # Task 2: Parallel Runtime Measurement
    └── 2-main.py                    # Test runner for Task 2
```

---

## Requirements

| Requirement | Detail |
|---|---|
| **OS** | Ubuntu 20.04 LTS |
| **Python** | 3.9 |
| **Style** | `pycodestyle` version 2.5.x |
| **Editors** | `vi`, `vim`, `emacs` |
| **Shebang** | `#!/usr/bin/env python3` (first line of every file) |
| **Newline** | Every file must end with a newline |
| **Docstrings** | Every module and every function must have a full docstring |
| **Type annotations** | All functions and coroutines must be fully type-annotated |
| **README** | `README.md` at the root of the project directory is mandatory |

---

## Installation & Setup

**1. Clone the repository:**

```bash
git clone https://github.com/<your-username>/holbertonschool-web_back_end.git
cd holbertonschool-web_back_end/python_async_comprehension
```

**2. Verify your Python version:**

```bash
python3 --version
# Expected: Python 3.9.x
```

**3. Make all files executable:**

```bash
chmod +x *.py
```

**4. (Optional) Install pycodestyle for style checking:**

```bash
pip install pycodestyle==2.5.0
```

---

## Tasks

---

### Task 0 – Async Generator

**File:** `0-async_generator.py`

#### What it does

Implements an **asynchronous generator** coroutine called `async_generator` that:

- Loops **10 times**
- Asynchronously waits **1 second** per iteration using `await asyncio.sleep(1)`
- Yields a **random float** between `0` and `10` using `random.uniform(0, 10)`

#### Signature

```python
async def async_generator() -> AsyncGenerator[float, None]:
```

#### How it works internally

```
t = 0s   → loop starts
t = 1s   → await sleep done → yield 4.40
t = 2s   → await sleep done → yield 6.90
t = 3s   → await sleep done → yield 6.29
...
t = 10s  → await sleep done → yield 1.37
           loop ends → StopAsyncIteration raised automatically
```

#### Source Code

```python
#!/usr/bin/env python3
"""Module containing an asynchronous random number generator.

Implements an async generator that yields random float values with
a one-second non-blocking delay between each value produced.
"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Yield 10 random floats asynchronously, one per second.

    Loops 10 times. Each iteration waits 1 second asynchronously
    then yields a random float between 0.0 and 10.0.

    Yields:
        float: A random number between 0.0 and 10.0.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
```

#### Expected Output

```bash
$ ./0-main.py
[4.403136952967102, 6.9092712604587465, 6.293445466782645, 4.549663490048418,
 4.1326571686139015, 9.99058525304903, 6.726734105473811, 9.84331704602206,
 1.0067279479988345, 1.3783306401737838]
```

> A list of 10 random floats. Values change on every run. Total execution time: ~10 seconds.

---

### Task 1 – Async Comprehensions

**File:** `1-async_comprehension.py`

#### What it does

Implements a coroutine called `async_comprehension` that:

- Imports `async_generator` from Task 0
- Collects all 10 values using a **single async comprehension**
- Returns the resulting list of floats

#### Signature

```python
async def async_comprehension() -> List[float]:
```

#### The async comprehension syntax

```python
# Manual loop (equivalent, but verbose)
result = []
async for val in async_generator():
    result.append(val)

# Async comprehension (concise, PEP 530)
result = [val async for val in async_generator()]
```

Both produce exactly the same result. The comprehension syntax is preferred for its readability and brevity.

#### Source Code

```python
#!/usr/bin/env python3
"""Module using an async comprehension to collect random values.

Demonstrates the use of async comprehensions (PEP 530) to gather
results from an asynchronous generator into a list.
"""

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Collect 10 random floats using an async comprehension.

    Iterates over async_generator using an async comprehension
    and returns the collected list of 10 float values.

    Returns:
        List[float]: A list of 10 random floats between 0.0 and 10.0.
    """
    return [val async for val in async_generator()]
```

#### Expected Output

```bash
$ ./1-main.py
[9.861842105071727, 8.572355293354995, 1.7467182056248265, 4.0724372912858575,
 0.5524750922145316, 8.084266576021555, 8.387128918690468, 1.5486451376520916,
 7.713335177885325, 7.673533267041574]
```

> Same format as Task 0. The comprehension resolves fully before `return` is executed.

---

### Task 2 – Run Time for Four Parallel Comprehensions

**File:** `2-measure_runtime.py`

#### What it does

Implements a coroutine called `measure_runtime` that:

- Imports `async_comprehension` from Task 1
- Runs `async_comprehension()` **four times concurrently** using `asyncio.gather()`
- Measures and returns the **total elapsed time** in seconds

#### Signature

```python
async def measure_runtime() -> float:
```

#### The surprising result: why ~10s and not ~40s?

This is the core insight of the entire project:

```
SEQUENTIAL execution (without gather):
──────────────────────────────────────────────────────► time
[comp_1 ░░░░░░░░░░ 10s][comp_2 ░░░░░░░░░░ 10s]
                       [comp_3 ░░░░░░░░░░ 10s][comp_4 ░░░░░░░░░░ 10s]
Total = 40 seconds

CONCURRENT execution (with asyncio.gather):
──────────────────────────────────────────────────────► time
[comp_1 ░░░░░░░░░░ 10s]
[comp_2 ░░░░░░░░░░ 10s]
[comp_3 ░░░░░░░░░░ 10s]
[comp_4 ░░░░░░░░░░ 10s]
Total ≈ 10 seconds   ← all 4 overlap completely!
```

**Why?** Because each coroutine spends most of its time in `await asyncio.sleep(1)`. During that sleep, the event loop is free to run the other coroutines. All four coroutines share the same waiting periods simultaneously — their `sleep` calls overlap perfectly on the single-threaded event loop.

The total time equals the time of the **slowest single coroutine** (~10s), not the sum of all four (~40s). This is the power of async concurrency for **I/O-bound tasks**.

#### Important: correct vs incorrect usage of gather

```python
# ✅ CORRECT — pass coroutine objects (not awaited)
await asyncio.gather(
    async_comprehension(),   # creates the coroutine object
    async_comprehension(),
    async_comprehension(),
    async_comprehension(),
)

# ❌ WRONG — awaiting before gather makes it sequential
await asyncio.gather(
    await async_comprehension(),  # executes first, then passes result
    await async_comprehension(),  # executes second...
)
```

#### Source Code

```python
#!/usr/bin/env python3
"""Module measuring the runtime of four parallel async comprehensions.

Demonstrates the use of asyncio.gather to run multiple coroutines
concurrently, and measures the total elapsed time to illustrate
the performance benefits of asynchronous concurrency.
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the runtime of four concurrent async comprehensions.

    Runs async_comprehension four times simultaneously using
    asyncio.gather. Measures and returns the total elapsed time.
    The expected result is approximately 10 seconds because the four
    coroutines run concurrently and share the same async wait periods.

    Returns:
        float: Total elapsed time in seconds (approximately 10.0).
    """
    start = time.perf_counter()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    return time.perf_counter() - start
```

#### Expected Output

```bash
$ ./2-main.py
10.021936893463135
```

> The result is ~10.02s. The small overhead (~0.02s) comes from event loop scheduling, context switching, and function call overhead — all negligible.

---

## How to Run

Run each task individually using its corresponding test file:

```bash
# Task 0 — Async Generator
./0-main.py

# Task 1 — Async Comprehension
./1-main.py

# Task 2 — Parallel Runtime
./2-main.py
```

Verify docstrings are present and non-trivial:

```bash
# Module docstring
python3 -c 'print(__import__("0-async_generator").__doc__)'
python3 -c 'print(__import__("1-async_comprehension").__doc__)'
python3 -c 'print(__import__("2-measure_runtime").__doc__)'

# Function docstrings
python3 -c 'print(__import__("0-async_generator").async_generator.__doc__)'
python3 -c 'print(__import__("1-async_comprehension").async_comprehension.__doc__)'
python3 -c 'print(__import__("2-measure_runtime").measure_runtime.__doc__)'
```

---

## Code Style

All files must comply with `pycodestyle` version 2.5.x:

```bash
pycodestyle 0-async_generator.py
pycodestyle 1-async_comprehension.py
pycodestyle 2-measure_runtime.py
```

No output means no style violations. Key rules enforced:

- Maximum line length: **79 characters**
- Two blank lines between top-level definitions
- One blank line between methods inside a class
- No trailing whitespace

---

## Why Async? Performance Explained

### Synchronous vs Asynchronous I/O

| Scenario | Sync | Async |
|---|---|---|
| 1 task × 10s wait | 10s | 10s |
| 4 tasks × 10s wait (sequential) | **40s** | — |
| 4 tasks × 10s wait (concurrent) | — | **~10s** |
| 100 HTTP requests | ~100s | **~1–2s** |

### When does async help?

Async shines for **I/O-bound tasks**: operations that spend most of their time waiting for something external (network, disk, database, timers). Examples:

- `await asyncio.sleep(n)` — timer-based wait
- `await aiohttp.get(url)` — HTTP request
- `await db.execute(query)` — database query
- `await file.read()` — async file read

Async does **not** help for **CPU-bound tasks** (heavy computation). For those, use `multiprocessing` or `concurrent.futures.ProcessPoolExecutor`.

---

## Real-World Applications

| Domain | Use Case | Tasks Applied |
|---|---|---|
| **Web scraping** | Download 1000 URLs concurrently | Task 0 (gen) + Task 2 (gather) |
| **REST API** | Stream large response bodies progressively | Task 0 (async generator) |
| **Data pipeline** | Async ETL — extract, transform, load at scale | Task 0 + Task 1 |
| **System monitoring** | Yield CPU/memory metrics every N seconds | Task 0 (periodic yield) |
| **Microservices** | Fan-out to N services and aggregate results | Task 2 (gather) |
| **IoT** | Poll 100 sensors simultaneously | Task 2 (gather) |
| **LLM streaming** | Stream tokens from an AI API token by token | Task 0 (async generator) |
| **Distributed cache** | Warm up Redis with parallel writes at startup | Task 2 (gather) |

---

## Resources

| Resource | Link |
|---|---|
| PEP 530 – Asynchronous Comprehensions | https://peps.python.org/pep-0530/ |
| What's New in Python – Async Comprehensions | https://docs.python.org/3/whatsnew/3.6.html#pep-530-asynchronous-comprehensions |
| asyncio — Python 3.9 official docs | https://docs.python.org/3.9/library/asyncio.html |
| asyncio.gather() | https://docs.python.org/3.9/library/asyncio-task.html#asyncio.gather |
| typing.AsyncGenerator | https://docs.python.org/3/library/typing.html#typing.AsyncGenerator |
| Type hints for generators | https://docs.python.org/3/library/typing.html#typing.Generator |
| pycodestyle docs | https://pycodestyle.pycqa.org/en/latest/ |

---

## Author

**REBATI SARA**


**Repository:** `holbertonschool-web_back_end`
**Directory:** `python_async_comprehension`
**Curriculum:** Holberton School — Web Back End Track

---

*All code written for Ubuntu 20.04 LTS · Python 3.9 · pycodestyle 2.5.x*