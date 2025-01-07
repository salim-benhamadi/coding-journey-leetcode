# Two Pointers Cheatsheet 🎯

## What are Two Pointers?
Two pointers is a technique where we use two reference points in an array/linked list to solve problems efficiently. Instead of using nested loops (O(n²)), we can often achieve O(n) complexity.

## When to Use?
1. Search for pairs in sorted array
2. In-place array manipulation
3. Sliding window scenarios
4. Linked list operations
5. String manipulation

## Key Benefits
- Reduces time complexity from O(n²) to O(n)
- Constant space complexity O(1)
- Efficient for sorted arrays
- Handles in-place operations

## Common Patterns

### 1. Opposite Direction
Used for: Finding pairs, container problems, palindromes
```python
left, right = 0, len(arr)-1
while left < right:
    if condition(arr[left], arr[right]):
        left += 1
    else:
        right -= 1
```

### 2. Fast/Slow Pointers
Used for: Remove duplicates, detect cycles, find middle
```python
slow = 0  # or head for linked list
for fast in range(len(arr)):
    if condition(arr[fast]):
        arr[slow] = arr[fast]
        slow += 1
```

### 3. Sliding Window
Used for: Subarrays with sum k, substring problems
```python
left = curr_sum = 0
for right in range(len(arr)):
    # add arr[right] to window
    while invalid_window():
        # remove arr[left]
        left += 1
```

### 4. Multiple Arrays
Used for: Merge sorted arrays, intersections
```python
i = j = 0
while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]: i += 1
    elif arr1[i] > arr2[j]: j += 1
    else:
        # process match
        i, j = i+1, j+1
```

## Problem Identifiers
- "Find pair of elements" → Opposite direction
- "Sorted array" → Two pointers
- "Subarray/substring" → Sliding window
- "Remove duplicates" → Fast/slow
- "Detect cycle" → Fast/slow
- "Merge sorted" → Multiple arrays

## Tips
1. Handle edge cases first
```python
if not arr: return 0
if len(arr) == 1: return arr[0]
```

2. Consider sorting first when order doesn't matter
```python
arr.sort()  # Often simplifies logic
```

3. Use while for flexible movement
```python
while left < right and arr[left] == arr[left-1]:
    left += 1
```

## Complexity Guide
- Opposite Direction: O(n) time, O(1) space
- Fast/Slow: O(n) time, O(1) space
- Sliding Window: O(n) time, O(1) or O(k) space
- Multiple Arrays: O(n+m) time, O(1) or O(n) space

## Common Mistakes to Avoid
1. Not handling edge cases
2. Incorrect pointer movement
3. Missing termination conditions
4. Not considering duplicates
5. Wrong pointer initialization

## Classic Problems
1. Two Sum
2. Container With Most Water
3. Remove Duplicates
4. Linked List Cycle
5. Palindrome Verification
6. Merge Sorted Arrays
7. Maximum Subarray Sum
8. Trapping Rain Water
