class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        # build adjacency list
        nei = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            # find all the wild card patterns
            # use j to go through all possible positions to replace with wild card *
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                # char at jth position is replaced with *
                nei[pattern].append(word) # add word to neighbor list for that pattern
        
        # Define visit set so we don't revisit the same word
        visit = set([beginWord])
        q = deque()
        q.append(beginWord)
        res = 1 # start with one word

        while q:
            # go through the entire layer before continuing
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res # found the endword so return the length of the path
                
                # otherwise go through all its possible wildcard patterns
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neiWord in nei[pattern]:
                        if neiWord not in visit:
                            # if not visited, add its neighbors to queue for processing
                            q.append(neiWord)
                            visit.add(neiWord)
            
            res += 1 # increment res after going through entire layer
        return 0 # return 0 when queue is empty and word != endWord
