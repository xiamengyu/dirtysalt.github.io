gen_proto:
	mkdir -p hello
	protoc -I. hello.proto --go_out=plugins=grpc:hello

run_client:
	go run client/main.go --server_addr localhost:10002

run_server:
	go run server/main.go --port 10002