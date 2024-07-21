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
