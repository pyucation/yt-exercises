"""
Topic: Closures
Difficulty: 4/5
Requires: functions, first class functions, OOP

Task:
You are given a class called F, which represents a family of mathematical
functions f(x) = ax^2 + bx + c, where c is always set to 1.
Rewrite this class using the concept of closures, i.e. using an outer and
an inner function. Test your result.

Note, that we call the class capital F, because of the Python convention for
class names.
"""

import matplotlib.pyplot as plt


class F:
    # constant for every instance of the class
    c = 1
    
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self, x, *args, **kwargs):
        # return single value if x is int or float
        if isinstance(x, int) or isinstance(x, float):
            return self.a * x**2 + self.b * x + self.c
        # return list of values if x is list
        elif isinstance(x, list):
            squared = list(map(lambda x: x**2, x))
            # elementwise multiplication (we could have used numpy here, I know)
            return [self.a * sq + self.b * x_i + self.c for sq, x_i in zip(squared, x)]
        # raise type error in case of tuple or something else (just to make it
        # a bit more complex for you :))
        else:
            raise TypeError("Provided type not supported.")
    

simple_parabola = F(1, 1)
values = list(range(-4, 5))
print(simple_parabola(values))

# plot the function values
plt.scatter(values, simple_parabola(values))
plt.xlabel("x")
plt.ylabel("y")
plt.show()
