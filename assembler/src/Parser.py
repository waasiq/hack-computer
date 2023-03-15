from SymbolTable import SymbolTable, C_Inst_Table

INSTCounter = 16

def parseInstructions(instructions):
    parseLCommand(instructions)
    finalOutput = []

    for instruction in instructions:
        if instruction[0] == "@":
            finalOutput.append(parseACommand(instruction))   
        else:
            finalOutput.append(parseCCommand(instruction))

    return finalOutput

def parseACommand(instruction):
    strippedInstruction = instruction[1:]
    binaryData = ''
    global INSTCounter

    if (strippedInstruction[0] >= '0' and strippedInstruction[0] <= '9'):
        intData = int(strippedInstruction)
        binaryData = (bin(intData)[2:].zfill(16))
    elif (strippedInstruction[0] == 'R' and strippedInstruction[1] >= '0' and strippedInstruction[1] <= '9'):
        intData = int(strippedInstruction[1:])
        binaryData = (bin(intData)[2:].zfill(16))
    elif (strippedInstruction in SymbolTable): 
        intData = SymbolTable[strippedInstruction]
        binaryData = (bin(intData)[2:].zfill(16))
    else:
        #* Variables are assigned memory addresses starting at 16
        SymbolTable[strippedInstruction] = INSTCounter
        binaryData = (bin(INSTCounter)[2:].zfill(16))
        INSTCounter += 1
        
        
    return binaryData

def parseCCommand(instruction):
    dest = ''
    comp = ''
    jump = ''
    binaryData = '111'

    if '=' in instruction:
        dest = instruction.split('=')[0]
        comp = instruction.split('=')[1]
    elif ';' in instruction:
        comp = instruction.split(';')[0]
        jump = instruction.split(';')[1]
    else:
        comp = instruction
    
    if (comp in C_Inst_Table['comp']['zero']):
        binaryData += '0'
        binaryData += C_Inst_Table['comp']['zero'][comp]
    elif (comp in C_Inst_Table['comp']['one']):
        binaryData += '1'
        binaryData += C_Inst_Table['comp']['one'][comp]

    binaryData += C_Inst_Table['dest'][dest]
    binaryData += C_Inst_Table['jump'][jump]
    return binaryData

def parseLCommand(instructions): 
    # First pass
    for indx, instruction in enumerate(instructions):
        if (instruction[0] == '('):
            strippedInstruction = instruction[1:-1]
            SymbolTable[strippedInstruction] = indx
            del instructions[indx]
    
    # Second pass:  remove L commands
    for indx, instruction in enumerate(instructions):
        if (instruction[0] == '('):
            del instructions[indx]
