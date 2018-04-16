'''
    author: Jana Hänßler
'''

def readFiles(filename):
    #read the file
    with open(filename, 'r', encoding='utf-16') as f:#files are in UCS-2 which is UTF-16
        lines = f.readlines()
    print('STATUS: Read file {}'.format(filename))
    return lines

def writeFile(doc, name):
    # save the merged file to the same location
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

if len(linesLoc)==len(linesPers) and len(linesLoc)==len(linesTit):
    for i in range(0, len(linesLoc) - 1):  # zero-based index
        if '\t' in linesLoc[i]:
            # Find first Tab
            firstTab = linesLoc[i].find('\t')

            # Save the key / word / token
            key = linesLoc[i][:firstTab]

            # Find last Tabs for each document
            lastTabLoc = linesLoc[i].rfind('\t')
            lastTabPers = linesPers[i].rfind('\t')
            lastTabTit = linesTit[i].rfind('\t')

            # get the labels
            labelLoc = linesLoc[i][lastTabLoc+1:len(linesLoc[i])-1]  #-1 at the end cause of the \n
            labelPers = linesPers[i][lastTabPers+1:len(linesPers[i])-1]
            labelTit = linesTit[i][lastTabTit + 1:len(linesTit[i]) - 1]

            docOutput = docOutput + key + '\t' + labelLoc + '\t' + labelPers + '\t' + labelTit + '\n'

    #replace some unicode characters that appeared after applying the model
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
