# Introduction
Understanding object mutability is fundamental to writing efficient Python code. Through recent exploration of list copying, tuple behavior, and function argument handling, I discovered how Python's treatment of objects impacts program behavior in surprising ways. Let me walk you through these concepts with practical examples.

# ID and Type
Every Python object has a unique identity (accessed via id()) and type (checked with type()):

```python
a = 42
print(f"ID: {id(a)}, Type: {type(a)}")  # ID: 140735812780912, Type: <class 'int'>

b = [1, 2]
print(f"ID: {id(b)}, Type: {type(b)}")  # ID: 2465487900224, Type: <class 'list'>
```

# Mutable Objects
Mutable objects can change their value while keeping the same identity. Lists and dictionaries are prime examples:

```python
colors = ['red', 'blue']
print(f"Before: {id(colors)}")  # Before: 2465487900224
colors.append('green')
print(f"After: {id(colors)}")   # After: 2465487900224 (same ID!)
```

# Immutable Objects
Immutable objects cannot be changed after creation. Numbers, strings, and tuples demonstrate this:

```python
name = "Python"
try:
    name[0] = 'J'  # TypeError: 'str' object does not support item assignment
except TypeError as e:
    print(e)

# Tuple gotcha
single_element = (1)    # Not a tuple!
actual_tuple = (1,)     # Correct single-element tuple
print(type(single_element))  # <class 'int'>
print(type(actual_tuple))    # <class 'tuple'>
```

# Why Mutability Matters
Python treats mutable and immutable objects differently in memory management and function argument passing. This impacts performance and program behavior:

```python
# Immutable (new object created)
x = 5
y = x
y += 1
print(x)  # 5 (unchanged)

# Mutable (same object modified)
list_a = [1, 2]
list_b = list_a
list_b.append(3)
print(list_a)  # [1, 2, 3] (changed!)
```

Function Argument Passing
Python uses pass-by-object-reference, meaning functions receive references to original objects:

```python
def modify(items):
    items.append('new')  # Affects original list
    items = [1, 2, 3]    # Creates new local reference

data = ['original']
modify(data)
print(data)  # ['original', 'new']
```
