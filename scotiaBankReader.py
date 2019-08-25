import PyPDF2
import time
import calendar
import datetime
import logging


logging.basicConfig(level=logging.DEBUG)

#parse the things after the refernce number
def cutUselessStuff(document):

    startOfUseless = "If you have any questions"


    interestedInfo = document.split(startOfUseless)[0]


    return interestedInfo
#determine which refernece number we are in
def nextPurchaseItem(aNumber):
    moveToNextNum = False
    if(int(aNumber)== nextPurchaseItem.counter ):
        moveToNextNum = True
        nextPurchaseItem.counter += 1
    logging.debug ("Counter is %d" % (nextPurchaseItem.counter -1))
    return moveToNextNum

nextPurchaseItem.counter = 1

#check if it is a isReferenceNumber
def isReferenceNumber(string):
    if(len(string)==3):
        if(string.isdigit()):
            return nextPurchaseItem(int(string))
    return False


#Collect the name of the info
def collectInfo(index,lines):

    index+=1
    string = ""
    while (not isReferenceNumber(lines[index])):
        newWordToEnter = lines[index]
        nextWordTobeEnterAfter= lines[index+1]
        logging.debug("The current string: %s and the newWord %s and the nextWord after that is %s"  % (string,newWordToEnter, nextWordTobeEnterAfter))

        if not isReferenceNumber(nextWordTobeEnterAfter):
            string +=  lines[index]
            index+=1
            string = string + " "
            time.sleep(2)
        else:
            price= lines[index]
            logging.debug("this is the price of the item %s" % price)
    logging.debug("This is your string %s" % string)
    return index


def parseStatement(counter,lines):
    index= counter
    index+=1
    nextWord= lines[index]
    if nextWord=="Period":
        index+=1

        #parse The Month
        startMonth = lines[index]
        startMonth = list(calendar.month_abbr).index(startMonth)
        index+=1

        #parse the Day
        stripElement = lines[index].split(",")
        startDay=stripElement[0]
        index+=1

        #parse Year
        startYear = lines[index]


        startDate = datetime.datetime(int(startYear), int(startMonth), int(startDay))
        index+=2


        #parse the month
        endMonth = lines[index]
        endMonth = list(calendar.month_abbr).index(endMonth)
        index+=1

        #parse the Day
        stripElement = lines[index].split(",")
        endDay= stripElement[0]
        index+=1

        #parse the Year
        endYear = lines[index]


        endDate = datetime.datetime(int(endYear), int(endMonth), int(endDay))

def parsePDF():
    creditCard = True
    pdfFileObj = open('January 2019 e-Statement.pdf', 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)


    pageObj = pdfReader.getPage(0)
    info = pageObj.extractText()

    info = cutUselessStuff(info)

    lines=info.split()

    counter =0
    for line in lines:


        # TODO: get the line of each thing

        if isReferenceNumber(line):
            logging.debug(line)
            time.sleep(1)

            index = counter+ 1

            transMonth = lines[index]
            index+=1

            transDay = lines[index]
            index+=1

            postMonth = lines[index]
            index+=1

            postDay = lines[index]


            logging.debug("This is the TransMonth: %s , transDay:%s , postMonth:%s, postDay:%s "% (transMonth, transDay, postMonth , postDay))

            collectInfo(index,lines)
        if line == "Statement":
            parseStatement(counter,lines)



        counter+=1
def main():

    parsePDF()

if __name__ == "__main__":
    main()
