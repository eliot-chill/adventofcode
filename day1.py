inputFile = "day1_input.txt"

with open(inputFile) as f:
    fileContent = f.readlines()

freq = 0
for change in fileContent:
    freq += int(change)

print(freq)