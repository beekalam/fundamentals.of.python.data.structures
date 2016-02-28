
def indexOfMin(lyst):
    """Returns the index of the minimum item."""
    # The algorithms complexity is o(n).
    minIndex = 0
    currentIndex = 1
    while currentIndex < len(lyst):
        if lyst[currentIndex] < lyst[minIndex]:
            minIndex = currentIndex
        currentIndex += 1

    return minIndex

if __name__ == "__main__":
    lyst = [12, 0, 1 , -1, 2]
    print(indexOfMin(lyst))
