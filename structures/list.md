# Lists

In a way, you have been using lists already. A string is known as an array of __char__acter__s__. Think of a list as a smarter string, except you can put anything into it.

## Creating a list

To create an empty list you do the following:

```py
l0 = list() # l0 = []
l1 = []
```
To create a list with some known values you do the following:

```py
l0 = [2,4,"cat",3.45]
```

Notice that I have floats, ints, and strings inside the same list.

### Alias and cloning

Look at the following code:

```py
l0 = [2,3,4]
l1 = l0
l2 = list(l0)
l0.remove(3)
l3 = l2 + l1
l1.append(1)
```

The function `remove(item)` looks through the list and finds the first occurrence of that `item` (known as an *element*) and removes it from the list. If the list was `[1,2,3,1]` and you did used `remove(1)`, you would have the list `[2,3,1]`.

The function `append(item)` takes the item and adds it to the end of the list. The opposite of this is a function called `pop()` that removes *and returns* the last element in the list.

After this code runs, what are the values of `l0`, `l1`, `l2`, and `l3`? Don't go to the next section until you've made a guess.

#### Answers

Here are the values:

```
l0 = [2,4,1]
l1 = [2,4,1]
l2 = [2,3,4]
l3 = [2,3,4,2,4]
```

Why are `l0` and `l1` the same? Because `l1` is an alias for `l0`. They are different variable names but they are connected (pointing) to the same data in the computer. Why are `l0` and `l2` different? Because `list()` has two meanings: `list()` and `list(list)`. One of them creates an empty list, and the other makes a copy of the list. `l2` and `l0` have the same values of data, but they are not the same data.

`l3 = l2 + l1`

This is a good talking put about *operators*. An operator is a symbol (like ,!@#$%^& and so on) that is linked to a special action for that data. For ints and floats, it is addition. For strings it is concatenation. Lists use the `+` for concatenation. I am appending the elements of the second list to the end of the first list.

### (Member) functions of a list

Here are some important member functions of lists:

* [i]
* del
* append(a)
* insert(i,a)
* remove(a)
* pop(i= -1)
* index(a)
* count(a)
* sort()
* reverse()

All functions for data structures either access, modify, and create.

#### Create

We've talked about `list()` and `= []` earlier in the lecture. They are used to create new representation of data in your program.

#### Access

The function `[i]` takes an int value and will `return` the value at that place in the list. If I have `l0 = [5,4,1]`, and `print l0[1]`, the program will print the returned value of `4`.

#### Modify

We already explained `append()`, `remove()`, and `pop()`, but I want to hit `pop()` one more time. The notation `i = -1` means that if you _do not_ put a value into the function `pop()`, the function will assume the value is `-1`. The `pop()` function's action is comparable to the using `[i]` followed by `del l0[i]`. The function `del` deletes an element at a certain place (an index) in the list.

The function `insert(i,a)` takes a index value, i, and an element, a, and adds that element to that position in the list.
``` py
l0 = [0,1,2,3]
l0.insert(2,"here")
print l0
```

This would print `[0,1,"here",2,3]`. Notice that it pushes everything back.
