package helloworld

const (
	Pi = 3.1415926
)

func Add(x, y int) int {
	return x + y
}

func Fib(x int) int {
	if x <= 1 {
		return x
	}
	a, b := 0, 1
	for i := 1; i < x; i++ {
		a, b = b, a+b
	}
	return b
}
