__author__ = 'admin'
import pickle

if __name__ == "__main__":
    lyst = [60, "A String object", 1977]
    fileObj = open("items.dat", "wb")
    for item in lyst:
        pickle.dump(item, fileObj)
    fileObj.close()

