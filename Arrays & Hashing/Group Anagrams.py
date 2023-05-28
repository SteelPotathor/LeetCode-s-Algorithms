import collections


def groupAnagrams(strs):
    dict = collections.defaultdict(list)
    for s in strs:
        count = [0 for i in range(26)]
        for c in s:
            count[ord(c) - ord("a")] += 1
        dict[tuple(count)].append(s)
    return dict.values()
