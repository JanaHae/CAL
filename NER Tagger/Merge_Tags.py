'''
    author: Jana Hänßler
'''
#import codecs
#import unicodedata

def readFiles(filename):
    with open(filename, 'r', encoding='utf-16') as f:#files are in UCS-2 which is UTF-16
        lines = f.readlines()
    print('STATUS: Read file {}'.format(filename))
    return lines

def writeFile(doc, name):
    #with open(name, 'w') as f:
        #f.write(codecs.BOM_UTF16_LE)
        #docEnc = doc.encode('utf-16-le')
        #f.write(str(docEnc))
    text_file = open(name, "w")
    text_file.write(doc)
    text_file.close()
    print('STATUS: saved file {}'.format(name))

DocLoc='output_LOC.txt'
DocPERS='output_PERS.txt'
DocTIT='output_TIT.txt'

linesLoc = readFiles(DocLoc)
linesPers = readFiles(DocPERS)
linesTit = readFiles(DocTIT)

print(linesLoc[30])

i = 0 # counter
docOutput = '' # output with all tags

if '\n' in linesLoc[0]:
    print("Found t")

if len(linesLoc)==len(linesPers) and len(linesLoc)==len(linesTit):
    for i in range(0, len(linesLoc) - 1):  # zero-based index
        if '\t' in linesLoc[i]:
            # Find first Tab
            firstTab = linesLoc[i].find('\t')
            # print('line: {}, TabIndex: {}'.format(i, firstTab))
            # print(linesLoc[i])

            # Save the key / word / token
            key = linesLoc[i][:firstTab]
            # print('Key: {}, Laenge: {}'.format(key, len(key)))

            # Find last Tabs for each document
            lastTabLoc = linesLoc[i].rfind('\t')
            lastTabPers = linesPers[i].rfind('\t')
            lastTabTit = linesTit[i].rfind('\t')
            # print('LastTab at index: {}'.format(lastTabLoc))

            # get the labels
            labelLoc = linesLoc[i][lastTabLoc+1:len(linesLoc[i])-1]  #-1 at the end cause of the \n
            labelPers = linesPers[i][lastTabPers+1:len(linesPers[i])-1]
            labelTit = linesTit[i][lastTabTit + 1:len(linesTit[i]) - 1]

            docOutput = docOutput + key + '\t' + labelLoc + '\t' + labelPers + '\t' + labelTit + '\n'

    if '\u2580' in docOutput:
        docOutput = docOutput.replace("\u2580", "ß")
    if '\u2584' in docOutput:
        docOutput = docOutput.replace("\u2584", "Ü")
    if '\u2500' in docOutput:
        docOutput = docOutput.replace("\u2500", "Ä")
    if '\u00B3' in docOutput:
        docOutput = docOutput.replace("\u00B3", "ü")

    print('---------------\n')
    print(docOutput)
    print('---------------')
    writeFile(docOutput, 'output_Merged.txt')
else:
    print('Failed to merge: documents of different length detected.')




'''
for i in range(0, len(linesLoc)-1): #zero-based index
    #print(len(lines[i]))
    if '\t' in lines[i]:
        # Find first Tab
        firstTab = lines[i].find('\t')
        #print('FirstTab at index: {}'.format(firstTab))

        # Save the key / word / token
        key = lines[i][:firstTab]
        #print('Key: {}, Laenge: {}'.format(key, len(key)))

        # Find last Tab
        lastTab = lines[i].rfind('\t')
        #print('LastTab at index: {}'.format(lastTab))

        # Save Value1 / v1 / first Label
        value1 = lines[i][firstTab+1:lastTab]
        #print('value 1: {}, Laenge: {}'.format(value1, len(value1)))

        # Save Value2 / v2 / second Label
        value2 = lines[i][lastTab+1:len(lines[i])-1]  #-1 am Ende wegen des Umbruchchars \n
        #print('value 2: {}, Laenge: {}'.format(value2, len(value2)))
        secondLabel = ''

        if 'PERS' in value1:
            docPERS = docPERS + key + '\t' + value1 + '\n'
        elif 'PERS' in value2:
            docPERS = docPERS + key + '\t' + value2 + '\n'
        else:
            docPERS = docPERS + key + '\t' + 'O' + '\n'

        if 'LOC' in value1:
            docLOC = docLOC + key + '\t' + value1 + '\n'
        elif 'LOC' in value2:
            docLOC = docLOC + key + '\t' + value2 + '\n'
        else:
            docLOC = docLOC + key + '\t' + 'O' + '\n'

        if 'TIT' in value1:
            docTIT = docTIT + key + '\t' + value1 + '\n'
        elif 'TIT' in value2:
            docTIT = docTIT + key + '\t' + value2 + '\n'
        else:
            docTIT = docTIT + key + '\t' + 'O' + '\n'


def writeFile(doc, name):
    text_file = open(name, "w")
    text_file.write(doc)
    text_file.close()
    print('STATUS: saved file {}'.format(name))

writeFile(docPERS, 'TrainDocPERS.txt')
writeFile(docLOC, 'TrainDocLOC.txt')
writeFile(docTIT, 'TrainDocTIT.txt')

#print('---------------\n')
#print(docPERS)
#print('---------------')
#print(len(docPERS))

'''

