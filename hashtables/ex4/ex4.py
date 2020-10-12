"""
For an input list of integers, we wish to know which positive numbers
have corresponding negative numbers in the list.

Example input:

```python
[ 1, -1, 2, 3, -4, -3, 4, -5, 6, 7 ]

Example return value:

```python
[ 1, 3, 4 ]
"""

def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # create dict
    num_dict = dict()

    # numbers as keys, positive numbers marked True as values
    for num in a:
        if num > 0:
            num_dict[num] = True
        else:
            num_dict[num] = False
    print(num_dict)

    # loop through a
    result = []
    for num in num_dict:
        if num_dict[num] is True and -num in num_dict:
            result.append(num)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
