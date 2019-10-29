from collections import defaultdict
class Solution(object):
    def __init__(self):
        self.length = 0
        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        self.all_combo_dict = defaultdict(list)

    def visitWordNode(self, queue, visited, others_visited):
        current_word, level = queue.popleft()
        for i in range(self.length):
            # Intermediate words for current word
            intermediate_word = current_word[:i] + "*" + current_word[i+1:]

            # Next states are all the words which share the same intermediate state.
            for word in self.all_combo_dict[intermediate_word]:
                # If the intermediate state/word has already been visited from the
                # other parallel traversal this means we have found the answer.
                if word in others_visited:
                    return level + others_visited[word]
                if word not in visited:
                    # Save the level as the value of the dictionary, to save number of hops.
                    visited[word] = level + 1
                    queue.append((word, level + 1))
        return None

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        # Since all words are of same length.
        self.length = len(beginWord)

        for word in wordList:
            for i in range(self.length):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                self.all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)


        # Queues for birdirectional BFS
        queue_begin = collections.deque([(beginWord, 1)]) # BFS starting from beginWord
        queue_end = collections.deque([(endWord, 1)]) # BFS starting from endWord

        # Visited to make sure we don't repeat processing same word
        visited_begin = {beginWord: 1}
        visited_end = {endWord: 1}
        ans = None

        # We do a birdirectional search starting one pointer from begin
        # word and one pointer from end word. Hopping one by one.
        while queue_begin and queue_end:

            # One hop from begin word
            ans = self.visitWordNode(queue_begin, visited_begin, visited_end)
            if ans:
                return ans
            # One hop from end word
            ans = self.visitWordNode(queue_end, visited_end, visited_begin)
            if ans:
                return ans

        return 0

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
        self.predecessor = None
        self.discovery = 0
        self.finish = 0

    def setDiscovery(self, time):
        self.discovery = time

    def setFinish(self, time):
        self.finish = time

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

class Solution(object):
    def __init__(self):
        self.time = 0
    def ladderLength(self, beginWord, endWord, wordList):
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
            return end.getDistance() + 1
        else:
            return 0
		
    
    def buildGraph(self, words):
        aGraph = Graph()
        bucketDict = {}
        for w in words:
            for i in range(len(w)):
                bucket = w[:i] + '_' + w[i+1:]
                if bucket in bucketDict:
                    bucketDict[bucket].append(w)
                else:
                    bucketDict[bucket] = [w]

        for bucket in bucketDict:
            for w1 in bucket:
                if w1 not in aGraph:
                    aGraph.addVertex(w1)
                for w2 in bucket:
                    if w1 != w2:
                        if w2 not in aGraph:
                            aGraph.addVertex(w2)
                        aGraph.addEdge(w1, w2)
                        aGraph.addEdge(w2, w1)
        return aGraph

    def bfs(self, graph, start):
        aQueue = Queue()
        aQueue.dequeue(start)
        while not aQueue.isEmpty():
            v = aQueue.dequeue()
            for nbr in v.getConnections():
                if nbr.color == 'white':
                    nbr.setColor('gray')
                    nbr.setPredecessor(v)
                    nbr.setDistance(v.distance + 1)
                    aQueue.enqueue(nbr)
            v.setColor('black')

    def dfs(self, graph, start):
        start.setColor('gray')
        self.time += 1
        start.setDiscovery(self.time)
        for v in start.getConnections():
            if v.color == 'white':
                self.dfs(graph, v)
        start.setColor('black')
        self.time += 1
        start.setFinish(self.time)

    def bfs(self, graph, start):
        aStack = []
        aStack.append(start)
        while aStack:
            v = aStack.pop()
            if v.color == 'white':
                v.setColor('gray')
                self.time += 1
                v.setDiscovery(self.time)
                for nbr in v.getConnections():
                    aStack.append(v)
            else
                if v.color == 'gray':
                    v.setColor('balck')
                    self.time += 1
                    v.setFinish(self.time)

            

            

