#!/usr/bin/env python
# coding:utf-8
# Copyright (C) dirlt
from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        C = {}
        nums.sort()

        def mp(k, n):
            if n == 0:
                return 0

            while k >= 0 and nums[k] > n:
                k -= 1

            if k == -1:
                return n

            key = '{}-{}'.format(k, n)
            if key in C:
                return C[key]

            # 可以使用nums[k], 也可以不使用
            res = min(mp(k - 1, n), mp(k - 1, n - nums[k]))

            while n > 1:
                res = max(res, mp(k, n - 1))
                n -= 1

            C[key] = res
            return res

        k = len(nums) - 1
        res = mp(k, n)
        return res


def test():
    cases = [
        ([1, 3], 6, 1),
        ([1, 5, 10], 20, 2)
    ]
    sol = Solution()
    ok = True
    for c in cases:
        (nums, n, exp) = c
        res = sol.minPatches(nums, n)
        if res != exp:
            print('case failed. {}, out = {}'.format(c, res))
            ok = False
    if ok:
        print('cases passed!!!')


if __name__ == '__main__':
    test()
