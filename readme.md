# Steps to run the substream in terminal

## Download all the dependencies
Use this doc to download and install all the dependencies required to run this substream - https://substreams.streamingfast.io/developer-guide/installation-requirements

## Setting up the env
For getting the block data we are using the substream API "api-dev.streaming-fast.io:443" which is using their particular hosted firehose. For accessing the API we need the streaming-fast token which you can get following this doc https://substreams.streamingfast.io/reference-and-specs/authentication

Once you have setup the SUBSTREAMS_API_TOKEN, you are good to run the substream.

## Running the substreams
Just move to the root directory of your substream folder and run this command

`
substreams run -e api-dev.streamingfast.io:443 \
   substreams.yaml \
   map_erc20_transfer,store_transfers \
   --start-block 12369621 \
   --stop-block 20000000
`