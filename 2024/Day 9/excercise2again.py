# Wenn die Listen aus freien/besetzten Längen von Blöcken immer korrekt sind, können sich fehler einschleichen.
# Ich versuche eine Version zu implementieren, welche nur direkt auf der Disk arbeitet
# Lösung rennt sehr lange, ist aber richtig! Hauptsache durch :D

class Disk:

    def __init__(self):
        #Input verarbeiten
        input = open("Day 9/input.txt")
        self.compactFormat = input.read()
        input.close()

        #Format entpacken
        self.disk = self.compactToDisk(self.compactFormat)

    def printDisk(self):
        for char in self.disk:
            print(char, end = "")
        print("")

    def compactToDisk(self,compactFormat):
        disk = []
        currentID = 0

        #Besetzen der Blöcke auf der Disk
        for pos in range(0,len(compactFormat)-1,2):
            numberOfUsedBlocks = int(compactFormat[pos])
            numberOfFreeBlocks = int(compactFormat[pos+1])
            
            #Hinzufügen der besetzten Blöcke auf die Disk
            for temp in range(0,numberOfUsedBlocks):
                disk.append(currentID)
            currentID += 1

            #Hinzufügen der freien Blöcke auf die Disk
            for temp in range(0,numberOfFreeBlocks):
                disk.append(".")
            
        
        #Der letze besetzte Block muss händisch besetzt werden, da nach ihm keine freien Blöcke folgen
        numberOfUsedBlocks = int(compactFormat[-1])
        for temp in range(0,numberOfUsedBlocks):
            disk.append(currentID)

        self.maxID = currentID

        return disk
    
    def moveFileByIDifPossible(self,ID):
        # Findet Start und Ende des zusammenhängenden files mit der spezifischen ID. Dabei ist das Ende die letzte Position,
        # die noch einen Block mit der ID enthält

        for pos in range(0,len(self.disk)):
            if self.disk[pos] == ID:
                fileStartPosition = pos
                break
        
        for pos in range(fileStartPosition,len(self.disk)):
            if self.disk[pos] != ID:
                fileEndPosition = pos - 1
                break

            if pos == len(self.disk)-1:
                fileEndPosition = pos
        
        lengthFile = fileEndPosition - fileStartPosition + 1

        freeSpaceStartPosition = self.findFirstFreeSpaceWithSpecificLength(lengthFile)

        if freeSpaceStartPosition == - 1 or freeSpaceStartPosition >= fileStartPosition:
            return
        
        #Move file to free space
        for i in range(0,lengthFile):
            self.disk[freeSpaceStartPosition + i] = self.disk[fileStartPosition+i]
            self.disk[fileStartPosition + i] = "."

        return

    def findFirstFreeSpaceWithSpecificLength(self, n):
        
        freeSpaceLength = -1

        for pos in range(0,len(self.disk)):

            if freeSpaceLength == n:
                return freeSpaceStartPosition

            if self.disk[pos] == "." and freeSpaceLength > 0:
                freeSpaceLength += 1
            
            if self.disk[pos] == "." and freeSpaceLength == -1:
                freeSpaceStartPosition = pos
                freeSpaceLength = 1

            if self.disk[pos] != ".":
                freeSpaceLength = -1
        
        return -1

    def compactDisk(self):
        for ID in range(self.maxID,0,-1):
            #self.printDisk()
            print(f"Moving ID {ID} from {self.maxID}")
            self.moveFileByIDifPossible(ID)

    def computeChecksum(self):
        res = 0
        for pos in range(0,len(self.disk)):
            if self.disk[pos] == ".":
                continue
            res += pos*self.disk[pos]
        print(f"Checksum: {res}")

MyDisk = Disk()
MyDisk.compactDisk()
MyDisk.computeChecksum()