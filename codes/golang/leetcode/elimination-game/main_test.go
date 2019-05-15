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
		Params{n:9, exp:6},
		Params{n:2, exp:2},
	}

	for _, c := range cases {
		res := lastRemaining(c.n)
		if res != c.exp {
			t.Errorf("case %v failed. res = %v", c, res)
		}
	}
}
