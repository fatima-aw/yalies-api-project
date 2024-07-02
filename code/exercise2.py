# WRITE YOUR CODE HERE
def move_to_bottom(d, key):
    if key not in d:
        return "The key is not in the dictionary"
    
    value = d.pop(key)  # Remove the key and get its value
    d[key] = value  # Reinsert the key-value pair at the end of the dictionary
    return d

# Test cases
if __name__ == "__main__":
    example_dict = {
        1: 'one',
        2: 'two',
        3: 'three'
    }

    # Test Case 1
    result = move_to_bottom(example_dict, 1)
    print(result)  # Output should be {2: 'two', 3: 'three', 1: 'one'}

    example_dict = {
        1: 'one',
        2: 'two',
        3: 'three'
    }

    # Test Case 2
    result = move_to_bottom(example_dict, 2)
    print(result)  # Output should be {1: 'one', 3: 'three', 2: 'two'}

    example_dict = {
        1: 'one',
        2: 'two',
        3: 'three'
    }

    # Test Case 3
    result = move_to_bottom(example_dict, 4)
    print(result)  # Output should be "The key is not in the dictionary"


# test code below

