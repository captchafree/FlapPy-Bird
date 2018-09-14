class State:
    def __init__(self, xDist, yDist, isAlive_):
        self.xDistance = xDist
        self.yDistance = yDist
        self.isAlive = isAlive_

    def __hash__(self):
        return hash((self.xDistance, self.yDistance, self.isAlive))

    def __eq__(self, other):
        return (self.xDistance, self.yDistance, self.isAlive) == (other.xDistance, other.yDistance, other.isAlive)

    def __ne__(self, other):
        return not(self == other)

    def __str__(self):
        return "State: (" + str(self.xDistance) + ", " + str(self.yDistance) + ") isAlive = " + str(self.isAlive)
