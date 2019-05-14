package zigzag_conversion

import (
	"bytes"
	"sort"
)

type Char struct {
	r, c int
	ch   byte
}
type Chars []Char

func (self Chars) Len() int {
	return len(self)
}
func (self Chars) Less(i, j int) bool {
	if self[i].r == self[j].r {
		return self[i].c < self[j].c
	}
	return self[i].r < self[j].r
}

func (self Chars) Swap(i, j int) {
	self[i], self[j] = self[j], self[i]
}

func convert(s string, numRows int) string {
	// 很难纳入到下面的逻辑里面
	if numRows == 1 {
		return s
	}
	temp := make(Chars, len(s))
	r, c, down := 0, 0, true
	for i := 0; i < len(s); i++ {
		// fmt.Printf("r, c= %d, %d\n", r, c)
		ch := s[i]
		temp[i] = Char{r: r, c: c, ch: ch}

		if down {
			if r == (numRows - 1) {
				r -= 1
				c += 1
				down = false
			} else {
				r += 1
			}
		} else {
			if r == 0 {
				r = 1
				down = true
			} else {
				r -= 1
				c += 1
			}
		}

	}
	sort.Sort(temp)
	// fmt.Println(temp)
	buffer := bytes.Buffer{}
	for _, ch := range temp {
		buffer.WriteByte(ch.ch)
	}
	return buffer.String()
}
