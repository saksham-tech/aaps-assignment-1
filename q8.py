def permute(s):
    result = []
    s = list(s)

    def backtrack(start):
        if start == len(s):
            result.append("".join(s))
            return
        for i in range(start, len(s)):
            s[start], s[i] = s[i], s[start]
            backtrack(start + 1)
            s[start], s[i] = s[i], s[start]
    
    backtrack(0)
    return result

#TIME COMPLEXITY = O(n × n!)
#SPACE COMPLEXITY = O(n) 