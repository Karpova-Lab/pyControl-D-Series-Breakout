import pandas as pd
import sys
import xlrd
import fileinput

xlsFile = '../../manufacturing/BOM.xlsx'

def makeChoice(choiceQuestion,choiceList):
    first  = True
    chosen = 0
    while chosen<1 or chosen>len(choiceList): 
        if first:
            print()
            print(choiceQuestion)
            for i,choice in enumerate(choiceList):
                print('{}: {}'.format(i+1,choice))
            # print("\nChoose a Table to Generate\n1: Cerebro\n2: Implant\n3: Base Station\n")
            print()
            typed = input("Choice = ")
            first = False
        else:
            print("\n\"{}\" is not an option. Try again ya dufus.".format(typed))
            for i,choice in enumerate(choiceList):
                print('{}: {}'.format(i+1,choice))
            print()
            typed = input("Choice = ")  
        try:
            chosen = int(typed)
        except:
            chosen = 0
    return choiceList[chosen-1]

def getColWidths(table):
    colMax = []
    for cols in table:
        lengths = []
        for entry in table[cols]:
            lengths.append(len(entry))
        colMax.append(max(lengths) if max(lengths)>len(cols) else len(cols) )
    return colMax

def printDivider(colWidths,emptyVec=[],doubleDash = False):
    dash = "=" if doubleDash else "-"
    index = 0
    dividerString = ""
    for width in colWidths:
        insert = dash
        if emptyVec:
            if emptyVec[index]:
                insert = " "
        dividerString += "{0}{1}".format("+",(width+2)*insert)
        index += 1
    dividerString += "+\n"
    return dividerString

def printContents(table,colWidths,isHeader=False,**kwds):
    mergeRows = False
    contentString  = "| "
    index = 0
    blankCols = []
    for cols in table:
        content =  cols if isHeader else table.loc[row,cols]
        if content=="nan":
            blankCols.append(mergeRows)
            content = ""
        else:
            blankCols.append(False)
        fill = colWidths[index]-len(content)
        contentString += "{0}{1}{2}".format(content,(fill)*" "," | ")
        index +=1
    contentString += "\n"
    return contentString,blankCols

##########################################
#           Script Start
##########################################

# convert xls BOM to rst table

book = xlrd.open_workbook(xlsFile)
sheetNames = book.sheet_names()
notDataNames = []
for sheet in sheetNames:
    if sheet.find('_data') < 0:
        notDataNames.append(sheet)

chosenSheet = makeChoice("Choose a Table to Generate",notDataNames)
table = pd.read_excel(xlsFile,usecols=[0,1,2,3,],sheet_name=chosenSheet,dtype='str')#read in table from excel file
table.fillna("",inplace=True)
widths = getColWidths(table) # get the maximum content width of each column

#print header
outputString = printDivider(widths) #first divider
outputString += printContents(table,widths,isHeader=True)[0] #header
outputString += printDivider(widths,doubleDash=True) #header divider

#print table contents
for row in range(len(table)):
    valString,blanks = printContents(table,widths)
    outputString += printDivider(widths,blanks)*(row != 0) + valString
outputString += printDivider(widths) #final divider


# Figure out where to place BOM
rstFiles = ['build.rst']
relative_path_to_BOM = makeChoice('Where to place BOM?',rstFiles)


# place rst BOM into file
insert_here_flag = False
waiting_for_endFlag = False
for line in (fileinput.input(relative_path_to_BOM,inplace=1)):
    if waiting_for_endFlag:
        if line.find('.. BOM end')>-1:
            sys.stdout.write(line.replace(line, '\n\n'+line))
            waiting_for_endFlag = False
        else:
            sys.stdout.write(line.replace(line, ''))

    elif insert_here_flag:
        sys.stdout.write(line.replace(line, '\n'+ outputString ))
        insert_here_flag = False
        waiting_for_endFlag = True
    else:
        sys.stdout.write(line.replace(line, line))
        if line.find('.. BOM start')>-1:
            insert_here_flag = True

print("\n\"{}\" sheet inserted into \"{}\"!\n".format(chosenSheet,relative_path_to_BOM))
