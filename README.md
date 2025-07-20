# MSCS-532-B01-Assignment3
# Hash Table with Chaining - Algorithm Efficiency Assignment

## Overview

This project implements a **hash table using chaining** as a collision resolution technique. The hash table supports efficient operations including:

- `Insert`: Add a key-value pair.
- `Search`: Retrieve the value associated with a key.
- `Delete`: Remove a key-value pair from the table.

A **universal hash function** is used to minimize collisions and improve the distribution of keys across buckets.

---

## Features

✅ Universal Hash Function  
✅ Chaining with Linked Lists (Python Lists)  
✅ Insert, Search, and Delete Support  
✅ Customizable Table Size  
✅ Print-Friendly Display of Buckets  

---

## Hash Function

We use the **universal hashing** scheme:

hash(key) = ((a * hash(key) + b) % p) % table_size


Where:
- `a` and `b` are random integers,
- `p` is a large prime number,
- `table_size` is the number of buckets in the hash table.

This approach ensures better key distribution and fewer collisions on average.

---

## How to Run

### 1. Clone or download the repository

### 2. Run the script
```bash
python part1.py
python part2.py
