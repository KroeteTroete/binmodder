#Written by Liam/KroeteTroete
import gof2translate

binFile = 'stations.bin'

names = """"""



#replacements = """"""

replacements = gof2translate.breaktranslation(names)

namesArray = names.split('\n')
replacementsArray = replacements.split('\n')

#for i in replacementsArray:
#    print(i)

successfulReplacements = 0
failedReplacements = 0

for i in namesArray:
    # Open the file in binary mode
    with open(binFile, 'rb') as f:
        # Read the entire contents of the file into a bytes object
        file_contents = f.read()
        #find position of the string in byte array
        index = file_contents.find(bytes(i, 'utf-8'))

        if index != -1:
            chosenReplacement = replacementsArray[namesArray.index(i)]
            new_data = file_contents.replace(bytes(i, 'utf-8'), bytes(chosenReplacement, 'utf-8'))
            print(f"replaced {i} with {chosenReplacement}")
            with open(binFile, 'wb') as f:
                f.seek(0)
                f.write(new_data)
                successfulReplacements += 1
                index2 = file_contents.find(bytes(chosenReplacement, 'utf-8'))
        else:
            print(f"""
            {i} not found in {binFile}
            """)
            failedReplacements += 1



f.close()

# Open the file in binary mode
with open(binFile, 'rb+') as f:
    # Read the entire contents of the file into a bytes object
    file_contents = f.read()

    for i in replacementsArray:
    
        # Search for the specific string within the bytes object
        index = file_contents.find(bytes(i, 'utf-8'))
        
        # If the string was found, replace the byte preceding it with the string length
        if index != -1:
            # Extract the byte preceding the string
            preceding_byte = file_contents[index - 1]
            
            # Convert the string length to a single-byte character
            string_length = chr(len(i)).encode('utf-8')
            
            # Replace the original byte with the new character
            file_contents = file_contents[:index-1] + string_length + file_contents[index:]
            
            # Move the file pointer to the beginning of the file
            f.seek(0)
            
            # Write the modified bytes object back to the file
            f.write(file_contents)

print(f"{successfulReplacements} successful replacements and {failedReplacements} failed replacements")