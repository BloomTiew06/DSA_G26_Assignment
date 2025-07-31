import time
import copy
import random

class SortingAlgorithms:
     
    """
    Performs Merge Sort on the input array.
    @param arr       - list of elements to sort
           tracing   - if True, prints split and merge steps
    """
    def MergeSort(self, arr, tracing=False):
        self._merge_sort_tree(arr, 0, len(arr) - 1, level=0, tracing=tracing)

    """
    -------------------------------------------------------------------------------------------
    Printing and formatting of the visualization was assisted with AI
    Partially modified from old pre U notes and https://www.geeksforgeeks.org/dsa/merge-sort/ 
    -------------------------------------------------------------------------------------------
    Recursively divides the array and merges sorted halves 
    private (helper) method for merge sort 
    @param arr        - list of elements to sort
            left      - starting index of the segment
            right     - ending index of the segment
            level     - current recursion depth (used for indentation in tracing)
            tracing   - if True, prints steps
    """
    def _merge_sort_tree(self, arr, left, right, level, tracing):
        indent = "│   " * level
        if tracing:
            print(f"{indent}Split: {arr[left:right+1]}")
        if left < right:
            mid = (left + right) // 2
            self._merge_sort_tree(arr, left, mid, level + 1, tracing)
            self._merge_sort_tree(arr, mid + 1, right, level + 1, tracing)
            # Merge step
            temp = []
            i, j = left, mid + 1
            while i <= mid and j <= right:
                if arr[i] < arr[j]:
                    temp.append(arr[i])
                    i += 1
                else:
                    temp.append(arr[j])
                    j += 1
            while i <= mid:
                temp.append(arr[i])
                i += 1
            while j <= right:
                temp.append(arr[j])
                j += 1
            for k in range(len(temp)):
                arr[left + k] = temp[k]
            if tracing:
                print(f"{indent}Merge: {arr[left:right+1]}")
    
    """
    --------------------------------------------------------------------------------
    Partially taken and modified from https://www.geeksforgeeks.org/dsa/shell-sort/
    --------------------------------------------------------------------------------
    Performs Shell Sort on the input array using gap reduction by half.
    @param arr       - list of elements to sort
           tracing   - if True, prints each step with current gap
    """
    def ShellSort(self, arr, tracing=False):
        n = len(arr)
        gap = n // 2
        step = 1
        while gap > 0:
            if tracing:
                print(f"\nStep {step}: Gap = {gap}")
            for i in range(gap, n):
                temp = arr[i]
                j = i
                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
                if tracing:
                    print("  ", arr)
            gap //= 2
            step += 1
    
    """
    Performs Quick Sort on the input array.
    @param arr       - list of elements to sort
           tracing   - if True, prints partitions and pivots
    """
    def QuickSort(self, arr, tracing=False):
        self._quick_sort_helper(arr, 0, len(arr) - 1, level=0, tracing=tracing)

    """
    ---------------------------------------------------------------------------------
    Visualization printing partially assisted with AI
    ---------------------------------------------------------------------------------
    Private/Helper function for Quick Sort using recursion and partitioning.
    @param arr       - list of elements to sort
           low       - starting index of the segment
           high      - ending index of the segment
           level     - current recursion depth (for tracing indentation)
           tracing   - if True, prints steps and pivots
    """
    def _quick_sort_helper(self, arr, low, high, level, tracing):
        indent = "│   " * level
        if tracing:
            print(f"{indent}QuickSort: {arr[low:high+1]}")
        if low < high:
            pi = self._partition(arr, low, high)
            if tracing:
                print(f"{indent}Pivot={arr[pi]} at index {pi}, after partition: {arr[low:high+1]}")
            self._quick_sort_helper(arr, low, pi - 1, level + 1, tracing)
            self._quick_sort_helper(arr, pi + 1, high, level + 1, tracing)

    """
    ---------------------------------------------------------------------------------------------------
    Partially taken and modified from https://www.geeksforgeeks.org/dsa/quick-sort-algorithm/
    ---------------------------------------------------------------------------------------------------
    Partitions the array around a pivot for Quick Sort.
    @param arr       - list of elements to sort
           low       - starting index
           high      - ending index (pivot element)
    """
    def _partition(self, arr, low, high):
        mid = (low + high) // 2
        if arr[low] > arr[mid]:
            arr[low], arr[mid] = arr[mid], arr[low]
        if arr[low] > arr[high]:
            arr[low], arr[high] = arr[high], arr[low]
        if arr[mid] > arr[high]:
            arr[mid], arr[high] = arr[high], arr[mid]
        pivot_index = mid
        pivot = arr[pivot_index]
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    """
    Performs Bubble Sort on the input array.
    @param arr       - list of elements to sort
           tracing   - if True, prints pass info and each comparison
    """
    def BubbleSort(self, arr, tracing=False):
        n = len(arr)
        # Note: If tracing is False (due to large array size), these prints won't execute.
        for i in range(n - 1):
            swapped = False
            if tracing:
                print(f"Pass {i+1}: {arr}")
            for j in range(0, n - i - 1):
                if tracing:
                    print(f"    Compare {arr[j]} and {arr[j+1]} -> ", end="")
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
                if tracing:
                    print(f"{arr}")  
            if tracing:
                print(f"End of Pass {i+1}: {arr}")
                print("="*60+"\n")
            if not swapped:
                if tracing:
                    print("No swaps. Array is sorted. Early termination.")
                break

    """
    Performs Selection Sort on the input array.
    @param arr       - list of elements to sort
           tracing   - if True, prints array after each swap
    """
    def SelectionSort(self, arr, tracing=False):
        n = len(arr)
        # Note: If tracing is False (due to large array size), these prints won't execute.
        for i in range(n - 1):
            min_idx = i
            if tracing:
                print(f"Searching for min from index {i} in: {arr[i:]}")
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            if min_idx != i:
                val_at_i = arr[i]
                val_at_min_idx = arr[min_idx]    
                arr[i], arr[min_idx] = arr[min_idx], arr[i] # Perform the swap
                if tracing:
                    print(f"    Swapped {val_at_i} (at index {i}) with {val_at_min_idx} (at index {min_idx}). Current array: {arr}")
            else:
                if tracing:
                    print(f"    No swap needed, {arr[i]} is already min at index {i}: {arr}")
            if tracing:
                print(f"Placed {arr[i]} at index {i}. Sorted part: {arr[:i+1]}")
                print("="*60+"\n")

    """
    Performs Insertion Sort on the input array.
    @param arr       - list of elements to sort
           tracing   - if True, prints array after each element is inserted
    """
    def InsertionSort(self, arr, tracing=False):
        n = len(arr)
        # Note: If tracing is False (due to large array size), these prints won't execute.
        for i in range(1, n):
            key = arr[i]
            j = i - 1
            if tracing:
                print(f"Consider element {key} at index {i}. Sorted part: {arr[:i]}")
            while j >= 0 and key < arr[j]:
                if tracing:
                    print(f"     Shifting {arr[j]} from {j} to {j+1} as {key} is smaller.")
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key
            if tracing:
                print(f"Inserted {key} at index {j+1}. Current array: {arr}")
                print("="*60+"\n")


