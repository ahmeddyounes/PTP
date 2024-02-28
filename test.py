from ptp_table import PTPTable
from ptp_vogel import VolgelApproximation

table = [[3, 2, 7, 6], [7, 5, 2, 3], [2, 5, 4, 5]]

supply = [50, 60, 25]

demand = [60, 40, 20, 15]

vogel = VolgelApproximation(PTPTable(table, supply, demand))

vogel.approximate()

print(vogel.getSolvedTable().table)