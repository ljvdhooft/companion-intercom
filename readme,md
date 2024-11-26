# Companion config builder

To use this repository, import the class `CompanionIntercom`:
```python
from CompanionIntercom import CompanionIntercom

c = CompanionIntercom()

c.createButton("button1", 1, [0, 1], ["/a/b 1", "/b/c 10"], ["/a/b 0", "/b/c 0"])
```

Alternatively, add a "listen" function to the button:
```python
c.createButton("button1", 1, [0, 1], ["/a/b 1", "/b/c 10"], ["/a/b 0", "/b/c 0"], ["x/y", "/q/t"], ["/x/y/vol"])
```

After the creation of all the buttons, you can create the special function buttons:

```python
c.createListenButton(1, [0, 0])
c.createVolUpButton(1, [1, 0])
c.createVolDownButton(1, [2, 0])
```

When finished, use the `.toJSON()` method to print out the entire config

```python
print(c.toJSON())
```