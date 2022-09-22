use anyhow::{Ok, Result};
use substreams_ethereum::Abigen;

fn main() -> Result<(), anyhow::Error> {
    Abigen::new("ERC20", "abis/ERC20.json")?
        .generate()?
        .write_to_file("src/abis/ERC20.rs")?;

    Ok(())
}