##### What is the difference between list and tuple?
The difference between list and tuple is that list is mutable while tuple is not. Tuple can be hashed for e.g as a key for dictionaries.

##### What is PEP 8?
PEP 8 is a coding convention, a set of recommendation, about how to write your Python code more readable.


##### What does ** (double star/asterisk) and * (star/asterisk) do for parameters?
[The syntax is the  `*`  and  `**`](http://docs.python.org/tutorial/controlflow.html#arbitrary-argument-lists). The names  `*args`  and  `**kwargs`  are only by convention but there's no hard requirement to use them.

You would use  `*args`  when you're not sure how many arguments might be passed to your function, i.e. it allows you pass an arbitrary number of arguments to your function. For example:

```python
>>> def print_everything(*args):
        for count, thing in enumerate(args):
...         print( '{0}. {1}'.format(count, thing))
...
>>> print_everything('apple', 'banana', 'cabbage')
0. apple
1. banana
2. cabbage
```

Similarly,  `**kwargs`  allows you to handle named arguments that you have not defined in advance:

```python
>>> def table_things(**kwargs):
...     for name, value in kwargs.items():
...         print( '{0} = {1}'.format(name, value))
...
>>> table_things(apple = 'fruit', cabbage = 'vegetable')
cabbage = vegetable
apple = fruit
```

You can use these along with named arguments too. The explicit arguments get values first and then everything else is passed to  `*args`  and  `**kwargs`. The named arguments come first in the list. For example:

```python
def table_things(titlestring, **kwargs)
```

You can also use both in the same function definition but  `*args`  must occur before  `**kwargs`.

You can also use the  `*`  and  `**`  syntax when calling a function. For example:

```python
>>> def print_three_things(a, b, c):
...     print( 'a = {0}, b = {1}, c = {2}'.format(a,b,c))
...
>>> mylist = ['aardvark', 'baboon', 'cat']
>>> print_three_things(*mylist)
a = aardvark, b = baboon, c = cat
```

As you can see in this case it takes the list (or tuple) of items and unpacks it. By this it matches them to the arguments in the function. Of course, you could have a  `*`  both in the function definition and in the function call.
[stackoverflow](https://stackoverflow.com/questions/3394835/use-of-args-and-kwargs)

##### When to use `__new__` vs. `__init__` ?
Use ` __new__ `when you need to control the creation of a new instance.
Use `__init__` when you need to control initialization of a new instance.

`__new__` is the first step of instance creation.  It's called first,
and is responsible for returning a new instance of your class.  In
contrast, `__init__` doesn't return anything; it's only responsible for
initializing the instance after it's been created.

In general, you shouldn't need to override `__new__ `unless you're
subclassing an immutable type like str, int, unicode or tuple.
[stackoverflow](http://stackoverflow.com/questions/674304/pythons-use-of-new-and-init)

##### what's a lambda function?
Lambda comes from the  [Lambda Calculus](http://en.wikipedia.org/wiki/Lambda_calculus)  and refers to anonymous functions in programming.

Why is this cool? It allows you to write quick throw away functions without naming them. It also provides a nice way to write closures. With that power you can do things like this.


```python
def adder(x):
    return lambda y: x + y
add5 = adder(5)
add5(1)
6
```

As you can see from the snippet of Python, the function adder takes in an argument x, and returns an anonymous function, or lambda, that takes another argument y. That anonymous function allows you to create functions from functions. This is a simple example, but it should convey the power lambdas and closures have.
[stackoverflow](https://stackoverflow.com/questions/16501/what-is-a-lambda-function/16509)
