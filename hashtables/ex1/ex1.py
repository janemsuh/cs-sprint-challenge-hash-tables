"""
# Merging Two Packages

Given a package with a weight limit `limit` and a list `weights` of item
weights, implement a function `get_indices_of_item_weights` that finds
two items whose sum of weights equals the weight limit `limit`. Your
function will return a tuple of integers that has the following form:

```
(zero, one)
```

where each element represents the item weights of the two packages.
_**The higher valued index should be placed in the `zeroth` index and
the smaller index should be placed in the `first` index.**_ If such a
pair doesn’t exist for the given inputs, your function should return
`None`.

Your solution should run in linear time.
"""

def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # create dict
    weight_dict = dict()
    
    # weights as key, weight list index as value
    for i in range(0, length):
        weight_dict[weights[i]] = i

    # loop through weights
    for i in range(0, length):
        if limit - weights[i] in weight_dict:
            weight_index1 = i
            weight_index2 = weight_dict[limit - weights[i]]
            # check list index order
            if weight_index1 < weight_index2:
                weight_index1, weight_index2 = weight_index2, weight_index1
            return weight_index1, weight_index2

    return None

weights_test = [ 4, 6, 10, 15, 16 ]
print(get_indices_of_item_weights(weights_test, 5, 21))
# output: [ 3, 1 ]  # since these are the indices of weights 15 and 6 whose sum equals 21