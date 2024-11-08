from web3 import Web3
from datetime import datetime
from typing import Set, Dict, List, Any
from decimal import Decimal

def get_latest_block() -> Dict[str, Any]:
    """
    Get real time block data from the Base Sepolia network, including all addresses involved in transactions
    and total value transferred.
    
    This function MUST be called every time in order to receive the latest block information.
    """
    # Connect to Base Sepolia network
    base_sepolia_rpc = "https://sepolia.base.org"
    w3 = Web3(Web3.HTTPProvider(base_sepolia_rpc))
    
    # Check connection
    if not w3.is_connected():
        raise Exception("Failed to connect to Base Sepolia network")

    # Get latest block
    latest_block = w3.eth.get_block('latest', full_transactions=True)
    
    # Initialize sets to store unique addresses and total value
    sender_addresses: Set[str] = set()
    receiver_addresses: Set[str] = set()
    total_value_eth: Decimal = Decimal('0')
    
    # Process all transactions in the block
    transactions_data: List[Dict[str, Any]] = []
    
    for tx in latest_block.transactions:
        # Add sender address
        sender_addresses.add(tx["from"])
        
        # Add receiver address if it exists
        if tx["to"]:
            receiver_addresses.add(tx["to"])

        # Convert value to ETH and add to total
        tx_value_eth = Decimal(str(w3.from_wei(tx["value"], 'ether')))
        total_value_eth += tx_value_eth
        
        # Store transaction data
        tx_data = {
            "hash": tx.hash.hex(),
            "from": tx["from"],
            "to": tx["to"] if tx["to"] else "Contract Creation",
            "value": tx_value_eth,
            "gas_price": w3.from_wei(tx["gasPrice"], 'gwei') if "gasPrice" in tx else None,
            "gas": tx["gas"]
        }
        transactions_data.append(tx_data)
    
    # Compile block data
    block_data = {
        "block_number": latest_block.number,
        "timestamp": datetime.fromtimestamp(latest_block.timestamp).strftime('%Y-%m-%d %H:%M:%S'),
        "hash": latest_block.hash.hex(),
        "transactions_count": len(latest_block.transactions),
        "total_value_transferred": float(total_value_eth),
        "address_summary": {
            "unique_senders": list(sender_addresses),
            "unique_receivers": list(receiver_addresses),
            "total_unique_addresses": len(sender_addresses.union(receiver_addresses))
        }
    }
    
    return block_data