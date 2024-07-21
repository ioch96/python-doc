# My Python Documentation

- [ ] Pylint
- [ ] Docstrings
- [ ] RST
- [ ] Try...Exceptions
- [ ] ...

## Try-Except-Else-Finally

```python
# Example 1
print("Example 1\n")
try:
    print("Try 1/0...")
    print(1/0)
except:
    print("Except...")
else:
    print("Else...")
finally:
    print("End...")

# Example 2
print("\nExample 2\n")
try:
    print("Try...")
except:
    print("Except...")
else:
    print("Else...")
finally:
    print("End...")
```

- In **Example 1**, the `try` block partially executes until an exception is raised, triggering the `except` block. The `else` block is skipped, and the `finally` block always executes.
- In **Example 2**, the `try` block executes fully without any exceptions, so the `except` block is skipped. The `else` block executes, followed by the `finally` block which always executes.

## all() function

```python
# Example 1: All elements are True
list1 = [True, True, True]
print("Example 1:", all(list1))  # Output: True

# Example 2: Not all elements are True
list2 = [True, False, True]
print("Example 2:", all(list2))  # Output: False

# Example 3: List with 0 (0 is considered False in Python)
list3 = [1, 2, 0, 4]
print("Example 3:", all(list3))  # Output: False

# Example 4: Empty list (should return True, as there are no False elements)
list4 = []
print("Example 4:", all(list4))  # Output: True

# Example 5: Using all() with a list of strings
list5 = ["Hello", "World", "Python"]
print("Example 5:", all(list5))  # Output: True

# Example 6: Using all() with a list of mixed types
list6 = [1, "Python", True]
print("Example 6:", all(list6))  # Output: True

# Example 7: Using all() with a generator expression
list7 = [1, 2, 3, 4, 5]
print("Example 7:", all(x > 0 for x in list7))  # Output: True
```

Example 4:

- `list4` is empty.
- `all(list4)` returns `True` because there are no elements to be False.
