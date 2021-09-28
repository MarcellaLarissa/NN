# NN - Nearest Neighbor Algorithm

## Program Description ##

# This program uses the Nearest Neighbor algorithm
# to find an approximate solution to the Traveling Salesman Problem.
# 
# the program takes a list of vertices as coordinate pairs, identified by an integer
# and processes them into vertex objects. 
# Edge weights are found by the Euclidean Distance formula 
# each of the n vertices is used as a starting vertex for the NN algorithm up to n = 300
# the Best Path and Path Weight are written to a file

## Included Files ##

tsp_example_0.txt 
...
tsp_example_5.txt
Problem sets to run with program as argument. Contains numbered list of vertices as coordinate pairs with number of vertices listed at the top.

tsp-verifier.py
TSPAllVisited.py
TSPAllVisited.pyc
Testing program writtin by course instructor Julie Schutfort. Takes starting vertex list and resulting tour list and verifies that all vertices are valid and gives approximate solution to the tour weight.

## Running Directions for Program ##

Please execute using python3. This program accepts one argument on the command line

The command will be: python3 NN.py testFileName.txt

## Running Directions for Test/Verifier Program ##

This program takes the original coordinate example file and the file created by the original program as arguments, for example -
python3 tsp-verifier.py tsp_example_0.txt tsp_example_0.txt.tour