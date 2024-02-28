from ptp_table import PTPSolvedTable

class VolgelApproximation:
    def __init__(self, ptpTable) -> None:
        self.ptpTable = ptpTable
        self.solvedTable = PTPSolvedTable(ptpTable.supplies, ptpTable.demands)

    def getSolvedTable(self) -> PTPSolvedTable:
        return self.solvedTable

    def getDeffirence(self, firstLength, secondLength, getVal, supplyFirst) -> list:
        difference = []

        firstMin = -1
        secondMin = -1
        for i in range(firstLength):
            if supplyFirst:
                if self.getSupply(i) <= 0:
                    difference.append(-1)
                    continue
            else:
                if self.getDemand(i) <= 0:
                    difference.append(-1)
                    continue

            for j in range(secondLength):
                if supplyFirst:
                    if self.getDemand(j) <= 0:
                        continue
                else:
                    if self.getSupply(j) <= 0:
                        continue
                val = getVal(i, j)
                if firstMin < 0:
                    firstMin = val
                elif secondMin < 0:
                    secondMin = val
                else:
                    if firstMin <= secondMin:
                        if secondMin > val:
                            secondMin = val
                    else:
                        if firstMin > val:
                            firstMin = val
            if secondMin < 0 and firstMin >= 0:
                difference.append(firstMin)
            elif firstMin >= 0 and secondMin >= 0:
                difference.append(abs(firstMin-secondMin))
            else:
                difference.append(-1)
            firstMin = -1
            secondMin = -1
        return difference

    def getRowDifference(self) -> list:
        rowLength = len(self.ptpTable.table)
        columnLength = len(self.ptpTable.table[0])
        return self.getDeffirence(rowLength, columnLength, lambda i, j: self.ptpTable.table[i][j], True)

    def getColumnDifference(self) -> list:
        rowLength = len(self.ptpTable.table)
        columnLength = len(self.ptpTable.table[0])
        return self.getDeffirence(columnLength, rowLength, lambda i, j: self.ptpTable.table[j][i], False)

    def getMaxList(self, firstList, secondList) -> tuple:
        if max(firstList) >= max(secondList):
            return self.getMaxIndex(firstList), 1
        return self.getMaxIndex(secondList), 0

    def getMaxIndex(self, list) -> int:
        return max(range(len(list)), key=list.__getitem__)

    def getSupply(self, index) -> int:
        return self.solvedTable.supplies[index]

    def getDemand(self, index) -> int:
        return self.solvedTable.demands[index]

    def isThereDemand(self) -> bool:
        return max(self.solvedTable.demands) > 0

    def isThereSupply(self) -> bool:
        return max(self.solvedTable.supplies) > 0

    def getMinRowIndex(self, index) -> int:
        mIndex = -1
        mValue = -1
        for i in range(len(self.ptpTable.table[index])):
            if self.getDemand(i) > 0:
                if mValue < 0 or mValue > self.ptpTable.table[index][i]:
                    mValue = self.ptpTable.table[index][i]
                    mIndex = i
        return mIndex

    def getMinColumnIndex(self, index) -> int:
        mIndex = -1
        mValue = -1
        for i in range(len(self.ptpTable.table)):
            if self.getSupply(i) > 0:
                if mValue < 0 or mValue > self.ptpTable.table[i][index]:
                    mValue = self.ptpTable.table[i][index]
                    mIndex = i
        return mIndex

    def approximate(self) -> None:
        while self.isThereSupply() or self.isThereDemand():
            rowDifference = self.getRowDifference()
            columnDifference = self.getColumnDifference()
            maxIndex, isRow = self.getMaxList(rowDifference, columnDifference)
            if isRow:
                minIndex = self.getMinRowIndex(maxIndex)
                self.solvedTable.supply(maxIndex, minIndex)
            else:
                minIndex = self.getMinColumnIndex(maxIndex)
                self.solvedTable.supply(minIndex, maxIndex)
                