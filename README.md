# Very Simple Timestamp Decorator Function

To return a timestamp of how long the function took to run :
```python

>>> @timestamp.timestamp
... def testing():
...     time.sleep(12)
...     return

```

Output :
```python

>>> testing()
[I] testing took 12010ms to complete, or ~0m, or ~12s

```