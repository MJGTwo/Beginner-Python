# Member Functions
Member function is a special name for a function that is "inside" a datatype.

``` python
s1 = "hello"
print s1.upper()
```
would display `HELLO` instead of `hello`. The following would not work

```python
num = 5
print num.upper()
```
It would cause an error because num is an int and does not have the .upper() function because .upper() is a member function of string.

## Member and non-member

The point of a member function is that it is just like any other function that you use or write, but it is only used with a certain datatype and possibly edits the data. The function `len()` is a function but the functions `.lower()` and `.isdigit()`are member functions.

### Are there a lot of member functions?

Yes. There are a lot of member functions that are used for strings and things that store strings and other data. To list them would be a waste of time. I will use them or suggest them in homework assignments and worksheets.
