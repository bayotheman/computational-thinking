from xml import dom
from greedy import *

def chooseBest(pset, maxWeight, getVal, getWeight):
    bestVal = 0.0
    bestSet = None
    for items in pset:
        itemsVal = 0.0
        itemsWeight = 0.0
        for item in items:
            itemsVal += getVal(item)
            itemsWeight += getWeight(item)
        if(itemsWeight <= maxWeight and itemsVal > bestVal):
            bestVal = itemsVal
            bestSet = items
    return (bestSet, bestVal)

def genPowerSet(items):
    pset = [[]]
    n = len(items)
    itemList = []
    size = 2 ** n
    # pset.append(itemList)
    for i in range(n):
        pset.append([items[i]])
        for j in range(0, n, i+1):
            pset.append([items[i:j]])

    pset.append(items)
    print("lenght ",len(pset))
    return pset



        



def testBest(maxWeight = 20):
    items = buildItems()
    pset = genPowerSet(items)
    taken, val = chooseBest(pset, maxWeight, Item.getValue, Item.getWeight)
    print('Total value of items taken is', val)
    for item in taken: 
        print(item)

genPowerSet(buildItems())

# testBest()