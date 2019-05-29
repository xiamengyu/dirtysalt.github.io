package patching_array

import (
	"sort"
	"fmt"
)

func minPatches(nums []int, n int) int {
	sort.Ints(nums)

	k, size, value := 0, len(nums), 1

	res := make([]int, 0)

	if k < size && nums[k] == 1 {
		k += 1
	} else {
		res = append(res, 1)
	}

	for ; value < n ; {
		if k < size {
			v := nums[k]
			if v > (value + 1) {
				res = append(res, value + 1)
				value = 2 * value + 1
			} else {
				value += v
				k += 1
			}
		} else {
			res = append(res, value + 1)
			value = 2 * value + 1
		}
	}
	fmt.Printf("res = %v\n", res)
	return len(res)
}