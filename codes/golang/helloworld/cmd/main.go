package main

import "fmt"
import "helloworld"

func main() {
	fmt.Println(helloworld.Pi)
	for i := 0; i < 10; i++ {
		fmt.Printf("Fib(%d) = %d\n", i, helloworld.Fib(i))
	}
}
