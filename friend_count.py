import MapReduce
import sys

"""
Inverted index with Map Reduce
"""

mr = MapReduce.MapReduce()

def mapper(record):
    # key: document identifier
    # value: document contents
    mr.emit_intermediate(record[0], record[1])

def reducer(key, list_of_values):
    mr.emit((key,len(list_of_values)))

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