if __name__ == "__main__":
    sorter = SortingAlgorithms()

    # --- Global tracing threshold ---
    # Set the maximum array size for which tracing/visualization will be enabled.
    # If array size exceeds this, tracing will be automatically disabled.
    MAX_TRACE_SIZE = 50 

    
    while True:
        # --- Array selection section ---
        print("Choose data array type:")
        print("1. Default array ([6, 7, 1, 5, 2, 4, 3, 9, 8, 0])")
        print("2. Generate random array")
        print("3. Generate sorted array")
        print("4. Generate reverse sorted array")
        print("5. Enter your own custom array")
        print("6. Exit")
        array_choice = input("Array Option [1-5]: ").strip()

        data = [] # Initialize data variable
        if array_choice == '1':
            data = [6, 7, 1, 5, 2, 4, 3, 9, 8, 0]
        elif array_choice in ['2', '3', '4']:
            while True:
                try:
                    array_size_str = input("Enter array size (e.g., 10, 100, 1000): ").strip()
                    array_size = int(array_size_str)
                    if array_size <= 0:
                        print("Please enter a positive integer for array size.")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")

            if array_choice == '2':
                data = [random.randint(0, array_size * 2) for _ in range(array_size)]
            elif array_choice == '3':
                data = list(range(array_size))
            elif array_choice == '4':
                data = list(range(array_size - 1, -1, -1))
        elif array_choice == '5':
            user_input = input("Enter your array (space or comma separated): ").strip()
            if ',' in user_input:
                parts = user_input.split(',')
            else:
                parts = user_input.split()
            try:
                data = [int(x) for x in parts]
            except ValueError:
                print("Invalid input. Please enter only integers.")
                continue
        elif array_choice == '6':
            exit()
        else:
            print("Invalid array option. Exiting.")
            exit()

        # Print only the first few elements if the array is very large for readability
        print(f"\n--- Using Array (first 20 elements if large): {data[:20]}{'...' if len(data) > 20 else ''} ---")

        # Determine if tracing should be active for visualization based on array size
        enable_tracing_for_viz = len(data) <= MAX_TRACE_SIZE

        # --- Sorting algorithm selection section ---
        print("\nChoose a sorting algorithm: ")
        print("1. Shell Sort")
        print("2. Merge Sort")
        print("3. Quick Sort")
        print("4. Bubble Sort")
        print("5. Selection Sort")
        print("6. Insertion Sort")
        ans = input("Sorting Algorithm Option [1-6] : ").strip()

        print() # spacing

        # Mapping of user option to algorithm name and function
        algorithm_map = {
            "1": ("Shell Sort", sorter.ShellSort),
            "2": ("Merge Sort", sorter.MergeSort),
            "3": ("Quick Sort", sorter.QuickSort),
            "4": ("Bubble Sort", sorter.BubbleSort),
            "5": ("Selection Sort", sorter.SelectionSort),
            "6": ("Insertion Sort", sorter.InsertionSort)
        }

        if ans in algorithm_map:
            alg_name, alg_func = algorithm_map[ans]
            
            # Only attempt visualization if within the trace size limit
            if enable_tracing_for_viz:
                print(f"{alg_name} Visualization:\n")
                data_copy_for_tracing = copy.deepcopy(data) # Copy for visualization
                alg_func(data_copy_for_tracing, tracing=True)
                print("\nFinal Sorted (from visualization):", data_copy_for_tracing)
            else:
                print(f"Array size ({len(data)}) exceeds tracing threshold ({MAX_TRACE_SIZE}).")
                print("Skipping visualization for performance, proceeding to timing comparison.\n")
                # No tracing, so no final sorted array from visualization to print
        else:
            print("Invalid option. Please choose between 1 and 6.")
            exit()

        # --- Time Comparison (tracing disabled) ---
        print("\n=== Timing Comparison ===")
        for name, func in algorithm_map.values():
            arr_copy_for_timing = copy.deepcopy(data) # Ensure a fresh copy for each timing
            start_time = time.perf_counter()
            func(arr_copy_for_timing, tracing=False) # Always disable tracing for timing measurements
            end_time = time.perf_counter()
            print(f"{name}: {end_time - start_time:.6f} seconds")
