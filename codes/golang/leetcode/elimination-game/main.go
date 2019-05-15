package elimination_game

func lastRemaining(n int) int {
	var res int = 0
	var bit uint32 = 0
	for ; n != 0; n = n >> 1 {
		res = res + ((1 - (n & 1)) << bit)
		bit += 1
	}
	return res
}
