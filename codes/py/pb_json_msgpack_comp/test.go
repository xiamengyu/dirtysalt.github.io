package main

import (
	"fmt"
	"time"

	jsoniter "github.com/json-iterator/go"
)

func json_bench(n int) {
	var json = jsoniter.ConfigCompatibleWithStandardLibrary

	size := 200
	keys := make([]string, size)
	pids := make([]int, size)
	for i := 0; i < size; i++ {
		keys[i] = fmt.Sprintf("key#%d", i)
		pids[i] = i + 200000
	}
	obj := make(map[string]interface{})
	obj["keys"] = keys
	obj["pids"] = pids

	var data []byte
	start := time.Now()
	for i := 0; i < n; i++ {
		data, _ = json.Marshal(obj)
	}
	end := time.Now()
	fmt.Printf("json save = %.2f, size = %d\n", end.Sub(start).Seconds(), len(data))

	obj2 := make(map[string]interface{})
	start = time.Now()
	for i := 0; i < n; i++ {
		json.Unmarshal(data, &obj2)
	}
	end = time.Now()
	fmt.Printf("json load = %.2f\n", end.Sub(start).Seconds())
	// fmt.Println(obj2)
}

func main() {
	const N = 10000
	json_bench(N)
}
