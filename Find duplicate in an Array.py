"""
Using Floyd's Tortoise and Hare Algorithm.
Used to detect cycles or repeating elements in a linked list or array.
We basically have two pointers, slow and fast. Slow pointer moves a single place and Fast pointer moves two places.
When both the pointers become equal, that means there is a cycle or repeating element. In fact, they meet in a circle,
the duplicate number must be the entry point of the circle when visiting the array from nums[0].
"""

arr = [3, 1, 3, 4, 2]
slow, fast = arr[0], arr[arr[0]]
print(slow, fast)
while slow != fast:
    slow = arr[slow]
    fast = arr[arr[fast]]
    print(slow, fast)
fast = 0
print("-----------------------------------------------------")
print(slow, fast)
while fast != slow:
    slow, fast = arr[slow], arr[fast]
    print(slow, fast)

print(slow)
