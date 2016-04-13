import MapReduce
import sys

"""
Inverted index with Map Reduce
"""

mr = MapReduce.MapReduce()

def mapper(record):
    mr.emit_intermediate(record[0], record[1])

def reducer(key, list_of_values):
    for friend in list_of_values:
        if friend not in mr.intermediate.keys() or key not in mr.intermediate[friend]:
            mr.emit((key,friend))
            mr.emit((friend,key))

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
