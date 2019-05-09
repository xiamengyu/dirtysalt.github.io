package main

import (
	"context"
	"flag"
	"fmt"
	pb "grpc_test/hello"
	"log"
	"net"

	"google.golang.org/grpc"
)

type  MyGreetServer struct {

}
func (self MyGreetServer) SayHello(ctx context.Context, in *pb.HelloRequest) (*pb.HelloReply, error) {
	return &pb.HelloReply{Message: "Hello again " + in.Name}, nil
}


func main() {
	var port = flag.Int("port", 10000, "runnig port")
	flag.Parse()
	lis, err := net.Listen("tcp", fmt.Sprintf("localhost:%d", *port))
	if err != nil {
		log.Fatalf("failed to listen: %v", err)
	}
	grpcServer := grpc.NewServer()
	server := MyGreetServer{}
	pb.RegisterGreeterServer(grpcServer, server)
	log.Printf("listen on %v\n", lis.Addr())
	grpcServer.Serve(lis)
}
