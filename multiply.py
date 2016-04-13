import MapReduce
import sys

"""
Matrix multiplication from sparse tables
"""

mr = MapReduce.MapReduce()

def mapper(record):
    # key: document identifier
    # value: document contents
    mat = record[0]
    (x,y) = (record[1],record[2])
    value = record[3]
    print("-----value-------")
    print(value)
    print("------------")
    if "a"==mat:
        mr.emit_intermediate(('r',x,y),value)
        for key in mr.intermediate.keys():
            if key[0]=='c' and key[1]==y:
                mr.emit_intermediate(('rc',x,key[1]),value*mr.intermediate[key][0])
    elif "b"==mat:
        mr.emit_intermediate(('c',x,y),value)
        for key in mr.intermediate.keys():
            if key[0]=='r' and key[2]==x:
                mr.emit_intermediate(('rc',key[1],y),value*mr.intermediate[key][0])


def reducer(key, list_of_values):
    if key[0]=='rc':
        mr.emit((key[1],key[2],sum(list_of_values)))

    # print(mr.intermediate)
    #     print('hello')
        # print('list val')
    #     print(list_of_values)

# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
