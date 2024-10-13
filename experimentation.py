from ShipYard import ShipYard,Container,Ship

def rmSort(a):  # a is an array
  if len(a) == 1:
    return a
  mid = len(a)//2
  a1 = rmSort(a[0:mid])
  a2 = rmSort(a[mid:len(a)])
  return merge2(a1, a2)

def merge2(a1, a2):
  i = 0
  j = 0
  r = []
  while i < len(a1) or j < len(a2):
    if (j == len(a2)) or (i < len(a1) and a1[i].getLoadingTime() < a2[j].getLoadingTime()):
      r.append(a1[i]) # pick item from a1
      i += 1
    else:
      r.append(a2[j]) # pick item from a2
      j += 1
  return r

def loadingAlgorithm(shipyard,containers):
    rownum, colnum = shipyard.getDimensions()
    containers = rmSort(containers)
    print([c.getLabel() for c in containers])
    i = 0
    sparestack = (0,0)
    for r in range(rownum):
        for c in range(colnum):
            col = shipyard.getStack(r,c)
            if col.getHeight()==4:
                if (r,c)==sparestack:
                    sparestack=(sparestack[0]+1,sparestack[1])
                continue
            while col.getHeight()<4 and i<len(containers) and (col.getHeight()==0 or containers[0].getLoadingTime()<=col.getTopContainer().getLoadingTime()):
                shipyard.add(r,c,containers[i])
                i+=1
            if i>=len(containers):
                return shipyard
    return shipyard

def calculateEfficiency(shipyard:ShipYard,ship_schedule:list):
    pass


if __name__ == '__main__':
    shipyard = ShipYard(2,2)
    ships = [Ship('BoatyMcBoatFace',datetime.datetime(2024,11,1,10,20)),Ship('ShippyMcShipFace',datetime.datetime(2024,11,1,11)),Ship('YachtyMcYatchFace',datetime.datetime(2024,11,1,10))]
    shipyard.add(0,0,Container('C-1',ships[2]))
    shipyard.add(1,0,Container('C-2',ships[0]))
    containers = [Container('C-3',ships[1]),Container('C-4',ships[0]),Container('C-5',ships[2]),Container('C-6',ships[2]),Container('C-7',ships[0])]

    result = loadingAlgorithm(shipyard,containers)
    result.printShipYard()