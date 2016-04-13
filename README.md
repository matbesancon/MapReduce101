# Map Reduce 101: getting started with basic computation

These computations use a Map Reduce object getting case-specific functions 
map and reduce. 

## Query from graph: a mini social network

The scripts friend_count.py and asymetric_friendships.py compute
number of friends for each person and the assymetric relations 
(one-way friendship) respectively.

## Linear algebra in MapReduce

Using two sparse matrices stored as tuples 
(matrix_name, row, column, value), the goal of multiply.py is to output 
the result of the matrix multiplication in the same format.

## Unique trims: data processing for biology

From DNA sequences, unique_trim.py takes out the ten last elements and 
return only the unique sequences (no copy).

## Mimic SQL/relational algebra in MapReduce

join.py builds a join between two tables.

## Retrieve information on book data

word_count.py... well trivially counts the occurrence of words in 
all documents of a data base. inverted_index.py finds all documents 
containing each word.
