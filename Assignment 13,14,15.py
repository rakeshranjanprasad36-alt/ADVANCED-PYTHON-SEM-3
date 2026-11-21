# Assignment 13

# Step 1: Import the threading module
import threading

# Step 2: Define the first task
def task1():
    # Print messages to show that Task 1 is running
    for i in range(1, 4):
        print("Task 1 - Counting:", i)

# Step 3: Define the second task
def task2():
    # Print messages to show that Task 2 is running
    for i in range(1, 4):
        print("Task 2 - Counting:", i)

# Step 4: Define the third task
def task3():
    # Print messages to show that Task 3 is running
    for i in range(1, 4):
        print("Task 3 - Counting:", i)

if __name__ == "__main__":
    # Step 5: Create separate threads for the three tasks
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)
    t3 = threading.Thread(target=task3)

    # Step 6: Start all threads
    # start() allows each thread to begin execution concurrently.
    t1.start()
    t2.start()
    t3.start()

    # Step 7: Wait until all threads finish
    # join() prevents the main program from finishing too early.
    t1.join()
    t2.join()
    t3.join()

    # Step 8: Print the final message
    print("All tasks completed!")


# Assignment 14

# Step 1: Import the required modules
import gc
import tracemalloc
import time

# Step 2: Define a class for creating cyclic objects
class Node:
    def __init__(self):
        # Each node will store a reference to another node
        self.reference = None

if __name__ == "__main__":
    # Step 3: Start memory tracking
    # tracemalloc helps us measure Python memory allocations.
    tracemalloc.start()

    # Step 4: Create objects that refer to each other
    def create_cycles(number):
        for i in range(number):
            # Create two objects
            a = Node()
            b = Node()

            # Make the objects refer to each other
            # This creates a reference cycle.
            a.reference = b
            b.reference = a

            # When the function ends, the local variables disappear.
            # The objects still refer to each other, so the cycle
            # cannot be cleaned up by reference counting alone.

    # Step 5: Create many cyclic objects
    create_cycles(10000)

    # Step 6: Measure memory before manual collection
    current_before, peak_before = tracemalloc.get_traced_memory()

    # Display memory in kilobytes
    print("Memory before GC:",
        round(current_before / 1024, 2), "KB")

    # Step 7: Measure the time taken by manual garbage collection
    start_time = time.perf_counter()

    # Request garbage collection manually
    collected = gc.collect()

    # Calculate the time taken in seconds
    gc_time = time.perf_counter() - start_time

    # Step 8: Measure memory after collection
    current_after, peak_after = tracemalloc.get_traced_memory()

    # Step 9: Display the results
    print("Objects collected:", collected)

    print("Memory after GC:",
        round(current_after / 1024, 2), "KB")

    print("Peak traced memory:",
        round(peak_after / 1024, 2), "KB")

    print("GC execution time:",
        round(gc_time, 6), "seconds")

    # Step 10: Stop memory tracking
    tracemalloc.stop()


#Assignment 15

# Step 1: Import the required modules
import gc
import tracemalloc
import time

# Step 2: Define a class for creating cyclic objects
class Node:
    def __init__(self):
        self.reference = None

# Step 3: Start memory tracking
tracemalloc.start()

# Step 4: Create objects that refer to each other
def create_cycles(number):
    for i in range(number):
        # Create two objects
        a = Node()
        b = Node()

        # Create a reference cycle
        a.reference = b
        b.reference = a

# Step 5: Create many cyclic objects
create_cycles(10000)

# Step 6: Measure memory before garbage collection
current_before, peak_before = tracemalloc.get_traced_memory()

print("Memory before GC:", round(current_before / 1024, 2), "KB")

# Step 7: Measure garbage collection time
start_time = time.perf_counter()

# Manually run garbage collection
collected = gc.collect()

gc_time = time.perf_counter() - start_time

# Step 8: Measure memory after garbage collection
current_after, peak_after = tracemalloc.get_traced_memory()

# Step 9: Display the results
print("Objects collected:", collected)

print("Memory after GC:", round(current_after / 1024, 2), "KB")

print("Peak traced memory:", round(peak_after / 1024, 2), "KB")

print("GC execution time:", round(gc_time, 6), "seconds")

# Step 10: Stop memory tracking
tracemalloc.stop()
