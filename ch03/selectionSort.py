from swap import swap

def selectionSort(lyst):
    # O(n^2)
    i = 0
    while i < len(lyst) - 1:    # Do n - 1 searches
        minIndex = i            # for the smallest
        j = i + 1
        while j < len(lyst):    # start a search
            if lyst[j] < lyst[minIndex]:
                minIndex = j
            j += 1
        if minIndex != i:       # Exchange if needed
            swap(lyst, minIndex, i)
        i += 1


if __name__ == "__main__":
    lyst = [1, 0, -1, 2, -2]
    selectionSort(lyst)
    print(lyst)
