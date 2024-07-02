# WRITE YOUR CODE HERE
def find_key(d, value):
    for k, v in d.items():
        if v == value:
            return k
    return None  # Return None if the value is not found


# test code below

