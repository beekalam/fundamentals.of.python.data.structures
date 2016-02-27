__author__ = 'admin'

if __name__ == "__main__":
    print("%6s" % "four")       #right justify
    print("%-6s" % "four")      #left justify

    print("-------------------------------------------")
    for exponent in range(7, 11):
        print("%-3d%12d" % (exponent, 10 ** exponent))

    print("-----------------------------------------")
    #%<fieldwidth>.<precision>f
    salary = 100.0
    print("Your salary is $" + str(salary))
    print("Your salary is $%0.2f" % salary)