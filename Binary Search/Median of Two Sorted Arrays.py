def findMedianSortedArrays(nums1, nums2):
    A, B = nums1, nums2
    total = len(A) + len(B)
    half = total // 2

    if len(A) > len(B):
        A, B = B, A
    print(A, B)
    l, r = 0, len(A) - 1
    while True:
        Amid = l + (r - l) // 2
        Bmid = half - Amid - 2
        #print(Amid, Bmid)
        Aleft = A[Amid] if Amid >= 0 else float("-infinity")
        Aright = A[Amid + 1] if Amid + 1 < len(A) else float("infinity")
        Bleft = B[Bmid] if Bmid >= 0 else float("-infinity")
        Bright = B[Bmid + 1] if Bmid + 1 < len(B) else float("infinity")

        if Aleft <= Bright and Aright >= Bleft:
            if total % 2:
                return min(Aright, Bright)
            else:
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
        else:
            if Aright < Bleft:
                l = Amid + 1
            elif Bright < Aleft:
                r = Amid - 1