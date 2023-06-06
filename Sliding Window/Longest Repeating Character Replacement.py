def characterReplacement(s, k):
    count = {}
    l, res, maxF = 0, 0, 0
    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        maxF = max(maxF, count[s[r]])
        while r - l + 1 - maxF > k:
            count[s[l]] -= 1
            l += 1
        res = max(res, r - l + 1)
    return res


print(characterReplacement("ABABBA", 2))
