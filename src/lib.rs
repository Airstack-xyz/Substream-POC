mod abis;
mod pb;

use pb::token_tracker::{AirTransfers, AirTransfer, AirBlock, AirAccount};
use substreams::{log, store, Hex};
use substreams::errors::Error;
use substreams_ethereum::{pb::eth::v2 as eth, Event as EventTrait};

#[substreams::handlers::map]
fn map_erc20_transfer(blk: eth::Block) -> Result<AirTransfers, Error> {
    let mut air_transfers = vec![];
    for log in blk.logs(){
        if let Some(event) = abis::ERC20::events::Transfer::match_and_decode(log){
            log::info!("transfer event: {}", Hex(&event.to));
            log::info!("token: {}", Hex(log.log.clone().address));
            // log::info!(log.to_string());

            // let mut blockRecord: AirBlock = AirBlock{
            //     hash: blk.hash,
            //     number: blk.number,
            //     timestamp: blk
            //     .header
            //     .as_ref()
            //     .unwrap()
            //     .timestamp
            //     .as_ref()
            //     .unwrap()
            //     .seconds
            //     .to_string(),
            // };

            // let fromAddress = match std::str::from_utf8(&event.from) {
            //     Ok(s) => s,
            //     Err(e) => panic!("Invalid UTF-8 sequence: {}", e),
            // };
            // let toAddress = match std::str::from_utf8(&event.to) {
            //     Ok(s) => s,
            //     Err(e) => panic!("Invalid UTF-8 sequence: {}", e),
            // };
    
            let mut air_transfer: AirTransfer = AirTransfer{
                amount: event.value.low_u64(),
                token_address: Hex(log.log.clone().address).to_string(),
                hash: log.receipt.transaction.hash.clone(),
                from: Hex(event.from).to_string(),
                to: Hex(event.to).to_string(),
                ..Default::default()
            };
    
            air_transfers.push(air_transfer);
        }
    }
    Ok(AirTransfers{ air_transfers })
}