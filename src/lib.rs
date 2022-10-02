mod abis;
mod pb;
mod rpc;

use pb::token_tracker::{AirTransfers, AirTransfer};
use substreams::store;
use substreams::{log, Hex, proto};
use substreams::errors::Error;
use substreams_ethereum::{pb::eth::v2 as eth, Event as EventTrait};

#[substreams::handlers::map]
fn map_erc20_transfer(blk: eth::Block) -> Result<AirTransfers, Error> {
    let mut air_transfers = vec![];
    for log in blk.logs(){
        if let Some(event) = abis::erc20::events::Transfer::match_and_decode(log){
            log::info!("transfer event: {}", Hex(&event.to));
            log::info!("token: {}", Hex(log.log.clone().address));

            let air_transfer: AirTransfer = AirTransfer{
                amount: event.value.low_u64(),
                token_address: Hex(log.log.clone().address).to_string(),
                hash: log.receipt.transaction.hash.clone(),
                from: Hex(event.from).to_string(),
                to: Hex(event.to).to_string(),
                block_number: blk.clone().number,
                timestamp: blk.clone()
                .header
                .as_ref()
                .unwrap()
                .timestamp
                .as_ref()
                .unwrap()
                .seconds
                .to_string(),
                log_ordinal: log.ordinal(),
                ..Default::default()
            };
    
            air_transfers.push(air_transfer);
        }
    }
    Ok(AirTransfers{ air_transfers })
}

#[substreams::handlers::store]
fn store_transfers(transfers: AirTransfers, output: store::StoreSet){
    for transfer in transfers.air_transfers{
        output.set(
            transfer.log_ordinal,
            generate_key(&transfer.hash),
            &proto::encode(&transfer).unwrap(),
        );
    }    
}

#[substreams::handlers::map]
fn map_erc721_transfer(blk: eth::Block) -> Result<AirTransfers, Error>{
    let mut air_transfers = vec![];
    for log in blk.logs(){
        if let Some(event) = abis::erc721::events::Transfer::match_and_decode(log){
            log::info!("transfer event: {}", Hex(&event.to));
            // log::info!("token: {}", Hex(log.log.clone().address));
            let air_transfer: AirTransfer = AirTransfer{
                amount: 1,
                token_address: event.token_id.to_string(),
                hash: log.receipt.transaction.hash.clone(),
                from: Hex(event.from).to_string(),
                to: Hex(event.to).to_string(),
                block_number: blk.clone().number,
                timestamp: blk.clone()
                .header
                .as_ref()
                .unwrap()
                .timestamp
                .as_ref()
                .unwrap()
                .seconds
                .to_string(),
                log_ordinal: log.ordinal(),
                ..Default::default()
            };
            air_transfers.push(air_transfer);
        }
    }
    Ok(AirTransfers{ air_transfers})
}

fn generate_key(holder: &Vec<u8>) -> String{
    return format!("{}", Hex(holder));
}