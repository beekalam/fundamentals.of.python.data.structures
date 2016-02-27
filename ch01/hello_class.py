__author__ = 'admin'

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

if __name__ == "__main__":
    c1 = Counter()
    print(c1)
    print(c1.getValue())
    print(str(c1))
    c1.increment(5)
    print(c1)
    c1.reset()
    print(c1)

    c2 = Counter()
    print(Counter.instances)

    print(c1 == c1)
    print(c1 == 0)
    print(c1 == c2)
    c2.increment()
    print(c1 == c2)

