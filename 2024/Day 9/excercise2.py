#wenn man jetzt wieder nur ganze Blöcke verschiebt, könnte es sich lohnen auf dem kompakten Format zu arbeiten.
#Ein Problem dabei ist aber, dass das kompakte Format nicht die IDs enthält. Damit reichen die in ihm gespeicherten Daten nicht aus
#Mein erster Ansatz ist, die freien Blöcke mit Beginn und Länge in einer Liste zu speichern.

class Disk:

    def __init__(self):
        #Input verarbeiten
        input = open("Day 9/testInput.txt")
        self.compactFormat = input.read()
        input.close()

        #Hilfliste für die Fragmentierung. Die Elemente sind auch Listen, wobei das erste Element der Liste die Startposition und das zweite die Länge angibt
        self.listOfFreeBlocks = []
        self.listOfUsedBlocks = []

        #Format entpacken
        self.disk = self.compactToDisk(self.compactFormat)

        self.printInit()
    
    def printInit(self):
        print(f"{len(self.compactFormat)} input numbers converted into {len(self.listOfUsedBlocks)} used blocks and {len(self.listOfFreeBlocks)} free blocks")
    
    def compactToDisk(self,compactFormat):
        disk = []
        currentID = 0

        #Besetzen der Blöcke auf der Disk
        for pos in range(0,len(compactFormat)-1,2):
            numberOfUsedBlocks = int(compactFormat[pos])
            numberOfFreeBlocks = int(compactFormat[pos+1])
            
            #Merken des Starts und der Länge des besetzten Blocks
            self.listOfUsedBlocks.append([len(disk),numberOfUsedBlocks])
            
            #Hinzufügen des Blocks auf die Disk
            for temp in range(0,numberOfUsedBlocks):
                disk.append(currentID)
            currentID += 1

            #Merken des freien Blocks der gleich hinzugefügt wird. 
            #Die Anfangposition des Blocks stimmt in diesem Moment mit der Länge der Disk überein
            if numberOfFreeBlocks > 0:
                self.listOfFreeBlocks.append([len(disk),numberOfFreeBlocks])

            #Hinzufügen des Blocks auf die Disk
            for temp in range(0,numberOfFreeBlocks):
                disk.append(".")
            
        
        #Der letze besetzte Block muss händisch besetzt werden, da nach ihm keine freien Blöcke folgen
        numberOfUsedBlocks = int(compactFormat[-1])
        self.listOfUsedBlocks.append([len(disk),numberOfUsedBlocks])
        for temp in range(0,numberOfUsedBlocks):
            disk.append(currentID)

        return disk

    def printDisk(self):
        for char in self.disk:
            print(char, end = "")
        print("")

    def moveLastBlockIfPossible(self):
        data = self.listOfUsedBlocks.pop()
        blockStart = data[0]
        blockLength = data[1]
        freeBlock = None

        #Finden eines passenden Blocks, extrahieren der Daten und Updaten der freien Block Liste
        for i in range(0, len(self.listOfFreeBlocks)):
            block = self.listOfFreeBlocks[i]
            if block[1] >= blockLength:
                freeBlock = block
                freeBlockStart = freeBlock[0]
                freeBlockLength = freeBlock[1]
                if freeBlockLength == blockLength:
                    self.listOfFreeBlocks.remove(block)
                else:
                    self.listOfFreeBlocks[i] = [freeBlockStart+blockLength,freeBlockLength-blockLength]
                break
        if freeBlock == None:
            return
        self.swapBlocks(blockStart, blockLength, freeBlockStart, freeBlockLength)

    def swapBlocks(self, usedBlockStart, usedBlockLength, freeBlockStart, freeBlockLength):
        #Überprüfen ob die Längen passen
        if usedBlockLength > freeBlockLength:
            raise ValueError(f"usedBlockLength {usedBlockLength} is shorther than freeBlockLength {freeBlockLength}")

        #Auf Disk schreiben
        for i in range(0,usedBlockLength):
            self.disk[freeBlockStart + i] = self.disk[usedBlockStart+i]
            self.disk[usedBlockStart + i] = "."
    
    def compactDisk(self):
        numberOfBlocks = len(self.listOfUsedBlocks)
        counter = 1
        while len(self.listOfUsedBlocks) > 0:
            #self.printDisk()
            #print(f"Moving block {counter} from {numberOfBlocks}")
            self.moveLastBlockIfPossible()
            counter += 1
    
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

#Checksum too high atm :( Im Beispiel aber richtig :( Vielleicht gibt es im richtigen Input irgendwelche Edge-Cases, die  mein Code nicht richtig behandelt?