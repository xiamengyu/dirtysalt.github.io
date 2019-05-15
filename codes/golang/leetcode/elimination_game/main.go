package elimination_game

type State struct {
	n        int
	val      int
	trailing int
	bits     uint
}

func (s *State) next() {
	bit := (s.val >> s.bits) & 1
	trailing := ((1 - bit) << s.bits) + s.trailing
	s.bits += 1
	s.trailing = trailing
}

func (s *State) smallest() int {
	if s.trailing == 0 {
		return s.trailing + (1 << s.bits)
	} else {
		return s.trailing
	}
}

func (s *State) largest() int {
	if s.trailing <= s.n {
		x := ((s.n - s.trailing) / (1 << s.bits)) * (1 << s.bits)
		return x + s.trailing
	} else {
		return 0 // you have to break
	}
}

func lastRemaining(n int) int {
	s := State{n: n, val: 1, trailing: 0, bits: 0}
	for {
		s.next()
		val := s.largest()
		// log.Printf("->max, s = %v, val = %d", s, val)
		if val <= s.val {
			break
		}
		s.val = val
		s.next()
		val = s.smallest()
		// log.Printf("->min, s = %v, val = %d", s, val)
		if val >= s.val || val <= 0 {
			break
		}
		s.val = val
	}
	return s.val
}
