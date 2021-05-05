def numWaterBottles(numBottles: int, numExchange: int):
    drunk = 0
    left = 0
    empty = 0
    while True:
        drunk += numBottles
        empty = numBottles + left
        left = empty % numExchange
        if empty // numExchange == 0:
            return drunk
        else:
            numBottles = empty // numExchange
    return drunk


print(numWaterBottles(9, 3))