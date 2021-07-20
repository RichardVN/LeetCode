"""
Approach: BFS
Let word character length be M and number of dict words be N

Time:   O(M^2 * N)  ,  O(M X N) to make combinations  and  each combination combination takes O(M) time to make new string
Space:  O(N)

Initialize:
    - words   :  set of all dictionary words, accessible in O(1) time
    - seen = set()   :   a set of seen words, to prevent adding to queue again and looping
    - queue   :  a queue of words that we have traveled to from original word, that we can expand
    - edit_count =  1  :  number of edits to get to endword,  incremented each bfs level
    
Procedure:
    1. Edge case, check that endWord is not already in words
    2. Create queue with beginWord only
    3. While Queue:  # BFS!!!
            for each word in queue level:
                pop word, add to seen, check if found EndWord
                
                For each letter in word: replace letter with 26 possible letters, check if valid word
                    if Valid word, add to queue, add to seen (so other words same level dont add)
            increment edit_count
"""     


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        # For a faster access turing it into a set
        words = set(wordList)
        
        # Edge case
        if endWord not in words: return 0
        
        # We will be doing a Breadth First search, so we begin with placing beginWord in the queue
        queue = collections.deque([beginWord])
        count = 1
        
        # To keep a track of what words we have visited already
        seen = set()
        
        while queue:
            # Picking up every word we put from the BFS neighbours
            # O(M X N)
            for _ in range(len(queue)):
                
                # Taking one element at a time
                word = queue.popleft()
                
                # We will not come to this word again
                seen.add(word)
                
                # Bingo, we won
                if word == endWord:
                    return count
                
                # Find the current words neighbours  O(M)
                for i in range(0, len(word)):
                    
                    # Try to create the possible new words  O(26)
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + c + word[i+1:]
                        
                        # Never visited this word, the word is in words  O(N)
                        if new_word in words and new_word not in seen:
                            queue.append(new_word)
                            seen.add(new_word)
            count+=1 
        return 0