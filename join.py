import MapReduce
import sys

"""
SQL join operation with MapReduce
"""

mr = MapReduce.MapReduce()

def mapper(record):
    # key: document identifier
    # value: document contents
    table = record[0]
    key = record[1]
    value = record[2:]
    mr.emit_intermediate((table,key), record)

def reducer(key_tuple, list_of_values):
    # key: word
    # value: list of document-ids
    if key_tuple[0]=="order":
        for keyt2 in mr.intermediate.keys():
            if ("line_item",key_tuple[1])==keyt2:
                list_val2 = mr.intermediate[keyt2]
                temp = list_of_values
                for lis2 in list_val2:
                    mr.emit(list_of_values[0]+lis2)

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
