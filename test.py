from web3 import Web3
from decimal import Decimal
from functions import *
from hexbytes import HexBytes
from multiprocessing.dummy import Pool

def bridge():
    with open('wallets.txt', 'r') as f:
        private_keys = f.read().splitlines()
    wallets = my_wallet_func(private_keys)
    for wallet in wallets:
        user_info = {
            'amount': 0.0051,
            'currency': 'eth',
            'trx_count': 10,
            'chain_from': 'nova',
            'code': 'optimism',
            'wallet': wallet,
        }
    wallet = user_info['wallet']
    provider_info = get_current_provider('nova')
    web3 = Web3(Web3.HTTPProvider('https://nova.arbitrum.io/rpc'))
    print(provider_info['rpc'])
    code = network_code[user_info['code']]
    nonce = web3.eth.get_transaction_count(wallet['wallet'].address)
    print(web3.eth.get_transaction_count(wallet['wallet'].address))
    gas = web3.eth.gas_price
    print(gas)
    wallet_balance = web3.eth.get_balance(wallet['wallet'].address)/10**18
    wallet_address = wallet['wallet'].address
    user_info['balance'] = wallet_balance
    user_info['address'] = wallet_address
    gas_limit = get_gas_limit('nova')
    print(gas_limit)
    eth_amount = web3.from_wei(gas * gas_limit ,'ether')
    print(eth_amount * user_info['trx_count'])
    tx = {}

    eth_value = web3.to_wei(Decimal(user_info['amount']) , 'ether') // 10000 * 10000 + code



    match user_info['chain_from']:
        case 'ethereum':
            match user_info['currency']:
                case 'eth':
                    tx = {'nonce': nonce, 
                          'to': HexBytes(eth_orbiter), 
                          'value': eth_value,   
                          'gas': 21000, 
                          'gasPrice': gas }    
        case 'arbitrum':
            match user_info['currency']:
                case 'eth': 
                    tx = {'nonce': nonce, 
                          'to': HexBytes(eth_orbiter), 
                          'value': eth_value, 
                          'gas': 200000, 
                          'gasPrice': gas } 
        case 'optimism':
            match user_info['currency']:
                case 'eth':
                    tx = {'nonce': nonce, 
                          'to': HexBytes('eth_orbiter'), 
                          'value': eth_value, 
                          'gas': 100000, 
                          'gasPrice': gas }
        case 'nova':
            match user_info['currency']:
                case 'eth':
                    tx = {'nonce': nonce, 
                          'to': HexBytes(eth_orbiter), 
                          'value': eth_value, 
                          'gas': 100000, 
                          'gasPrice': gas }   
                    
    

    #signed_tx = web3.eth.account.sign_transaction(tx, wallet['wallet'].key)
    #tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    #print(web3.to_hex(tx_hash))

bridge()