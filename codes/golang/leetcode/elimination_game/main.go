package elimination_game

func forward(val int, bits uint, n int) int {
	rem := (n - val) / (1 << bits)
	// fmt.Println(val, bits, n, rem)
	return rem*(1<<bits) + val
}

func lastRemaining(n int) int {
	if n == 1 {
		return 1
	}
	val := 0
	var bits uint = 1
	var res int
	for {
		// fmt.Println(">>>", val, bits)
		x := forward(val, bits, n)
		if ((x >> bits) & 1) == 1 {
			res = x
			break
		}
		val = ((1 - ((x >> bits) & 1)) << bits) + val
		if val > n {
			res = x
			break
		}
		bits = bits + 1
		// fmt.Println("<<<", x, val, bits)
	}
	return res
}
