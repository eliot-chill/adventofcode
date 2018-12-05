inputFile = "day4_input.txt"

with open(inputFile) as f:
    fileContent = f.readlines()

# Sort by time
class Record:

    def __init__(self, record):
        self.record = record
        self.date = self.getDate()
        self.time = self.getTime()
        self.status = self.getStatus()
    
    def __str__(self):
        return self.record


    def getDate(self):
        return self.record[1:11]

    def getMonth(self):
        return self.date[5:7]
    def getDay(self):
        return self.date[8:10]
    def getTime(self):
        return self.record[12:17]
    def getStatus(self):
        return self.record[19:]

records = []

for record in fileContent:
    records.append(Record(record))

records.sort(key=lambda record: (record.date, record.time))
for record in records:
    print(record.date, record.time, record.status)



