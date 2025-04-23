# Time Complexity: O(k^n * n log(k^n)), where k = avg options, n = num of segments
# Space Complexity: O(k^n * n)

class Solution:
    def expand(self, s: str) -> List[str]:
        def parse(s):
            i = 0
            groups = []
            while i < len(s):
                if s[i] == '{':
                    i += 1
                    options = []
                    while s[i] != '}':
                        if s[i] != ',':
                            options.append(s[i])
                        i += 1
                    groups.append(sorted(options))
                    i += 1  # skip '}'
                else:
                    groups.append([s[i]])
                    i += 1
            return groups
        
        def backtrack(groups, index, path, res):
            if index == len(groups):
                res.append("".join(path))
                return
            for ch in groups[index]:
                path.append(ch)
                backtrack(groups, index + 1, path, res)
                path.pop()
        
        parsed = parse(s)
        result = []
        backtrack(parsed, 0, [], result)
        return result
