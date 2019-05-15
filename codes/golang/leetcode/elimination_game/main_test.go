package elimination_game


import (
	"testing"
)

type Params struct {
	n int
	exp int
}

func TestLastRemaining(t *testing.T) {

	cases := []Params{
		Params{n:1, exp:1},
		Params{n:9, exp:6},
		Params{n:2, exp:2},
		Params{n:3, exp:2},
		Params{n:4, exp:2},
		Params{n:6, exp:4},
	}

	for _, c := range cases {
		res := lastRemaining(c.n)
		if res != c.exp {
			t.Errorf("case %v failed. res = %v", c, res)
		}
	}

	// for i:=1;i<100;i++ {
	// 	lastRemaining(i)
	// }
}
