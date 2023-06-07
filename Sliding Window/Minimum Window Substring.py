def minWindow(s, t):
    if t == "":
        return t

    window, needed = {}, {}
    for c in t:
        needed[c] = needed.get(c, 0) + 1

    have, need = 0, len(needed)
    res, resLen = [-1, -1], float("infinity")
    l = 0
    for r in range(len(s)):
        window[s[r]] = 1 + window.get(s[r], 0)
        if s[r] in needed and window[s[r]] == needed[s[r]]:
            have += 1

        while have == need:
            if r - l + 1 < resLen:
                resLen = r - l + 1
                res = [l, r]
            window[s[l]] -= 1
            if s[l] in needed and window[s[l]] < needed[s[l]]:
                have -= 1
            l += 1
    i, j = res
    return s[i:j + 1] if resLen != float("infinity") else ""