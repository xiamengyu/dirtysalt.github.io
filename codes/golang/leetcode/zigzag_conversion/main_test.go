package zigzag_conversion

import (
	"testing"
)

type Params struct {
	s    string
	rows int
	exp  string
}

func TestConvert(t *testing.T) {
	cases := []Params{
		Params{s: "PAYPALISHIRING", rows: 3, exp: "PAHNAPLSIIGYIR"},
		Params{"PAYPALISHIRING",1,"PAYPALISHIRING"},
		Params{s: "AB", rows: 1, exp: "AB"},
	}

	for _, c := range cases {
		res := convert(c.s, c.rows)
		if res != c.exp {
			t.Errorf("case %v failed. res = %s", c, res)
		}
	}
}
