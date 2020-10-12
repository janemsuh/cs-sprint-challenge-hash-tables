"""
Find the intersection between multiple lists of integers.
"""

def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # create dict
    num_dict = dict()

    # num as key, count as value
    for array in arrays:
        for num in array:
            if num not in num_dict:
                num_dict[num] = 1
            else:
                num_dict[num] += 1
            
    # loop through num_dict, add keys to result list if value equals number of arrays
    result = []
    for (num, count) in num_dict.items():
        if count == len(arrays):
            result.append(num)

    return result


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
