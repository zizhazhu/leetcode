class Solution:
    def simplifyPath(self, path: str) -> str:
        parts = path.split('/')
        folder = []
        for part in parts:
            if part == '' or part == '.':
                continue
            elif part == '..':
                if len(folder) != 0:
                    folder.pop()
            else:
                folder.append(part)
        path = '/'
        path += '/'.join(folder)
        return path
