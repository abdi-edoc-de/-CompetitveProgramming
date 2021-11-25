# from typing import defaultdict
from collections import deque,defaultdict


class Solution:
    def findLadders(self, beginWord , endWord, wordList):
        checkingStartRelation = [True]
        graph = defaultdict(list)
        graph = self.chageToGraph(beginWord, endWord, wordList,graph,checkingStartRelation)
        
        if checkingStartRelation[0]:
            return []
        if endWord not in wordList:
            return []
        # print(graph)
        return self.bfs(beginWord, endWord, graph)
    def bfs(self, beginWord, endWord, graph):
        visited = set()
        que = deque()
        
        que.append(([beginWord],beginWord))
        visited.add(beginWord) 
        while que:
            words ,word = que.popleft()
            # print(words)
            for neighbour in graph[word]:
                
                if neighbour == endWord:
                    words.append(neighbour)
                    # print('here')
                    # print(words)
                    # print('here')
                    return words + []
                if neighbour not in visited:
                    visited.add(neighbour)
                    que.append((words + [neighbour] , neighbour))
        return []
            
            
        
        
    def chageToGraph(self,beginWord , endWord, wordList,graph, checkingStartRelation):
        checkList = set(wordList)
        startL = ord('a')
        lastL = ord('z')
        n = len(wordList[0])
        for word in wordList:
            for k in range(n):
                for letter in range(startL,lastL+1):
                    newWord = word[0:k] + chr(letter) + word[k+1:]
                    if newWord != word and newWord in checkList:
                        graph[word].append(newWord)
                        
                        # print(newWord) 
        for k in range(n):
            for letter in range(startL, lastL + 1):
                newWord = beginWord[0:k] + chr(letter) + beginWord[k+1:]
                if newWord != beginWord and newWord in checkList:
                    checkingStartRelation[0] = False
                    graph[beginWord].append(newWord)
                    graph[newWord].append(beginWord)
        return graph

arr =["hot","dot","dog","lot","log","cog"]
print(Solution().findLadders('hit','cog',arr))