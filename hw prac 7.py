from math import floor
from datetime import datetime

data = [
    ("Post code", "Cost, thousands USD", "Country", "City", "Street", "Build.", "App.", "Date"),
    (33022, 543.67, 'USA', 'New York', '53rd street', 44, 345, datetime(2020, 1, 30, 11, 45, 33, 654357)),
    (33145, 9563214.67555478, 'UK', 'London', '45 yard av.', 3, 210, datetime(1985, 4, 2, 22, 45, 45, 45385)),
    (33658, 85543, 'Australia', 'Sidney', 'Cristmess eve str.', 235, 3, datetime(2010, 10, 10, 10, 0)),
    (33854, 10, 'Ukraine', 'Lutsk', 'Soborna str.', 10, 5342, datetime(2008, 2, 28, 23, 33, 33, 0)),
    (33698, 1000000000.01, 'USA', 'Washington', 'Columbia str.', 25, 222, datetime(2021, 9, 29, 7, 34, 1, 143)),
]
for x in data[0:1]:
    (z, x, c, v, b, n, m, d) = x
    print('| {:^10}| {:^19} | {:^10}| {:^10} | {:^19}| {:^6} | {:^4} | {:^26} |'.format(z, x, c, v, b, n, m, d))
print("|-----------+---------------------+-----------+------------+--------------------+--------+------+----------------------------|")
for line in data[1:]:
    (post_code, cost, country, city, street, build, app, dt) = line
    print('| {:<10}| {:>19} | {:<10}| {:<10} | {:<19}| {:>6} | {:>4} | {:^26} |'.format(post_code, format(floor(cost)/1000, '.3f'), country, city, street, build, app, dt.isoformat('T', "microseconds")))