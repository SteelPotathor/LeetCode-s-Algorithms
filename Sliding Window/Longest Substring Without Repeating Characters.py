def lengthOfLongestSubstring(s):
    res, l = 0, 0
    hashset = set()
    for r in range(len(s)):
        while s[r] in hashset:
            hashset.remove(s[l])
            l += 1
        hashset.add(s[r])
        res = max(res, r - l + 1)
    return res


print(lengthOfLongestSubstring("pwwkew"))
