#Marcella Petrucci
#petrucma@oregonstate.edu
########################
#Program Description
# This program uses the Nearest Neighbor algorithm
# to find the approximate solution to the Traveling Salesman Problem.
# 
# the program takes a list of vertices as coordinate pairs, identified by an integer
# and processes them into vertex objects. 
# Edge weights are found by the Euclidean Distance formula 
# each of the n vertices is used as a starting vertex for the NN algorithm up to n = 300
# the Best Path and Path Weight are written to a file
###########################

#imports
import time
import numpy as np
import random
import math
import re, sys
#################################################
#       Function and class Definitions :
#################################################
class Vertex:
    def __init__(self, vID, coords):##pass in list of coord pairs 
        self.vID = vID
        self.x = coords[0]
        self.y = coords[1]
        self.visited = False

#################################################
#       Global variables:
#################################################        

numV = 0 # number of vertices/cities
pathWeight = 0 #total weight of TSP path

#################################################
#       Main Function :
# takes input file arg, initializes empty arrays, calls read and write
# calls TSP functions
# usage: python3 NN.py inputFileName
#################################################

def main(input):
    #take arg filename
    t1 = time.time()
    input_file = sys.argv[1]
    
    #initialize lists
    data = [] # raw input from file reading
    listOfVertices = []# input parsed into lists containing id and coord pairs
    graph = [] # list of vertex objects with vID,x, and y attributes    
    path = [] #list of vertices in order of visit

    #vals is list containing lists of data representing each line
    vals = readFile(input_file, data, listOfVertices)

    # list of vertex objects representing fully connected graph
    graph = createVertex(vals, graph)
    
    # append new extension to input file to create output_file
    ext = ".tour"
    output_file = input_file + ext
    
    # loops through all vertices as start nodes for NN algorithm
    bestPath(graph, path, output_file)
    t2 = time.time()
    finalTime = t2 - t1
    print(f'finalTime = {finalTime}')
    milliTime = finalTime * 1000.0
    print(f'finalTime in Milliseconds = {milliTime}')

#################################################
#   takes file name and reads input file
#   casts ints to strings
#   opens file and writes formatted output to it
#################################################

def readFile(input_file, data, listOfVertices):
    global numV
    file = open(input_file,'r')
    # store the first line as number of vertices
    numV = int(file.readline())
    i = 0
    while (True):
        
        line = file.readline()	# iterator

        if not line:
            break
        # remove new line character leading white space from line
        line = line.strip("\n")
        line = line.lstrip()
        # add to data list
        data.append(line)
  
        # this parses at whiteSpace, casts to int, maps into list, and appends to listOfVertices
        listOfVertices.append(list(map(int, data[i].split())))
        i = i + 1

    return listOfVertices
 

#################################################
#   takes vertex ID and list of vertices and empty graph list
#   creates vertex objects
#   adds vertices to graph list and returns it
#################################################
def createVertex(vals, graph):
    #iterate through list of vertices, create vertex obj and add to graph
    for i in range(0, len(vals)):
        #vID is the first index, representing the vertex id
        # loop through vals[i] to initiate vertex node ID's, initialize vertices, store in graph list
        vID = vals[i].pop(0)
        vertex = Vertex(vID, vals[i])
        graph.append(vertex)
    return graph

#################################################
#       takes two coordinate pairs
#   finds and returns the euclidean distance
#################################################
def EuclideanDistance(x1, y1, x2, y2):
    ## the euclidean formula in two parts
    num = pow((x1- x2), 2) + pow((y1 - y2),2)
    sq = round(math.sqrt(num))
    # print(f'E = [{x1},{y1}] - [{x2},{y2}] W = {sq}')
    return sq

