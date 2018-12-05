inputFile = "day1_input.txt"

with open(inputFile) as f:
    fileContent = f.readlines()
fileContent = list(map(int, fileContent))

freq = 0
freqs = [0]
found = False
while found == False:
    for update in fileContent:
        freq += update
        if freq in freqs:
            print(freq)
            found = True
            break
        else:
            freqs.append(freq)