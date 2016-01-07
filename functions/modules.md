# Modules

We can define functions and have them do whatever we want. The logical question to ask is "Do we have to define a function for everything? Like square roots or absolute values?"

No, we have modules!

Modules are collections of functions and values that other people have created that we can use in our code. In other languages, these are called libraries, but we will call them modules because that is what the Python community does.

## math

I don't want to through every module under the sun because there are a lot of modules, but I will talk about the math module.

To add a library to your code, you "import the module". Here is the code to import the math module and use it:

```python
import math

print math.pi
print math.ceil(4.5)
print math.ceil(4.1)
print math.trunc(math.pi)
print math.sqrt(3)

```
This would display:

`3.14159265359`

`5`

`5`

`3`

`1.77245385091`

If you ever wonder what is inside a module, you can do the following:

```python
import math
help(math)
```

The help() function is very useful for these sort of things.
