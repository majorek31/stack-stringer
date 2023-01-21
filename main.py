import sys
print("Stack-Stringer - string generator, that pushes WHOLE strings onto stack made by majorek31 v0.1\n")
if len(sys.argv) >= 2:
    string = " ".join(sys.argv[1:])
    reversed_string = string[::-1]
    bytes = bytes(reversed_string, 'ascii')
    f = open("output.txt", "w")
    arrays = []
    endLength = len(bytes)
    skip = 0
    f.write("xor edx, edx\npush edx\n")
    for i in range(0, len(bytes), 4):
        arrays.append(bytes[i:i+4])
    for i in arrays:
        printable = ""
        for j in range(4):
            try:
                printable += f'{int(i[j]):x}'
            except:
                for k in range(j):
                    if k % 2 == 0:
                        skip += 1                
                if len(printable) < 8:
                    for l in range(8 - len(printable)):
                        printable += "0"
        f.write("push 0x" + printable + "\n")
    f.write("mov esi, esp\n")
    endLength += 4
    if skip != 0:
        skip -= 1
        endLength += skip
        f.write("add esi, " + str(hex(skip)) + "\n")
    print("String length (it has to be added to esp): " + str(hex(endLength)))
    print("Created file: output.txt")
    f.close()
else:
    print("Please enter your string!")