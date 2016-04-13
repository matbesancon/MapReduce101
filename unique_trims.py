import MapReduce
import sys

"""
Cut DNA strings and retrieve only the unique versions
"""

mr = MapReduce.MapReduce()

def mapper(record):
    mr.emit_intermediate(record[0], record[1][:-10])

def reducer(key, list_of_values):
    # mr.emit((key,list_of_values[0]))
    if list_of_values[0] not in mr.result:
        mr.emit(list_of_values[0])

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