#################################################
# takes graph list representing fully connected graph
# takes empty path list to store vertices in order of visitation
# takes start vertex
#
# this is the Nearest Neighbor algorithm
# curr vertex is processed by looping through all connected, 
# unvisited vertices adjacent on curr, calculating edge weights
# between each vertex and curr by calling EuclideanDistance() 
# the minimum weight and edge is stored as the next vertex in path[]
#################################################
def findPath(graph, path, start):
    global pathWeight
    #global
    minWeight = 1000000
    curr = start
    path.append(curr)
    numV = len(graph)
    for i in range(0, len(graph)):
           #### this uses vertices and continually computes weights
        if (numV > 1):#exits after last node is added to path
            #mark current vertex as visited
            curr.visited = True
            #compare to all other vertices
            for j in range(0, len(graph)):
                #if vertex is not visited
                if(graph[j].visited == False):
                    # current comparison weight is set
                    #find weight with euclidean distance, pasing .x and .y attributes of each vertex obj
                    weight = EuclideanDistance(graph[j].x, graph[j].y, curr.x, curr.y)
     
                    #find least weighted edge
                    if (weight < minWeight):                        
                        minWeight = weight
                        tempV = graph[j]
                        
            ##UPDATE OUTER FOR LOOP VARIABLES
            #set least weighted edge to path and increment path weight
            path.append(tempV)
            pathWeight = pathWeight + minWeight
            minWeight = 1000000
            #update current vertex to end of new path
            curr = tempV
            numV = numV - 1

    ##add the weight of the final edge connected to start vertex to the total path weight
    finalEdgeWeight = EuclideanDistance(path[0].x, path[0].y, curr.x, curr.y)
    pathWeight = pathWeight + finalEdgeWeight
        
    # print(pathWeight)
    # print("path")    
    # for i in range(0, len(path)): 
        # print(path[i].vID)
        
    return path

#################################################
#   takes graph list, empty path list, and output_file
#   loops through all vertices of graph and uses
#   each vertex as start point for NN algo
#   stores best total path and weight 
#   and calls writeToFile, passing output_file
#################################################

def bestPath(graph, path, output_file):
    global pathWeight
    global numV
    bestPath = []
    bestPathWeight = 100000000000
    
    #large data sets will only run on 1 of every 1000 vertices
    if (numV > 300):
        for i in range(0, len(graph), 100):
            path = findPath(graph, path, graph[i])
            #save lowest pathWeight
            if(bestPathWeight > pathWeight):
                bestPathWeight = pathWeight
                bestPath = path.copy()

            #reset visited attribute for new path assessment
            for x in range(len(graph)):
                graph[x].visited = False
            # reset path and path weight
            pathWeight = 0
            path.clear()
    
    else:
        for i in range(len(graph)):
            path = findPath(graph, path, graph[i])
            # for x in range(len(path)):
                # print(f' p = {path[x].vID}')
            # print(f'pathWeight = {pathWeight}')
            #save lowest pathWeight
            if(bestPathWeight > pathWeight):
                bestPathWeight = pathWeight
                bestPath = path.copy()

            #reset visited attribute for new path assessment
            for x in range(len(graph)):
                graph[x].visited = False
            # reset path and path weight
            pathWeight = 0
            path.clear()
    
    print("bestPath")
    print(bestPathWeight)
    for z in range(0, len(bestPath)): 
        print(bestPath[z].vID)
    writeToFile(bestPath, bestPathWeight, output_file)

#################################################
#   takes bestPath list of vertex objs and bestPathWeight
#   creates and opens output_file and writes formatted output to it
#   if output_file has contents, they will be overwritten
#################################################
    
def writeToFile(bestPath, bestPathWeight, output_file):
    # open file in write mode
    f = open(output_file, "w")
    # write path weight in str format
    f.write(str(bestPathWeight) + "\n")
    # print one vertex per line in str format
    for i in range(0, len(bestPath)):    
        f.write(str(bestPath[i].vID) + "\n")
    f.close()

# system call to accept arguments on the command line
if __name__ == '__main__':
	main(sys.argv[1])