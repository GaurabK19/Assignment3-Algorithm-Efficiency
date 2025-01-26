import random
import time
import matplotlib.pyplot as plt
import sys

# Increase recursion limit
sys.setrecursionlimit(2000)

# Partition function
def partition(arr, low, high):
    pivot = arr[high]  # Pivot element
    i = low - 1  # Index of the smaller element
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap elements
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Place pivot in the correct position
    return i + 1

# Randomized Quicksort
def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)  # Choose pivot randomly
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  # Swap pivot with the last element
    return partition(arr, low, high)

def randomized_quicksort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        pivot_index = randomized_partition(arr, low, high)
        randomized_quicksort(arr, low, pivot_index - 1)
        randomized_quicksort(arr, pivot_index + 1, high)
    return arr

# Deterministic Quicksort with Median-of-Three Pivot
def deterministic_partition(arr, low, high):
    mid = (low + high) // 2
    pivot_candidates = [(arr[low], low), (arr[mid], mid), (arr[high], high)]
    pivot_candidates.sort(key=lambda x: x[0])
    pivot_index = pivot_candidates[1][1]  # Median value
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  # Move pivot to end
    return partition(arr, low, high)

def deterministic_quicksort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        pivot_index = deterministic_partition(arr, low, high)
        deterministic_quicksort(arr, low, pivot_index - 1)
        deterministic_quicksort(arr, pivot_index + 1, high)
    return arr

# Measure time for each algorithm
def measure_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr[:])
    return time.time() - start_time

# Generate test cases
def generate_test_cases(size):
    return {
        "random": [random.randint(1, 10000) for _ in range(size)],
        "sorted": list(range(1, size + 1)),
        "reverse_sorted": list(range(size, 0, -1)),
        "repeated": [random.randint(1, 10) for _ in range(size)],
    }

# Compare algorithms on different input distributions
if __name__ == "__main__":
    sizes = [100, 500, 1000, 5000, 10000]
    results = {"Randomized": [], "Deterministic": []}

    for size in sizes:
        print(f"\nArray Size: {size}")
        test_cases = generate_test_cases(size)

        for case_name, arr in test_cases.items():
            print(f"  Test Case: {case_name}")

            # Measure Randomized Quicksort
            rand_time = measure_time(randomized_quicksort, arr)
            print(f"    Randomized Quicksort: {rand_time:.6f} seconds")

            # Measure Deterministic Quicksort
            det_time = measure_time(deterministic_quicksort, arr)
            print(f"    Deterministic Quicksort: {det_time:.6f} seconds")

            # Store results for plotting (only for random arrays as an example)
            if case_name == "random":
                results["Randomized"].append(rand_time)
                results["Deterministic"].append(det_time)

    # Plot results
    plt.figure()
    plt.plot(sizes, results["Randomized"], label="Randomized Quicksort")
    plt.plot(sizes, results["Deterministic"], label="Deterministic Quicksort")
    plt.xlabel("Input Size")
    plt.ylabel("Time (seconds)")
    plt.title("Comparison of Randomized vs Deterministic Quicksort")
    plt.legend()
    plt.grid(True)
    plt.show()