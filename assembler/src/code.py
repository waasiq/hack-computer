
def readASM(address): 
    # Read the file
    with open(address, 'r') as file:
        lines = file.readlines()
        file.close()
    return lines

def removeWhiteSpace(lines):
    # Remove all whitespace from the lines
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
    return lines

def removeComments(lines):
    # Remove all comments from the lines
    for i in range(len(lines)):
        if "//" in lines[i]:
            lines[i] = lines[i].split("//")[0]
            lines[i] = lines[i].strip() # removing whitespace if any
    return lines

def removeEmptyLines(lines):
    # Remove all empty lines from the lines
    parsedLines = []
    for i in range(len(lines)):
        if lines[i] != "":
            parsedLines.append(lines[i])
    return parsedLines

