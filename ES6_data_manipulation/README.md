# ES6 Data Manipulation

## Description

This project covers advanced ES6 data structures and array manipulation methods in JavaScript.
It explores `map`, `filter`, `reduce` on arrays, Typed Arrays with `ArrayBuffer` and `DataView`,
and the `Set`, `Map`, and `WeakMap` data structures.

## Learning Objectives

By the end of this project, you should be able to explain without Google:

-How to use `map`, `filter`, and `reduce` on arrays
-What Typed Arrays are and how to use `ArrayBuffer` and `DataView`
-The `Set` data structure: what it is, how to create it, and how to use it
-The `Map` data structure: what it is, how to create it, and how to use it
-The `WeakMap` data structure: what it is and when to use it

## Requirements

-Node 20.x.x
-npm 9.x.x or higher
-Ubuntu 20.04 LTS
-All files use the `.js` extension
-All files end with a new line
-Code uses ES6 syntax with `import`/`export`
-Tests run with Jest via `npm run test`
-Linting with ESLint (Airbnb style) via `npm run check-lint`
-All functions are exported

## Setup

```bash
# Install Node.js 20.x
curl -sL https://deb.nodesource.com/setup_20.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y

# Install project dependencies
npm install
```markdown
# ES6 Data Manipulation

## Description

This project covers advanced ES6 data structures and array manipulation methods in JavaScript.
It explores `map`, `filter`, `reduce` on arrays, Typed Arrays with `ArrayBuffer` and `DataView`,
and the `Set`, `Map`, and `WeakMap` data structures.

## Learning Objectives

By the end of this project, you should be able to explain without Google:

-How to use `map`, `filter`, and `reduce` on arrays
-What Typed Arrays are and how to use `ArrayBuffer` and `DataView`
-The `Set` data structure: what it is, how to create it, and how to use it
-The `Map` data structure: what it is, how to create it, and how to use it
-The `WeakMap` data structure: what it is and when to use it

## Requirements

-Node 20.x.x
-npm 9.x.x or higher
-Ubuntu 20.04 LTS
-All files use the `.js` extension
-All files end with a new line
-Code uses ES6 syntax with `import`/`export`
-Tests run with Jest via `npm run test`
-Linting with ESLint (Airbnb style) via `npm run check-lint`
-All functions are exported

## Setup

```bash
# Install Node.js 20.x
curl -sL https://deb.nodesource.com/setup_20.x -o nodesource_setup.sh
sudo bash nodesource_setup.sh
sudo apt install nodejs -y

# Install project dependencies
npm install
```

## Configuration Files

| File | Purpose |
| --- | --- |
| `package.json` | npm scripts and dev dependencies |
| `babel.config.js` | Babel transpilation configuration |
| `.eslintrc.js` | ESLint rules (Airbnb base + Jest) |

## Available Scripts

```bash
npm run dev <file>    # Run a file with babel-node
npm run test          # Run all Jest tests
npm run check-lint    # Run ESLint on numbered JS files
npm run full-test     # Lint + Jest together
```

## Project Structure

```
ES6_data_manipulation/
├── 0-get_list_students.js       # Returns array of student objects
├── 1-get_list_student_ids.js    # Extracts ids using map
├── 2-get_students_by_loc.js     # Filters students by city
├── 3-get_ids_sum.js             # Sums ids using reduce
├── 4-update_grade_by_city.js    # Combines filter + map
├── 5-typed_arrays.js            # ArrayBuffer + DataView
├── 6-set.js                     # Creates Set from array
├── 7-has_array_values.js        # Checks if all array values exist in Set
├── 8-clean_set.js               # Filters and formats Set values
├── 9-groceries_list.js          # Creates a Map
└── 10-update_uniq_items.js      # Updates Map entries
```

## Key Concepts Summary

### Array Methods

- `map(fn)` → transforms each element, returns new array (same size)
- `filter(fn)` → keeps elements where fn returns true (smaller or equal size)
- `reduce(fn, init)` → accumulates all elements into a single value

### Typed Arrays

- `ArrayBuffer(n)` → raw memory block of n bytes
- `DataView(buffer)` → flexible read/write interface over a buffer
- `view.setInt8(pos, val)` → write 1 signed byte at position pos

### Set

- Unique values only — no duplicates
- `new Set([...])` → create from array
- `.has()`, `.add()`, `.delete()`, `.size`

### Map

- Key-value pairs — any type for keys
- `new Map([[k, v], ...])` → create from array of pairs
- `.get()`, `.set()`, `.has()`, `.delete()`, `.size`

### WeakMap

- Keys must be objects
- Weak references → garbage collectible
- Not iterable — no `.size`, no `.keys()`

## Author

Sara REBATI — Holberton School
```
