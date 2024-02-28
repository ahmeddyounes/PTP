# PTP
Python Transportation Problem Solver

# Example
To create a new table use ```PTPTable``` from ptp_table.py file as follows:
```python
from ptp_table import PTPTable

table = [[3, 2, 7, 6], [7, 5, 2, 3], [2, 5, 4, 5]]
supply = [50, 60, 25]
demand = [60, 40, 20, 15]

ptpTable = PTPTable(table, supply, demand)
```

Now you have the table ready you can approximate its solution using Vogel's approximaion method:
```python
from ptp_vogel import VolgelApproximation

vogel = VolgelApproximation(ptpTable)
vogel.approximate()

print(vogel.getSolvedTable().table)
```
