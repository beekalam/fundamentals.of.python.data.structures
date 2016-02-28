def sequentialSearch(target, lyst):
    """Returns the position of the target item found, or -1 otherwise."""
    position = 0
    while position < len(lyst):
        if target == lyst[position]:
            return position
        position += 1

    return -1

if __name__ == "__main__":
    lyst = [1, 2, -1, 0, -2]
    print(sequentialSearch(-2, lyst))       # worst case o(n)
    print(sequentialSearch(1, lyst))        # best case o(1)
