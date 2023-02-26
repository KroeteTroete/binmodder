#Written by Liam/KroeteTroete for development of the GOF2 Google Translate Mod
import struct
from random_googletrans.gof2translate import gof2translate

#successfulReplacements = 0
#failedReplacements = 0

def breakStrings(binStrings):
    
    translatedStrings = gof2translate.breaktranslation(binStrings)
    return translatedStrings

def separateStrings(binStrings, splitter = '\n'):
    namesArray = binStrings.split(splitter)
    return namesArray

def replaceBinStrings(binFile, binStringsArray, stringReplacements, returnReplacements = False, fileEncoding="utf-8"):
    """
    Replace a List of Strings

    :param str binFile: name or path of the .bin file, including file suffix (for example: names_bobolan_0.bin)
    :param str binStringsArray: Array of strings which are to be replaced
    :param str stringReplacements: Replacement strings which are to be placed into the .bin
    :param bool returnReplacements: Whether or not the replacementArray should be returned (useful if breakStrings() was used in the process. Defaults to FALSE)
    """

    for i in binStringsArray:
        
        with open(binFile, 'rb') as f:
            
            file_contents = f.read()
            #find position of the name in byte array
            index = file_contents.find(bytes(i, 'utf-8'))

            #if found
            if index != -1:
                chosenReplacement = stringReplacements[binStringsArray.index(i)]
                new_data = file_contents.replace(bytes(i, 'utf-8'), bytes(chosenReplacement, 'utf-8'))
                print(f"replaced {i} with {chosenReplacement}")
                with open(binFile, 'wb') as f:
                    f.seek(0)
                    f.write(new_data)
                    #successfulReplacements += 1
                    #index2 = file_contents.find(bytes(chosenReplacement, 'utf-8'))
            else:
                print(f"""
                {i} not found in {binFile}
                """)
                #failedReplacements += 1
    
    f.close()
    if returnReplacements:
        return stringReplacements
    

def placeStringLength(binFile, stringReplacements):
    """
    Place the string length into the byte preceding the string

    :param str binFile: name or path of the .bin file, including file suffix (for example: names_bobolan_0.bin)
    :param str stringReplacements: strings which length bytes need to be changed
    """
    with open(binFile, 'rb+') as f:
        file_contents = f.read()

        for i in stringReplacements:
        
            index = file_contents.find(bytes(i, 'utf-8'))
            
            if index != -1:
                # Extract the byte preceding the string
                #preceding_byte = file_contents[index - 1]
                
                #string_length = chr(len(i)).encode('utf-8')
                string_length = struct.pack('>H', len(i))

                # Place string_length in front of the name (:index-1)
                file_contents = file_contents[:index-2] + string_length + file_contents[index:]
                
                f.seek(0)
                
                f.write(file_contents)

        #print(f"{successfulReplacements} successful replacements and {failedReplacements} failed replacements")

