__author__ = 'rsukla'

import time
from datetime import datetime
from time import mktime

bigDataFile = open('AMAT.txt', 'r')

readFile = bigDataFile.read()

lineSplit = readFile.split('\n')

for everyLine in lineSplit:
    dividedLine = everyLine.split(',')

    stockName = dividedLine[0].split('.')[1]
    initialDate = dividedLine[2] + dividedLine[3]

    unixStamp = mktime(datetime.strptime(initialDate, '%Y%m%d%H%M%S').timetuple())
    try:
        dateStamp = time.strftime('%m/%d/%Y  %H:%M:%S', time.localtime(unixStamp))
    except:
        pass

    stockPrice = dividedLine[4]

    reformatted = unixStamp, dateStamp, stockName, stockPrice
    saveFormat = str(reformatted).replace('\'','').replace('(', '').replace(')','')

    print reformatted
    print saveFormat

    appendFile = open('example.txt', 'a')
    appendFile.write(saveFormat)
    appendFile.write('\n')
    appendFile.close()

    time.sleep(5)





