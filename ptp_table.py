
class PTPTable:

    def __init__(self, table, supplies, demands) -> None:
        self.table = table
        self.supplies = supplies
        self.demands = demands

class PTPSolvedTable:
    def __init__(self, supplies, demands) -> None:
        self.supplies = supplies.copy()
        self.demands = demands.copy()
        self.table = [ [0]*len(demands) for _ in range(len(supplies)) ]
    
    def getTable(self) -> list:
        return self.table
    
    def setValue(self, i, j, value) -> None:
        self.table[i][j] = value

    def supply(self, row, column) -> None:
        supplyCount = self.supplies[row]
        demandCount = self.demands[column]
        if supplyCount <= demandCount:
            self.supplies[row] = 0
            self.demands[column] = self.demands[column] - supplyCount
            self.setValue(row, column, supplyCount)
        elif supplyCount > demandCount:
            self.demands[column] = 0
            self.supplies[row] = supplyCount - demandCount
            self.setValue(row, column, demandCount)