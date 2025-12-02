#Ich probier erstmal die Disk in einer normalen Python-Liste festzuhalten. 
#Wenn das Rechnen damit zu lange dauert, sollte ich wahrscheinlich ein numpy-Array verwenden

class Disk:

    def __init__(self):
        #Input verarbeiten
        input = open("Day 9/input.txt")
        compactFormat = input.read()
        input.close()

        #Format entpacken
        self.disk = self.compactToDisk(compactFormat)

        #Position des ersten unbesetzten Blocks und des letzten besetzten Block initialisieren
        for pos in range(0,len(self.disk)):
            if self.disk[pos] == ".":
                self.firstFreePos = pos
                break
        self.lastUsedPos = len(self.disk) -1
        
    
    def compactToDisk(self,compactFormat):
        disk = []
        currentID = 0
        for pos in range(0,len(compactFormat)-1,2):
            numberOfUsedBlocks = int(compactFormat[pos])
            numberOfFreeBlocks = int(compactFormat[pos+1])
            for temp in range(0,numberOfUsedBlocks):
                disk.append(currentID)
            currentID += 1
            for temp in range(0,numberOfFreeBlocks):
                disk.append(".")
        numberOfUsedBlocks = int(compactFormat[-1])
        for temp in range(0,numberOfUsedBlocks):
            disk.append(currentID)
        return disk


    def printDisk(self):
       for char in self.disk:
        print(char, end = "")

    def oneCompactStep(self):
        self.disk[self.firstFreePos] = self.disk[self.lastUsedPos]
        self.disk[self.lastUsedPos] = "."
        self.updateUsedAndFreePos()

    def updateUsedAndFreePos(self):
        for pos in range(self.firstFreePos,len(self.disk)):
            if self.disk[pos] == ".":
                self.firstFreePos = pos
                break
        
        for pos in range(self.lastUsedPos,0,-1):
            if self.disk[pos] != ".":
                self.lastUsedPos = pos
                break
    
    def compactDisk(self):
        while self.firstFreePos <= self.lastUsedPos:
            print(self.firstFreePos)
            print(self.lastUsedPos)
            self.oneCompactStep()
    
    def computeChecksum(self):
        res = 0
        for pos in range(0,len(self.disk)):
            if self.disk[pos] == ".":
                break
            res += pos*self.disk[pos]
        print(f"Checksum: {res}")

MyDisk = Disk()
MyDisk.compactDisk()
MyDisk.computeChecksum()