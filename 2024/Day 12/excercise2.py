# Attribut perimeter in der Klasse Plot gibt schon die Anzahl der Seiten des Feldes an.
# Idee: Pro Knoten fuer jeden Nachbarn 0.5 vom Perimeter abziehen, dann ist Summe der
#       Perimeter gleich der Anzahl an Seiten? -> Nur Nachbarn an der gleichen "Seite"
#       muessen dafuer gezaehlt werden, dass ist genau das Problem.
# Anzahl an Seiten = Anzahl an Ecken = Perimeter - 1 Falsch!
class plot:

    def __init__(self, char, garden):
        self.neighbours: list[plot] = []
        self.type: chr = char
        self.garden: garden = garden
        self.isInARegion = False
        self.perimeter: int = 0
    
    def setCoords(self,x,y):
        self.x = x
        self.y = y

    def getNeighbours(self):
        for coords in [[-1,0], [1,0], [0,-1], [0,1]]:

            i = self.x + coords[0]
            j = self.y + coords[1]

            if self.garden.coordsInRange(i,j):
                neighbour = self.garden.grid[i][j]
                self.neighbours.append(neighbour)
                if neighbour.type != self.type:
                    self.perimeter += 1
            else:
                self.perimeter += 1
                continue

class region:

    def __init__(self):
        self.type: chr
        self.plots: list[plot] = []
        self.area: int
        self.perimeter: int
        self.fencingPrice: int
        self.plotByCoords = {}

    def addAllPlotsToRegion(self, plot: plot):
        self.type = plot.type
        self.plots.append(plot)
        plot.isInARegion = True
        for otherPlot in plot.neighbours:
            if otherPlot.type == self.type and (not otherPlot.isInARegion):
                self.addAllPlotsToRegion(otherPlot)
    
    def initPlotbyCoords(self):
        for plot in self.plots:
            self.plotByCoords[plot.x, plot.y] = plot

    def getNextPlot(self, plot: plot, dir: tuple[int, int]):
        if plot.perimeter == 1:
            return 
        # GET TO WORK RIGHT HERE

    def calculatePrice(self):
        self.area = len(self.plots)
        self.perimeter = 0
        for plot in self.plots:
            per = plot.perimeter
            if per > 0:
                self.perimeter += plot.perimeter - 1
        self.fencingPrice = self.area*self.perimeter
    
    def printRegion(self):
        for plot in self.plots:
            print(plot.x, plot.y)


class garden:

    def __init__(self):
        self.regions: list[region] = []
        self.grid: list[list[plot]] = []

        input = open("Day 12/testInput.txt")

        for line in input:
            newLine = []
            for char in line:
                if char == "\n":
                    continue
                newLine.append(plot(char, self))
            self.grid.append(newLine)

        for x in range(0, len(self.grid)):
            for y in range(0,len(self.grid[x])):
                self.grid[x][y].setCoords(x,y)
                self.grid[x][y].getNeighbours()

        for x in range(0, len(self.grid)):
            for y in range(0,len(self.grid[x])):
                currentPlot = self.grid[x][y]
                if not currentPlot.isInARegion:
                    newRegion = region()
                    newRegion.addAllPlotsToRegion(currentPlot)
                    newRegion.initPlotbyCoords()
                    newRegion.calculatePrice()
                    self.regions.append(newRegion)
        input.close()
    
    def printInit(self):
        for region in self.regions:
            print(f"Type: {region.type} with area {region.area}, perimiter {region.perimeter} and price {region.fencingPrice}")
            #region.printRegion()
        print(f"A total fencing price of {self.PriceSum()}")

    def coordsInRange(self,x,y):
        if x < 0 or y < 0:
            return False
        if x > len(self.grid)-1:
            return False
        if y > len(self.grid[x])-1:
            return False
        return True
    
    def PriceSum(self):
        sum = 0
        for region in self.regions:
            sum += region.fencingPrice
        return sum

garden = garden()
garden.printInit()