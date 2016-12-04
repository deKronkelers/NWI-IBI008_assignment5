# author: Hendrik Werner s44549775
# author: Constantin Blach s4329872

import csv
import numpy as np

# exercise 2.1
with open("./data/MovieLensData.txt") as movieLens:
    items = 1682
    reader = csv.reader(movieLens)
    data = np.array(list(reader))

    # exercise 2.2

    # exercise 2.3
    item_counts = []
    for i in range(1, items + 1):
        count = 0
        for basket in data:
            if str(i) in basket:
                count += 1
        item_counts.append((i, count))
    item_counts.sort(key=lambda item: item[1], reverse=True)
    print(item_counts)
