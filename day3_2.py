import re
import day3 as d3
filename = "day3_input.txt"

with open(filename) as f:
    fileContent = f.readlines()

for claim in fileContent:
    idNumber, distanceValues, areaValues = d3.parseInput(claim)
    
