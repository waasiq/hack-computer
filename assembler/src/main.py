from code import readASM, removeWhiteSpace, removeComments, removeEmptyLines
from Parser import parseInstructions

##? Types of commands in the Hack assembly language
##* A command: @value
##* C command: dest=comp;jump
##* L command: (symbol)

if __name__ == '__main__':
    path = '../files/pong/Pong'
    readPath = path + '.asm'
    writePath  = path + '.hack'
    fileContent = readASM(readPath)
    whiteLessContent = removeWhiteSpace(fileContent)
    commentLessContent = removeComments(whiteLessContent)
    parsedContent = removeEmptyLines(commentLessContent)
    finalOutput = parseInstructions(parsedContent)

    with open(writePath, 'w') as f:
        for line in finalOutput:
            f.write(line + '\n')
