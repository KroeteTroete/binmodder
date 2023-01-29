#bindetect.py detects strings inside a .bin file

def detectStrings(binFile, binType, returnType = 'list'):
    """
    detects the strings inside a bin file and places them into an array

    :param str binFile: path to the .bin file
    :param str binType: Type of bin file. Valid binTypes are: 'names', 'stations', 'systems'
    :param str returnType: Determines what type of object should be returned in the end. Valid returntypes are: 'list', 'string'
    """
    names = []
    
    if binType == 'names':
        with open(binFile, 'rb') as f:
            
            #00 00 00 NUM SEP
            f.read(3)
            amount = ord(f.read(1)) #extract amount of bytes
            

            try:
                for i in range(0, amount ):

                    f.read(1)#skip seperator
                    length = ord(f.read(1)) #read length
                    name = f.read(length).decode() #extract name

                    names.append(name)

            except EOFError:
                print("EOF reached!")
            
            
            f.close()

    if returnType == 'list':
        return names
    elif returnType == 'string':
        namesInString = names[0]
        for i in names[1:]:
            namesInString = namesInString + "\n" + i
        
        return namesInString