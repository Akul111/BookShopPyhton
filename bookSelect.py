import matplotlib.pyplot as pl
import numpy as np
def creatingGraph():

    uniqueNumber = []
    bookIDAppearances = []

    openLogFile = open("logfile.txt", "r")

    for records in openLogFile:
        recordsList = records.split("-")

        bookIDAppearances.append(int(recordsList[0]))



        for i in range(1, len(bookIDAppearances)):
            if i not in bookIDAppearances:
                uniqueNumber.append(recordsList[0])
    sortedList = sorted(bookIDAppearances)


    pl.hist(uniqueNumber, sortedList)
    pl.show()

