def binarySearch(target, sortedLyst):
    left = 0
    right  = len(sortedLyst) - 1
    while left <= right:
        midpoint = (left + right) // 2
        if target == sortedLyst[midpoint]:
            return  midpoint
        elif target < sortedLyst[midpoint]:
            right =midpoint - 1
        else:
            left = midpoint + 1

    return -1

if __name__ == "__main__":
    lyst = [1, 12, 24, 32, 64]
    print(binarySearch(24, lyst))
