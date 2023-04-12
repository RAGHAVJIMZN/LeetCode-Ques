class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        stack = []
        for name in path:
            if p not in ['','.','..']:
                stack.append(name)
            elif c=='..' and stack:
                stack.pop()
        return '/'+'/'.join(stack)