# Two Pointers Cheatsheet 🎯



| Pattern & Use Cases | Example Code |
|---|---|
| **Opposite Direction** <br>• Finding pairs summing to target<br>• Container with most water<br>• Trapping rain water<br>• Palindrome verification | ```python
left, right = 0, len(arr)-1
while left < right:
    if condition(arr[left], arr[right]):
        # process result
        left += 1
    else:
        right -= 1
``` |
| **Fast/Slow Pointers** <br>• Remove duplicates<br>• Finding cycle in linked list<br>• Middle of linked list<br>• Array partitioning | ```python
slow = 0  # or head for linked list
for fast in range(len(arr)):
    if condition(arr[fast]):
        arr[slow] = arr[fast]
        slow += 1
``` |
| **Sliding Window** <br>• Subarray with sum k<br>• Longest substring without repeats<br>• Min window substring<br>• Max consecutive ones | ```python
left = curr_sum = 0
for right in range(len(arr)):
    # add arr[right] to window
    while invalid_window():
        # remove arr[left] from window
        left += 1
``` |
| **Multiple Arrays** <br>• Merge sorted arrays<br>• Intersection of arrays<br>• Common elements<br>• Array difference | ```python
i = j = 0
while i < len(arr1) and j < len(arr2):
    if arr1[i] < arr2[j]:
        i += 1
    elif arr1[i] > arr2[j]:
        j += 1
    else:
        # process match
        i += 1
        j += 1
``` |

## Common Patterns to Identify 🔍

| Characteristic | Likely Solution |
|---|---|
| "Find pair of elements..." | Opposite direction pointers |
| "Sorted array..." | Two pointers (often opposite direction) |
| "Subarray/substring..." | Sliding window |
| "Remove duplicates..." | Fast/slow pointers |
| "Detect cycle..." | Fast/slow pointers |
| "Merge sorted..." | Multiple array pointers |

## Tips & Tricks 💡

| Tip | Example |
|---|---|
| Handle edge cases first | ```python
if not arr: return 0
if len(arr) == 1: return arr[0]
``` |
| Consider sorting first | ```python
arr.sort()  # Often simplifies two-pointer logic
``` |
| Use while loops for flexible movement | ```python
while left < right and arr[left] == arr[left-1]:
    left += 1
``` |
| Track additional state when needed | ```python
max_area = curr_sum = 0
visited = set()
``` |

## Time/Space Complexity 📊

| Pattern | Typical Time | Typical Space |
|---|---|---|
| Opposite Direction | O(n) | O(1) |
| Fast/Slow | O(n) | O(1) |
| Sliding Window | O(n) | O(1) or O(k) |
| Multiple Arrays | O(n+m) | O(1) or O(n) |