def longestConsecutive(nums):
    s = set(nums)
    longest = 1

    for n in s:
        if n - 1 not in s:
            length = 1
            while n + length in s:
                length += 1
            longest = max(length, longest)
    return longest