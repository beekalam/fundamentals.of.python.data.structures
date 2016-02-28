class SavingsAccount(object):
    """This class represents a savings account
    with the owner's name, PIN, and balance. """

    def __init__(self, name, pin, balance = 0.0):
        self._name = name;
        self._pin = pin;
        self._balance = balance

    def __lt__(self, other):
        return self._name < other._name


if __name__ == "__main__":
    s1 = SavingsAccount("Ken", "1000", 0)
    s2 = SavingsAccount("Bill", "1001", 30)
    print (s1 < s2)
    print (s1 > s2)
    print (s2 > s1)
    print (s2 == s1)
