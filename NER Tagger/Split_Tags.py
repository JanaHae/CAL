'''
    author: Jana Hänßler
'''

filename='train.txt'
with open(filename) as f:
    lines = f.readlines()
#print("Done reading")
print('STATUS: Read file {}'.format(filename))

i = 0 #counter
docPERS = '' #output 1, only PERS
docTIT = '' #output 1, only TIT
docLOC = '' #output 1, only LOC

#print(type(lines[i])) #string
#print(lines[i]) #Kg.<TAB>B-PERS<TAB>B-TIT

for i in range(0, len(lines)-1): #zero-based index
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


