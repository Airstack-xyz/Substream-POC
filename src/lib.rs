mod abis;
mod pb;
mod rpc;

// use num_bigint::BigInt;

use pb::token_tracker::{AirTransfers, AirTransfer, AirBlock, AirAccount, TransferCall, TransferCalls};
use substreams::store;
use substreams_ethereum::Function;
use substreams::{log, Hex, proto};
use substreams::errors::Error;
use substreams_ethereum::{pb::eth::v2 as eth, Event as EventTrait};

#[substreams::handlers::map]
fn map_erc20_transfer(blk: eth::Block) -> Result<AirTransfers, Error> {
    let mut air_transfers = vec![];
    for log in blk.logs(){
        if let Some(event) = abis::ERC20::events::Transfer::match_and_decode(log){
            log::info!("transfer event: {}", Hex(&event.to));
            log::info!("token: {}", Hex(log.log.clone().address));
            // let wallet_balance_data = hex::decode("18160ddd").unwrap();
            // log::info!()
            // log::info!(log.to_string());

            let mut blockRecord: AirBlock = AirBlock{
                hash: blk.clone().hash,
                number: blk.clone().number,
                timestamp: blk.clone()
                .header
                .as_ref()
                .unwrap()
                .timestamp
                .as_ref()
                .unwrap()
                .seconds
                .to_string(),
            };

            // let sender_balance: BigInt = rpc::get_wallet_balance(&Hex(&event.from).to_string());
            // log::info!("Sender_balance: {}", sender_balance);

            let mut air_transfer: AirTransfer = AirTransfer{
                amount: event.value.low_u64(),
                token_address: Hex(log.log.clone().address).to_string(),
                hash: log.receipt.transaction.hash.clone(),
                from: Hex(event.from).to_string(),
                to: Hex(event.to).to_string(),
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
fn map_erc20_calldata(blk: eth::Block) -> Result<TransferCalls, Error>{
    let mut transfer_calls = vec![];
    for trx in blk.transaction_traces{
        // log::info!("transaction address: {}", Hex(trx.hash));
        if trx.status != 1{
            continue;
        }
        for call in trx.calls{
            let mut transaction_address= String::new();
            if let Some(transfer) = abis::ERC20::functions::Transfer::match_and_decode(&call){
                // log::info!("transfer data: {:?}", &transfer.value);
                let mut transferCall: TransferCall = TransferCall{
                    receiver: Hex(&transfer.to).to_string(),
                    value: transfer.value.to_string(),
                };
                transaction_address = Hex(&trx.hash).to_string();
                // log::info!("Transaction address: {}", transaction_address);
                transfer_calls.push(transferCall);
            }
            // log::info!("Transaction address outside: {}", transaction_address);
            if Hex(&trx.hash).to_string() == transaction_address && &call.call_type.to_string() == "1" && &call.parent_index.to_string() == "0"{
                log::info!("transaction address: {:?}", transaction_address);
                log::info!("call address: {}", Hex(&call.address).to_string());
                // log::info!("call logs: {:?}", &call.logs);
                log::info!("call caller: {}", Hex(&call.caller));
                // log::info!("call caller: {}", Hex(&call.));
                log::info!("call parent index: {}", &call.parent_index);
                // log::info!("call status failed: {}", &call.status_failed);
                // log::info!("call status failed: {}", &call.sta);
            }
        }
    }
    Ok(TransferCalls{transfer_calls})
}

fn generate_key(holder: &Vec<u8>) -> String{
    return format!("{}", Hex(holder));
}