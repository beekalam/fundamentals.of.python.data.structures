"""
File: countfib.py
Prints the number of calls of a recursive Fibonacci
function with problem sizes that double.
"""
class Counter(object):
    """Models a counter"""

    #class variable
    instances = 0

    #constructor
    def __init__(self):
        """sets up counter"""
        Counter.instances += 1
        self.reset()

    #Mutator methods
    def reset(self):
        """sets the counter to 0."""
        self._value = 0

    def increment(self, amount = 1):
        """Adds amount to the counter."""
        self._value += amount

    def decrement(self, amount = 1):
        """Subtracts amount from the counter."""
        self._value -= amount

    #accessor methods
    def getValue(self):
        """Returns the counter's value."""
        return self._value

    def __str__(self):
        """Returns the string representation of the counter."""
        return str(self._value)

    def __eq__(self, other):
        """Returns True if self equals other or False otherwise"""
        if self is other: return True
        if type(self) != type(other): return False
        return self._value == other._value

def fib(n, counter):
    """Count the number of calls of the Fibonacci function"""
    counter.increment()
    if n < 3:
        return 1
    else:
        return fib(n - 1, counter) + fib(n - 2, counter)

if __name__ == "__main__":

    problemSize = 2
    print("%12s%15s" % ("Problem Size", "Calls"))
    for count in range(5):
        counter = Counter()

        #The start of the algorithm
        fib(problemSize, counter)
        #The end of the algorithm

        print("%12d%15s" % (problemSize, counter))
        problemSize *= 2
