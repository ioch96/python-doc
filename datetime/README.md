# Datetime

```python
from datetime import datetime

print(datetime.now()) # 2024-07-25 21:20:13.970513
print(type(datetime.now())) # <class 'datetime.datetime'>

print(datetime.now().strftime("%Y")) # 2024
print(datetime.now().strftime("%m")) # 07
print(datetime.now().strftime("%d")) # 25
print(datetime.now().strftime("%H")) # 21
print(datetime.now().strftime("%M")) # 20

print(datetime.now().strftime("Today is %d/%m/%Y.")) # Today is 25/07/2024.
print(type(datetime.now().strftime("Today is %d/%m/%Y."))) # <class 'str'>
```

- Εάν αλλάξω την ώρα του συστήματος από τις ρυθμίσεις του υπολογιστή, τότε η Python αυτόματα διαβάζει την ώρα του συστήματος.
