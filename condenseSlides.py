import PyPDF2
import re
import sys

if len(sys.argv) != 2:
    print "Not enough args"
    sys.exit()

pdfName = sys.argv[1] 
pdfNameAndEnding = pdfName.split('.')
pdfFileEnding = pdfNameAndEnding[-1]

if pdfFileEnding != 'pdf':
    print "No pdf file endings\do not recognise file"
    sys.exit()

pdfFileObj = open(pdfName, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

def removeLastNLinesOfString(string, numberToRemove):
    string = string.split('\n')
    listOfLines = string[:-numberToRemove]
    return '\n'.join(listOfLines)

def compressPdf(pdfReader):
    pdfReader.decrypt('rosebud')
    pdfWriter = PyPDF2.PdfFileWriter()
    textOfPreviousPage = ""
    previousPage = None
    for pageNum in range(pdfReader.numPages):
        page = pdfReader.getPage(pageNum)
        text = page.extractText()

        # last two lines are pageNum/total pages and blank line so remove them so we can compare
        # if the texts are the same
        textWithLinesRemoved = removeLastNLinesOfString(text, 2)
        if (textOfPreviousPage != "" and textOfPreviousPage != textWithLinesRemoved):
            pdfWriter.addPage(previousPage)  
        
        textOfPreviousPage = textWithLinesRemoved
        previousPage = page

    # add last page
    if previousPage:
        pdfWriter.addPage(previousPage)
    
    return pdfWriter 
        
pdfWriter = compressPdf(pdfReader)
outputFileName = pdfNameAndEnding[0] + "Condensed.pdf"
pdfOutputFile = open(outputFileName, 'wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()
pdfFileObj.close()
