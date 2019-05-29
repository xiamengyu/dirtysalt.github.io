package patching_array

import "testing"

type Params struct {
	nums []int
	n int
	exp int
}

func TestMinPatches(t *testing.T) {

	cases := []Params{
		{nums: []int{1,3},  n:6, exp:1},
		{nums: []int{1,5,10}, n:20, exp:2},
		{nums:[]int{1,2,2}, n:5, exp:0},
	}

	for _, c := range cases {
		res := minPatches(c.nums, c.n)
		if res != c.exp {
			t.Errorf("case %v failed. res = %v", c, res)
		}
	}
}
