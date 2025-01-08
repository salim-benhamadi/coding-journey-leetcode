# Linked List Cheatsheet 🔗

## What is a Linked List?
A linked list is a linear data structure where elements are stored in nodes, and each node points to the next node in the sequence. Unlike arrays, linked lists don't store elements in contiguous memory locations.

## Types of Linked Lists
1. **Singly Linked List**: Each node points to the next node
2. **Doubly Linked List**: Each node points to both next and previous nodes
3. **Circular Linked List**: Last node points back to first node

## When to Use Linked Lists?
1. **Dynamic Size**: When you need frequent insertions/deletions
2. **Memory Usage**: When memory is fragmented
3. **Stack/Queue Implementation**: Efficient for implementing these ADTs
4. **Undo Functionality**: Easy to implement with doubly linked lists
5. **Memory Management**: Used in memory allocation systems

## Advantages & Disadvantages

### Advantages
- Dynamic size
- Easy insertion/deletion
- No memory waste
- Can grow as needed
- Efficient memory utilization

### Disadvantages
- No random access
- Extra memory for pointers
- Not cache friendly
- No backward traversal (in singly linked)
- Complex to reverse

## Basic Implementation

### Node Structure
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
```

### Doubly Node Structure
```python
class DoublyNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev
```

## Common Patterns

### 1. Basic Traversal
```python
def traverse(head):
    current = head
    while current:
        # process current.val
        current = current.next
```

### 2. Dummy Node Pattern
```python
def dummy_pattern(head):
    dummy = ListNode(0)
    dummy.next = head
    current = dummy
    # ... operations ...
    return dummy.next
```

### 3. Fast/Slow Pointers
```python
def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
```

## Essential Operations

### 1. Insertion
```python
# At beginning
def insert_start(head, val):
    new_node = ListNode(val)
    new_node.next = head
    return new_node

# After a node
def insert_after(node, val):
    new_node = ListNode(val)
    new_node.next = node.next
    node.next = new_node

# At end
def insert_end(head, val):
    if not head:
        return ListNode(val)
    current = head
    while current.next:
        current = current.next
    current.next = ListNode(val)
    return head
```

### 2. Deletion
```python
# Delete first node
def delete_first(head):
    if head:
        return head.next
    return None

# Delete after node
def delete_next(node):
    if node.next:
        node.next = node.next.next

# Delete by value
def delete_value(head, val):
    if not head:
        return None
    if head.val == val:
        return head.next
    
    current = head
    while current.next and current.next.val != val:
        current = current.next
    if current.next:
        current.next = current.next.next
    return head
```

### 3. Reverse List
```python
def reverse(head):
    prev = None
    curr = head
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    return prev
```

## Advanced Operations

### 1. Merge Sorted Lists
```python
def merge_lists(l1, l2):
    dummy = ListNode(0)
    curr = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 or l2
    return dummy.next
```

### 2. Cycle Detection
```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
```

## Common Problems & Solutions

### 1. Finding Length
```python
def get_length(head):
    length = 0
    current = head
    while current:
        length += 1
        current = current.next
    return length
```

### 2. Finding Nth Node from End
```python
def find_nth_from_end(head, n):
    first = second = head
    # Move first n steps ahead
    for _ in range(n):
        first = first.next
    # Move both until first reaches end
    while first:
        first = first.next
        second = second.next
    return second
```

## Common Edge Cases to Handle
1. Empty list (`None`)
2. Single node
3. Two nodes
4. Cycle present
5. No cycle
6. Multiple cycles
7. Same values in nodes

## Complexity Analysis
| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Access    | O(n)           | O(1)            |
| Search    | O(n)           | O(1)            |
| Insertion | O(1)*          | O(1)            |
| Deletion  | O(1)*          | O(1)            |
| Traversal | O(n)           | O(1)            |

*When position is known

## Debug Helper
```python
def print_list(head, max_nodes=100):
    nodes = []
    curr = head
    while curr and len(nodes) < max_nodes:
        nodes.append(str(curr.val))
        curr = curr.next
    print(" -> ".join(nodes))
```

Remember: Always handle edge cases and use dummy nodes when modifying the head of the list!s