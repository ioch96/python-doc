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
