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
    
    def getTopContainer(self):
        return self.containers[-1]
    
    def getContainerOrder(self,name):
        i=1
        for con in self.containers[::-1]:
            if con.getLabel() != name:
                i+=1
            else:
                return i


class ShipYard:
    def __init__(self,x:int,y:int):
        self.x = x
        self.y = y
        self.shipyard = []
        self.shipmapping = {}
        self.containermapping = {}
        if x<=1 or y<=1:
            raise(Exception,"Rows and columns must be positive integers")
        for row in range(x):
            rowContents = []
            for column in range(y):
                rowContents.append(Stack())
            self.shipyard.append(rowContents)

    def add(self,x:int,y:int,container:Container):
        self.shipyard[x][y].add(container)
        if container.ship not in self.shipmapping:
            self.shipmapping[container.ship] = []
        self.shipmapping[container.ship].append(container)
        self.containermapping[container] = x,y
    
    def remove(self,x,y):
        return self.shipyard[x][y].remove()
    
    def getShipYard(self):
        return self.shipyard
    
    def getDimensions(self):
        return self.x, self.y
    
    def getStack(self,x,y):
        return self.shipyard[x][y]
    
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