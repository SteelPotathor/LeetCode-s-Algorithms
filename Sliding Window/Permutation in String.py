def checkInclusion(s1, s2):
    if len(s1) > len(s2):
        return False

    map, res = {}, {}

    for c in s1:
        map[c] = map.get(c, 0) + 1

    l, r, cnt = 0, 0, 0
    while r < len(s2) and map != res:
        if s2[r] in map:
            res[s2[r]] = res.get(s2[r], 0) + 1
            cnt += 1
            r += 1
            if cnt == len(s1) + 1:
                cnt -= 1
                if res[s2[l]] <= 1:
                    res.pop(s2[l])
                else:
                    res[s2[l]] -= 1
                l += 1
        else:
            r += 1
            l = r
            cnt = 0
            res.clear()
        print(res, cnt, len(s1))
    return map == res