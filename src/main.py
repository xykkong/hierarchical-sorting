#!/usr/bin/env python3

from hierarchical_sort import HierarchicalSort
import csv
import sys
from functools import cmp_to_key

def main(argv):
    if len(argv) == 0:
        print('Error: File not specified.\n')
        sys.exit(1)
            
    file = argv[0]
    with open(file) as file:
        arr = []
        isFirstLine = True
        for line in csv.reader(file, delimiter="|"):
            if(isFirstLine):
                header = line
                isFirstLine = False
            else:
                arr.append(line)

        mysort = HierarchicalSort(header, asc=False)
        arr.sort(key=cmp_to_key(mysort.sort))
        arr.insert(0, header)

        for row in arr:
            print("|".join(row))



if __name__ == "__main__":
    main(sys.argv[1:])

