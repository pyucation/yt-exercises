"""
Topic: Generators
Difficulty: 4/5
Requires: functions

Task:
Write a generator that returns the numbers that are divisable by 5 in a given
range of 0 to N.

Additional Task: Rewrite your generator in a way that it can be used to create
a generator for numbers divisable by 3, 5 and 8, using closures.
Example:
div_by_3 = div_gen(3)
for i in div_by_3(30):
    print(i)
# output: 0, 3, 6, ...
"""
