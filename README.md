# My Python Documentation

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

- In **Example 1**, the try block partially executes until an exception is raised, triggering the except block. The else block is skipped, and the finally block always executes.
- In **Example 2**, the try block executes fully without any exceptions, so the except block is skipped. The else block executes, followed by the finally block which always executes.
