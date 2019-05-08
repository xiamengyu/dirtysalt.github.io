package helloworld

import "testing"

func TestFib(t *testing.T) {
	if Fib(0) != 0 {
		t.Error("0 failed")
	}
	if Fib(1) != 1 {
		t.Error("1 failed")
	}
	if Fib(3) != 2 {
		t.Error("3 failed")
	}
}
