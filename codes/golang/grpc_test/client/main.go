package main

import (
	"context"
	"flag"
	"fmt"
	pb "golang/grpc_test/hello"
	"log"
	"time"

	"google.golang.org/grpc"
)

func main() {
	var serverAddr = flag.String("server_addr", "127.0.0.1:10000", "The server address in the format of host:port")
	flag.Parse()
	var opts []grpc.DialOption
	opts = append(opts, grpc.WithInsecure())
	conn, err := grpc.Dial(*serverAddr, opts...)
	if err != nil {
		log.Fatalf("fail to dial: %v", err)
	}
	defer conn.Close()

	for i := 0; i < 10; i++ {
		ctx, cancel := context.WithTimeout(context.Background(), 1*time.Second)
		defer cancel()
		client := pb.NewGreeterClient(conn)
		req := &pb.HelloRequest{Name: fmt.Sprintf("Person#%d", i)}
		resp, err := client.SayHello(ctx, req)
		if err != nil {
			log.Fatal("request failed")
		} else {
			log.Println(resp.Message)
		}
	}
}
