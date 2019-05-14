package main

import (
	"encoding/json"
	"fmt"
	"time"
	// jsoniter "github.com/json-iterator/go"
)

type JSObj struct {
	Keys []string `json:"keys"`
	Pids []int    `json:"pids"`
}

func json_bench(n int) {
	// var json = jsoniter.ConfigCompatibleWithStandardLibrary

	size := 200
	keys := make([]string, size)
	pids := make([]int, size)
	for i := 0; i < size; i++ {
		keys[i] = fmt.Sprintf("key#%d", i)
		pids[i] = i + 200000
	}
	// obj := make(map[string]interface{})
	// obj["keys"] = keys
	// obj["pids"] = pids
	obj := JSObj{Keys: keys, Pids: pids}
	// fmt.Println(obj)

	var data []byte
	start := time.Now()
	for i := 0; i < n; i++ {
		data, _ = json.Marshal(&obj)
	}
	end := time.Now()
	fmt.Printf("json save = %.2f, size = %d\n", end.Sub(start).Seconds(), len(data))

	// obj2 := make(map[string]interface{})
	obj2 := JSObj{}
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
