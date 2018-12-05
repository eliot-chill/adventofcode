inputFile = "day2_input.txt"

with open(inputFile) as f:
    fileContent = f.readlines()

twoLetters = 0
threeLetters = 0

for content in fileContent:
    word = list((content.count(letter)) for letter in set(content))
    if 2 in word:
        twoLetters+=1
    if 3 in word:
        threeLetters+=1

print(twoLetters)
print(threeLetters)
print(twoLetters*threeLetters)
    # for key in word:
    #     print(word[key])


