import random
import sys
import time
import matplotlib.pyplot as plt

# Increase recursion depth
sys.setrecursionlimit(10000)

# ----------------------------
# Randomized Quicksort
# ----------------------------
def randomized_partition(arr, low, high):
    if low >= high:
        return low
    pivot_index = random.randint(low, high)
    arr[high], arr[pivot_index] = arr[pivot_index], arr[high]
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomized_quicksort(arr, low, high):
    if low < high:
        pivot_index = randomized_partition(arr, low, high)
        if pivot_index == low and pivot_index == high:
            return
        randomized_quicksort(arr, low, pivot_index - 1)
        randomized_quicksort(arr, pivot_index + 1, high)

# ----------------------------
# Deterministic Quicksort (mid pivot)
# ----------------------------
def deterministic_partition(arr, low, high):
    mid = (low + high) // 2
    pivot = arr[mid]
    arr[low], arr[mid] = arr[mid], arr[low]
    i = low + 1
    j = high
    while True:
        while i <= j and arr[i] <= pivot:
            i += 1
        while i <= j and arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            break
    arr[low], arr[j] = arr[j], arr[low]
    return j

def deterministic_quicksort(arr, low, high):
    if low < high:
        pivot_index = deterministic_partition(arr, low, high)
        if pivot_index == low and pivot_index == high:
            return
        deterministic_quicksort(arr, low, pivot_index - 1)
        deterministic_quicksort(arr, pivot_index + 1, high)

# ----------------------------
# Benchmarking
# ----------------------------
def time_sort(sort_fn, arr):
    arr_copy = arr.copy()
    start = time.time()
    sort_fn(arr_copy, 0, len(arr_copy) - 1)
    return time.time() - start

def generate_arrays(size):
    return {
        "Random": [random.randint(0, size) for _ in range(size)],
        "Sorted": list(range(size)),
        "Reverse": list(range(size, 0, -1)),
        "Repeated": [random.choice([1, 2, 3, 4, 5]) for _ in range(size)],
    }

def benchmark_distributions(sizes):
    distributions = ["Random", "Sorted", "Reverse", "Repeated"]
    results = {dist: {"Randomized": [], "Deterministic": []} for dist in distributions}

    for size in sizes:
        arrays = generate_arrays(size)
        print(f"\nBenchmarking input size: {size}")
        for dist in distributions:
            arr = arrays[dist]
            time_r = time_sort(randomized_quicksort, arr)
            time_d = time_sort(deterministic_quicksort, arr)
            results[dist]["Randomized"].append(time_r)
            results[dist]["Deterministic"].append(time_d)
            print(f"{dist:<10} | Randomized: {time_r:.6f} sec | Deterministic: {time_d:.6f} sec")

    return results

# ----------------------------
# Main Execution
# ----------------------------
if __name__ == "__main__":
    sizes = [100, 500, 1000, 2000, 5000]
    results = benchmark_distributions(sizes)

    # Plot results
    for dist in results:
        plt.figure()
        plt.plot(sizes, results[dist]["Randomized"], label="Randomized Quicksort", marker='o')
        plt.plot(sizes, results[dist]["Deterministic"], label="Deterministic Quicksort", marker='x')
        plt.xlabel("Input Size")
        plt.ylabel("Time (seconds)")
        plt.title(f"Quicksort Performance on {dist} Arrays")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()
