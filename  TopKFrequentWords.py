class Solution:
    def topKFrequent(self, words, k):
        dictMap = {}
        for i in words:
            if i not in dictMap:
                dictMap[i] = 1 
            else : 
                dictMap[i] += 1
        print(dictMap)
        resultSet = sorted(dictMap, key=lambda x: (-dictMap[x],x))
        print(resultSet)
        return resultSet[:k]