import datetime

class Ship:
    def __init__(self,name:str,loadingTime:datetime.datetime):
        self.name = name
        self.loadingTime = loadingTime

    def getLoadingTime(self):
        return self.loadingTime

class Container:
    def __init__(self,name:str,ship:Ship):
        self.name = name
        self.ship = ship
        self.loadingDuration = 0

    def setloadingDuration(self,loadingDuration:float):
        self.loadingDuration = loadingDuration

    def getLabel(self):
        return self.name
    
    def getLoadingTime(self):
        return self.ship.getLoadingTime()
    
class Stack:
    def __init__(self):
        self.containers = []
    
    def add(self, container):
        self.containers.append(container)

    def remove(self):
        return self.containers.pop()
    
    def getContainers(self):
        return ','.join([x.getLabel() for x in self.containers])
    
    def getHeight(self):
        return len(self.containers)

class ShipYard:
    def __init__(self,x:int,y:int):
        self.shipyard = []
        if x<=1 or y<=1:
            raise(Exception,"Rows and columns must be positive integers")
        for row in range(x):
            rowContents = []
            for column in range(y):
                rowContents.append(Stack())
            self.shipyard.append(rowContents)

    def add(self,x:int,y:int,container:Container):
        self.shipyard[x][y].add(container)
    
    def remove(self,x,y):
        return self.shipyard[x][y].remove()
    
    def getShipYard(self):
        return self.shipyard
    
    def printShipYard(self):
        header = []
        for i in range(len(self.shipyard[0])):
            header.append(str(i))
        print("row\\col |"+'\t|'.join(header))
        j=0
        for row in self.shipyard:
            print(str(j)+"\t|",end='')
            print('\t|'.join([x.getContainers() for x in row]))
            j+=1
    
shipyard = ShipYard(2,2)
ships = [Ship('BoatyMcBoatFace',datetime.datetime(2024,11,1,10,20)),Ship('ShippyMcShipFace',datetime.datetime(2024,11,1,11)),Ship('YachtyMcYatchFace',datetime.datetime(2024,11,1,10))]
shipyard.add(0,0,Container('C-1',ships[2]))
shipyard.add(1,0,Container('C-2',ships[0]))
containers = [Container('C-3',ships[1]),Container('C-4',ships[0]),Container('C-5',ships[2]),Container('C-6',ships[2]),Container('C-7',ships[0])]

shipyard.printShipYard()