"""
Topic: Iterators
Difficulty: 4/5
Requires: OOP

Task:
Write an iterator class called BinaryEncoderIterator. The purpose of this class
is to binary encode a given sequence. For example: ['yes', 'no', 'no'] will
be transformed to [1, 0, 0].
Make sure the sequences contains at most two distinguishable categories.
After that, write a function binary_transform() taking a pandas dataframe, that
transforms a specified column with the help of your BinaryEncoderIterator class.
Do not use any pandas methods!

Example:
   answer   ->         answer
0  yes              0  1
1  no               1  0
2  no               2  0
3  yes              3  1
4  no               4  0
"""
import pandas as pd


d ={
    "answers": ["yes", "no", "no", "yes", "no", "yes", "no", "no"]
}
df = pd.DataFrame(d)


class BinaryEncoderIterator:
    ...


def binary_transformer():
    ...
