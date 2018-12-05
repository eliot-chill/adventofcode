import re
filename = "day3_input.txt"

with open(filename) as f:
    fileContent = f.readlines()

def parseInput(claim):
    #define regex's for the three components
    idPattern = re.compile(r'#[0-9]{1,9999}')
    distancePattern = re.compile(r'([0-9]{1,4},[0-9]{1,4})')
    areaPattern = re.compile(r"[0-9]{1,2}x[0-9]{1,2}")
    #find matches based on expressions
    idResult = re.findall(idPattern, claim)
    idNumber = idResult[0].replace("#","")

    distanceResult = re.findall(distancePattern, claim)
    distanceValues = list(map(int, distanceResult[0].split(",")))

    areaResult = re.findall(areaPattern, claim)
    areaValues = list(map(int, areaResult[0].split("x")))

    #print for debugging
    # print(idNumber)
    # print(distanceValues)
    # print(areaValues)

    return idNumber, distanceValues, areaValues
fabric = [list("."*1000) for i in range(1000)]

for claim in fileContent:
    
    idNumber, distanceValues, areaValues = parseInput(claim)
    for i in range(distanceValues[1], areaValues[1]+distanceValues[1]):
        for j in range(distanceValues[0], areaValues[0]+distanceValues[0]):
            if fabric[i][j] == ".":
                fabric[i][j] = "#"
            else:
                fabric[i][j] = "X"
    
for claim in fileContent:
    currentClaim = "" 
    idNumber, distanceValues, areaValues = parseInput(claim)
    for i in range(distanceValues[1], areaValues[1]+distanceValues[1]):
        for j in range(distanceValues[0], areaValues[0]+distanceValues[0]):
            currentClaim += fabric[i][j]
    
    if "X" not in currentClaim:
        print(idNumber)

            # if fabric[i][j] == "X":
            #     overlapped = True
            #     break
    # if overlapped == False:
    #     print(idNumber)

counter = 0
for row in fabric:
    for item in row:
        if item == "X":
            counter +=1
print(counter)
        

