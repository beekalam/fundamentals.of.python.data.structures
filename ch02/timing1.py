"""
File:timing1.py
Prints the running times for problem sizes that double,
using a single loop
"""
import time

if __name__ == "__main__":
    problemSize = 1000000
    print("%12s%16s" % ("ProblemSize", "Seconds"))
    for count in range(5):

        start = time.time()
        #The start of the algorithm
        work = 1
        for x in range(problemSize):
            work += 1
            work -= 1
        #The end of the algorithm
        elapsed = time.time() - start

        print("%12d%16.3f" % (problemSize, elapsed))
        problemSize *= 2