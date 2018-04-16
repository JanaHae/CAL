'''
    author: Jana Hänßler
'''

filename='train.txt'
with open(filename) as f:
    lines = f.readlines()
print('STATUS: Read file {}'.format(filename))

i = 0 #counter
docPERS = '' #output 1, only PERS
docTIT = '' #output 1, only TIT
docLOC = '' #output 1, only LOC

for i in range(0, len(lines)-1): #zero-based index
    if '\t' in lines[i]:
        # Find first Tab
        firstTab = lines[i].find('\t')

        # Save the key / word / token
        key = lines[i][:firstTab]

        # Find last Tab
        lastTab = lines[i].rfind('\t')

        # Save Value1 / v1 / first Label
        value1 = lines[i][firstTab+1:lastTab]

        # Save Value2 / v2 / second Label
        value2 = lines[i][lastTab+1:len(lines[i])-1]  #-1 at the end because of char \n at the end
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



