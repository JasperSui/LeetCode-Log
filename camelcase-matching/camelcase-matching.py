class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def u(s):
            return [c for c in s if c.isupper()]
        
        def issup(p, s):
            it = iter(s)
            return all(c in it for c in p)
        
        return [u(q) == u(pattern) and issup(pattern, q) for q in queries]