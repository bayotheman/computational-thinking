class Item(object) :
    def __init__(self, name, value, weight):
        self.name = name
        self.value = value
        self.weight = weight

    def getName(self):
        return self.name

    def getValue(self):
        return self.value

    def getWeight(self):
        return self.weight

    def __str__(self):
        result = '<' + self.name + ', ' + str(self.value)\
                + ', ' + str(self.weight) + '>' 
        return result
    # def getDensity(self):
    #     return self.value/self.weight

def value(item):
    return item.getValue()

def weightInverse(item):
    return 1/item.getWeight()

def density(item):
    return item.getValue()/item.getWeight()

def greedy(items, maxWeight, keyFunction):
    """Assumes Items a list, maxWeight >= 0,
        keyFunction maps elements of Items to numbers"""        
    itemsCopy = sorted(items, key= keyFunction, reverse=True)
    result = []
    totalValue, totalWeight = 0.0, 0.0
    for i in range(len(itemsCopy)):
        if(totalWeight + itemsCopy[i].getWeight() <= maxWeight):
            result.append(itemsCopy[i])
            totalValue += itemsCopy[i].getValue()
            totalWeight += itemsCopy[i].getWeight()
    return (result, totalValue)
