class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, x):
        self.items.insert(0, x)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return len(self.items) == 0

class Vertex(object):
    def __init__(self, key):
        self.key = key
        self.connectedTo = {}
        self.distance = 0
        self.color = 'white'
        self.predecessor = []
    
    def setColor(self, color):
        self.color = color

    def addNeighbor(self, nbr, weight = 0):
        self.connectedTo[nbr] = weight

    def getConnections(self):
        return self.connectedTo.keys()

    def setPredecessor(self, n):
        self.predecessor = n

    def setDistance(self, dis):
        self.distance = dis

    def getDistance(self):
        return self.distance

class Graph(object):
    def __init__(self):
        self.verList = {}
        self.numVertices = 0

    def addVertex(self, key):
        newVertex = Vertex(key)
        self.verList[key] = newVertex

    def getVertex(self, key):
        if key in self.verList:
            return self.verList[key]
        else:
            return None

    def __contains__(self, key):
        return key in self.verList

    def addEdge(self, f, t, weight = 0):
        if f not in self.verList:
            self.addVertex(f)
        if t not in self.verList:
            self.addVertex(t)
        self.verList[f].addNeighbor(self.verList[t], weight)
    
    def printGraph(self):
        for n in self.verList:
            print('%s\t%s' %(n, self.verList[n].getDistance()))

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList.append(beginWord)
        aGraph = self.buildGraph(wordList)
        end = aGraph.getVertex(endWord)
        if end:
            start = aGraph.getVertex(beginWord)
            self.bfs(aGraph, start)
            #aGraph.printGraph()
            #print(len(end.predecessor))
            return self.getPath(end)
        else:
            return []


    def buildGraph(self, words):
        aGraph = Graph()
        bucketDict = {}
        for w in words:
            #print(w)
            for i in range(len(w)):
                bucket = w[:i] + '_' + w[i+1:]
                #print(bucket)
                if bucket in bucketDict:
                    bucketDict[bucket].append(w)
                else:
                    bucketDict[bucket] = [w]
        #print(bucketDict)

        for bucket in bucketDict:
            for w1 in bucketDict[bucket]:
                for w2 in bucketDict[bucket]:
                    if w1 != w2:
                        aGraph.addEdge(w1, w2)
                        aGraph.addEdge(w2, w1)
        return aGraph

    def bfs(self, graph, start):
        aQueue = Queue()
        aQueue.enqueue(start)
        while not aQueue.isEmpty():
            v = aQueue.dequeue()
            
            #print('-'*3 + str(v.key) + '-'*3 + str(v.distance) + '-'*3)
            for nbr in v.getConnections():
                #print('%s\t%s' %(nbr.key, nbr.distance))
                if nbr.color == 'white':
                    nbr.setColor('gray')
                    nbr.predecessor.append(v)
                    nbr.setDistance(v.distance + 1)
                    aQueue.enqueue(nbr)
                    #print('%s\t%s' %(nbr.key, nbr.distance))
                else:
                    #print('%s\t%s\t%s' %(nbr.key, nbr.getDistance, v.key,)
                    if nbr.getDistance() == v.distance + 1:
                        nbr.predecessor.append(v)
                        #print('add again')
            v.setColor('black')
    
    def getPath(self, end):
        if not end.predecessor:
            return [[end.key]]
        else:
            path = []
            for n in end.predecessor:
                restpath = self.getPath(n)
                #print('%s\t%s' %(n.key, str(restpath)))
                for rp in restpath:
                    onepath = rp[:]
                    onepath.append(end.key)
                    path.append(onepath)
            return path
                    
                
                
                
            
            
