def checkInclusion(s1, s2):
    if len(s1) > len(s2):
        return False

    counts1, counts2 = [0] * 26, [0] * 26
    for i in range(len(s1)):
        counts1[ord(s1[i]) - ord("a")] += 1
        counts2[ord(s2[i]) - ord("a")] += 1

    matches = 0
    for m in range(26):
        if counts1[m] == counts2[m]:
            matches += 1

    l, r = 0, len(s1)
    while matches < 26 and r < len(s2):
        idxR = ord(s2[r]) - ord("a")
        counts2[idxR] += 1
        if counts2[idxR] == counts1[idxR]:
            matches += 1
        elif counts2[idxR] - 1 == counts1[idxR]:
            matches -= 1

        idxL = ord(s2[l]) - ord("a")
        counts2[idxL] -= 1
        if counts2[idxL] == counts1[idxL]:
            matches += 1
        elif counts2[idxL] + 1 == counts1[idxL]:
            matches -= 1
        l += 1
        r += 1
    return matches == 26