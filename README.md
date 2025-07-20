# Assignment 3: Understanding Algorithm Efficiency and Scalability

## 📘 Overview

This assignment is designed to deepen your understanding of how algorithms perform under different conditions. You will analyze and compare the efficiency and scalability of two key algorithms:

1. **Randomized Quicksort**
2. **Hashing with Chaining**

Through this assignment, you will develop the skills necessary to evaluate algorithm performance, implement efficient solutions, and make informed decisions about algorithm selection based on both theoretical and empirical analysis.

---

## 📌 Part 1: Randomized Quicksort Analysis

### 🔹 1. Implementation

- Implemented **Randomized Quicksort**, where the pivot is selected uniformly at random from the current subarray.
- Efficient handling of edge cases:
  - Repeated elements
  - Empty arrays
  - Already sorted or reverse-sorted arrays

### 🔹 2. Analysis

- The **average-case time complexity** of Randomized Quicksort is proven to be **O(n log n)**.
- Analysis includes:
  - Recurrence relation:  
    `T(n) = (1/n) * ∑(T(i) + T(n-i-1)) + Θ(n)`
  - Use of **indicator random variables** to calculate expected comparisons.
  - The expected number of comparisons is approximately `1.39 * n log n`.

### 🔹 3. Comparison

Empirical comparisons between **Randomized** and **Deterministic Quicksort** (first/mid element as pivot) were conducted on the following input distributions:

- ✅ Randomly generated arrays  
- ✅ Already sorted arrays  
- ✅ Reverse-sorted arrays  
- ✅ Arrays with repeated elements  

#### 💡 Observations:
- Randomized Quicksort consistently outperforms deterministic on non-random distributions.
- Deterministic Quicksort can degrade to **O(n²)** in worst-case (e.g., sorted input).
- Runtime differences align well with theoretical expectations.

## 📌 Part 2: Hashing with Chaining

### 🔹 1. Implementation

- Implemented a **Hash Table using Chaining** (lists for each bucket).
- A **universal hash function** is used to minimize collisions:
 hash(key) = ((a * hash(key) + b) % p) % table_size

where:
- `a, b` are random constants
- `p` is a large prime number
- `table_size` is the number of buckets

### 🔹 Supported Operations

| Operation | Description |
|-----------|-------------|
| `insert(key, value)` | Adds or updates a key-value pair |
| `search(key)`        | Retrieves the value for a given key |
| `delete(key)`        | Removes the key-value pair |

### 🔹 2. Analysis

- Under **simple uniform hashing**, expected time for all operations is **O(1 + α)**, where:
- α = load factor = number of elements / number of slots
- **Load Factor Impact**:
- High α → longer chains → slower operations
- Low α → efficient constant-time behavior

### 🔹 Collision Minimization Strategies

- Use a **universal hash function**
- Keep **α < 1** via:
- Table resizing (rehashing)
- Choosing prime number table sizes
- Dynamic expansion based on threshold

### 🔹 Files
- `hash_table_chaining.py`

---

## 🧪 How to Run

### 1. Prerequisites

- Python 3.x
- `matplotlib` for plotting (used in quicksort):
```bash
pip install matplotlib

#### Run Sorting Analysis
python part1.py

#### Run Hash Table Demo
python part2.py
