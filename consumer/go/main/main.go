package main

import (
	"context"
	"fmt"
	"io"
	"os"

	"github.com/streamingfast/substreams/client"
	"github.com/streamingfast/substreams/manifest"
	pbsubstreams "github.com/streamingfast/substreams/pb/sf/substreams/v1"
	"google.golang.org/grpc"
)

var jwt_token string
var endpoint string

func main() {
	jwt_token := os.Getenv("SUBSTREAMS_API_TOKEN")
	if len(jwt_token) == 0 {
		fmt.Printf("SUBSTREAMS_API_TOKEN not set")
	}
	endpoint = "api.streamingfast.io:443"
	package_pb := "../all-token-tracker-v0.1.0.spkg"
	output_modules := []string{"map_erc20_transfer", "store_transfers"}
	start_block := 12369621
	end_block := 12369800

	manifestReader := manifest.NewReader(package_pb)
	pkg, err := manifestReader.Read()
	if err != nil {
		fmt.Printf("read manifest %q: %w", package_pb, err)
	}

	client, callOpts := substreams_service()
	fmt.Println(client)
	req := &pbsubstreams.Request{
		StartBlockNum: int64(start_block),
		StopBlockNum:  uint64(end_block),
		ForkSteps:     []pbsubstreams.ForkStep{pbsubstreams.ForkStep_STEP_IRREVERSIBLE},
		Modules:       pkg.Modules,
		OutputModules: output_modules,
	}
	fmt.Println("hello")
	// ctx, _ := context.WithTimeout(context.Background(), 5*time.Second)
	stream, err := client.Blocks(context.Background(), req, callOpts...)
	fmt.Println(stream)
	if err != nil {
		fmt.Printf("call sf.substreams.v1.Stream/Blocks: %w", err)
	}

	for {
		resp, err := stream.Recv()
		fmt.Println(resp)
		if err != nil {
			if err == io.EOF {
				fmt.Printf("Error occured")
			}
			fmt.Printf("Error occured in receiving a package: %w", err)
		}
		fmt.Println(resp.Message)
		switch r := resp.Message.(type) {
		case *pbsubstreams.Response_Progress:
			_ = r.Progress
		case *pbsubstreams.Response_SnapshotData:
			_ = r.SnapshotData
		case *pbsubstreams.Response_SnapshotComplete:
			_ = r.SnapshotComplete
		case *pbsubstreams.Response_Data:

			for _, output := range r.Data.Outputs {
				fmt.Printf("Something")
				for _, log := range output.Logs {
					fmt.Println("LOG: ", log)
				}
				fmt.Println(output)
				// if output.Name == "db_out" {
				// 	if err := loader.ReturnHandler(output.GetMapOutput().GetValue(), r.Data.Step, r.Data.Cursor, r.Data.Clock); err != nil {
				// 		fmt.Printf("RETURN HANDLER ERROR: %s\n", err)
				// 	}
				// }
			}
		}
	}

}

func substreams_service() (pbsubstreams.StreamClient, []grpc.CallOption) {
	ssClient, _, callOpts, err := client.NewSubstreamsClient(
		endpoint, jwt_token, true, false,
	)
	// fmt.Println(err)
	if err != nil {
		fmt.Printf("Substreams client setup: %w", err)
	}

	return ssClient, callOpts
}
