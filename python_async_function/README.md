# Python Async Functions

> Asynchronous programming in Python using `asyncio` — from basics to concurrent task management.

---

## 📋 Description

This project covers the fundamentals of **asynchronous programming in Python** through a progressive series of tasks. Starting from a simple coroutine that waits a random delay, we build up to concurrent execution, runtime benchmarking, and asyncio Task management.

By the end of this project, you will understand how Python's `asyncio` event loop enables non-blocking I/O, how to run multiple coroutines concurrently, and how to leverage `asyncio.Task` objects for fine-grained control over async execution.

---

## 🧠 Learning Objectives

At the end of this project, you should be able to explain — without Google — :

- The `async` and `await` syntax in Python
- How to execute an async program with `asyncio`
- How to run concurrent coroutines
- How to create `asyncio` tasks
- How to use the `random` module

---

## 🛠️ Requirements

| Item | Detail |
|---|---|
| **OS** | Ubuntu 20.04 LTS |
| **Python** | `python3` (version 3.9) |
| **Style** | `pycodestyle` 2.5.x |
| **Editors** | `vi`, `vim`, `emacs` |
| **Shebang** | `#!/usr/bin/env python3` (first line of every file) |
| **Type annotations** | Required on all functions and coroutines |
| **Docstrings** | Required on all modules and functions |
| **Newline** | All files must end with a new line |
| **Executable** | All files must be executable (`chmod +x`) |

---

## 📁 Project Structure

```
python_async_function/
├── README.md
├── 0-basic_async_syntax.py       # Task 0 — wait_random coroutine
├── 1-concurrent_coroutines.py    # Task 1 — wait_n concurrent launcher
├── 2-measure_runtime.py          # Task 2 — measure_time benchmark
├── 3-tasks.py                    # Task 3 — task_wait_random factory
└── 4-tasks.py                    # Task 4 — task_wait_n using Tasks
```

---

## 📚 Tasks

### Task 0 — The Basics of Async

**File:** `0-basic_async_syntax.py`

Write an asynchronous coroutine `wait_random` that takes an integer `max_delay` (default: `10`), waits for a random float delay between `0` and `max_delay` seconds, and returns it.

```python
async def wait_random(max_delay: int = 10) -> float:
```

**Example:**
```bash
$ ./0-main.py
9.034261504534394
1.6216525464615306
10.634589756751769
```

---

### Task 1 — Execute Multiple Coroutines Concurrently

**File:** `1-concurrent_coroutines.py`

Write an async routine `wait_n` that spawns `wait_random` `n` times with the specified `max_delay`. Returns all delays as a **sorted list** (ascending) **without using** `.sort()`, leveraging natural concurrency ordering via `bisect`.

```python
async def wait_n(n: int, max_delay: int) -> List[float]:
```

**Example:**
```bash
$ ./1-main.py
[0.96, 1.02, 1.79, 3.64, 4.50]
[0.07, 1.51, 3.35, 3.70, 3.77, 4.74, 5.50, 5.75, 6.10, 6.83]
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
```

---

### Task 2 — Measure the Runtime

**File:** `2-measure_runtime.py`

Write a **regular (non-async) function** `measure_time` that measures the total execution time for `wait_n(n, max_delay)` and returns `total_time / n` as a float. Uses `time.perf_counter()` for high-precision timing.

```python
def measure_time(n: int, max_delay: int) -> float:
```

**Example:**
```bash
$ ./2-main.py
1.759705400466919
```

---

### Task 3 — asyncio Tasks

**File:** `3-tasks.py`

Write a **regular (non-async) function** `task_wait_random` that takes `max_delay` and returns an `asyncio.Task` object wrapping `wait_random(max_delay)`.

```python
def task_wait_random(max_delay: int) -> asyncio.Task:
```

**Example:**
```bash
$ ./3-main.py
<class '_asyncio.Task'>
```

---

### Task 4 — Tasks (variation)

**File:** `4-tasks.py`

Rewrite `wait_n` as `task_wait_n`, replacing direct `wait_random` calls with `task_wait_random`. The logic and output are identical — only the Task creation mechanism changes, demonstrating clean abstraction.

```python
async def task_wait_n(n: int, max_delay: int) -> List[float]:
```

**Example:**
```bash
$ ./4-main.py
[0.22, 1.19, 1.84, 2.14, 4.00]
```

---

## ⚡ Key Concepts

### `async` / `await`

```python
# Declare a coroutine
async def my_coroutine() -> float:
    await asyncio.sleep(1.0)   # non-blocking pause
    return 1.0
```

### Running an async program

```python
import asyncio
asyncio.run(my_coroutine())    # entry point — starts the event loop
```

### Concurrent execution

```python
# All 3 coroutines run at the same time — total time ≈ max(delays)
results = await asyncio.gather(coro_1(), coro_2(), coro_3())
```

### asyncio Tasks

```python
# Schedules and starts the coroutine immediately in the background
task = asyncio.create_task(my_coroutine())
result = await task            # wait for it when needed
```

### ⚠️ Common Pitfalls

| Mistake | Why it's wrong | Fix |
|---|---|---|
| `time.sleep(n)` inside async | Blocks the entire event loop | Use `await asyncio.sleep(n)` |
| Calling `coro()` without `await` | Creates object, doesn't run it | Always `await coro()` |
| `await` outside `async def` | `SyntaxError` | Wrap in `async def` |
| Multiple `asyncio.run()` calls | Runtime error if nested | Use one `asyncio.run(main())` |

---

## 📦 Modules Used

| Module | Purpose |
|---|---|
| `asyncio` | Event loop, coroutines, Tasks, gather, sleep |
| `random` | `random.uniform(a, b)` — random float in `[a, b]` |
| `time` | `time.perf_counter()` — high-resolution benchmarking |
| `bisect` | `bisect.insort()` — sorted insertion without `.sort()` |
| `typing` | `List[float]` — type annotations |

---

## 🔗 Resources

- [Async IO in Python: A Complete Walkthrough — Real Python](https://realpython.com/async-io-python/)
- [asyncio — Asynchronous I/O — Python Docs](https://docs.python.org/3/library/asyncio.html)
- [random.uniform — Python Docs](https://docs.python.org/3/library/random.html#random.uniform)

---

## 👤 Author

**REBATI SARA** — Holbertonschool student

Project as part of the **Holberton School Web Back End** curriculum.

**Repository:** `holbertonschool-web_back_end` | **Directory:** `python_async_function`