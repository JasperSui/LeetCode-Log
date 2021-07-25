# class TrieNode:
#     def __init__(self):
#         self.links = defaultdict(TrieNode)

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()
        
#     def insert(self, word, pattern):
#         node = self.root
#         for c in word:
#             if not pattern:
#                 if ord('A') <= ord(c) <= ord('Z'):
#                     return False
#             if pattern and c == pattern[0]:
#                 pattern.pop(0)
            
    
        
class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        return [self.get_ans(word, list(pattern)) for word in queries]
    
    def get_ans(self, word, pattern):
        for c in word:
            if pattern:
                if (ord('A') <= ord(c) <= ord('Z') and c == pattern[0]) or ord(c) > ord('Z'):
                    if c == pattern[0]:
                        pattern.pop(0)
                else:
                    return False
            else:
                if ord('A') <= ord(c) <= ord('Z'):
                    return False
        return pattern == []
        