class ShipYard:
    def __init__(self,x,y):
        self.shipyard = []
        for row in range(x):
            rowContents = []
            for column in range(y):
                rowContents.append(Stack())
            self.shipyard.append(rowContents)

    def addContainer(self,x,y,container):
        self.shipyard[x][y].add(container)
    
    def removeContainer(self,x,y):
        return self.shipyard[x][y].remove()
    
    def getShipYard(self):
        return self.shipyard
    
    def printShipYard(self):
        for row in self.shipyard:
            print([x.getContents() for x in row])

    def getStack(self,x,y):
        return self.shipyard[x][y]

class Container:
    def __init__(self,label,ship):
        self.label = label
        self.ship = ship
        self.unloadingTime = 0

    def setUnloadingTime(self,unloadingTime):
        self.unloadingTime = unloadingTime

    def getLabel(self):
        return self.label

class Stack:
    def __init__(self):
        self.contents = []
    
    def add(self, content):
        self.contents.append(content)

    def remove(self):
        return self.contents.pop()
    
    def getContents(self):
        return [x.getLabel() for x in self.contents]
    
shipyard = ShipYard(3,3)
stack = shipyard.getStack(1,1)
stack.add(Container('A1','Boeing'))
stack.add(Container('A2','Boeing2'))
shipyard.printShipYard()