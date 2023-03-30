from web3 import Web3
from decimal import Decimal
from functions import *
from hexbytes import HexBytes
from multiprocessing.dummy import Pool

import math


def bridge(user_info):
    wallet = user_info['wallet']
    provider_info = get_current_provider(user_info['chain_from'])
    web3 = Web3(Web3.HTTPProvider(provider_info['rpc']))
    code = network_code[user_info['code']]

    nonce = web3.eth.get_transaction_count(wallet['wallet'].address)


    gas = web3.eth.gas_price
    gas_limit = get_gas_limit(user_info['chain_from'])
    total_transaction_gas_fees = web3.from_wei(Decimal(gas) * Decimal(gas_limit), 'ether')

    
    wallet_balance = web3.eth.get_balance(wallet['wallet'].address)
    wallet_address = wallet['wallet'].address

    user_info['balance'] = wallet_balance
    user_info['address'] = wallet_address
    user_info['total_transaction_gas_fees'] = total_transaction_gas_fees

    tx = {}
    
    eth_value = web3.to_wei((Decimal(user_info['amount'])) + total_transaction_gas_fees, 'ether')// 10000 * 10000 + code

    if bridge_check(user_info) == 0:
        return 0
        

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
                          'gas': 500000, 
                          'gasPrice': gas } 
        case 'optimism':
            match user_info['currency']:
                case 'eth':
                        tx = {'nonce': nonce, 
                          'to': HexBytes(eth_orbiter), 
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
    signed_tx = web3.eth.account.sign_transaction(tx, wallet['wallet'].key)
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    print(web3.to_hex(tx_hash))



if (__name__ == "__main__"):
    with open('wallets.txt', 'r') as f:
        private_keys = f.read().splitlines()
    wallets = my_wallet_func(private_keys)
    currency = ask_currency()
    chain_from, chain_to = network_choose(currency)
    trx_count = ask_transaction_count()
    amount = ask_amount(currency, chain_from, chain_to) 
    trx_cost = (amount + 0.003 * amount + token_fees[currency][chain_to]['withholding_fee']) 
    total_trxs_cost = trx_cost * trx_count


    print(token_fees[currency][chain_to]['withholding_fee'])
    print('CHAIN FROM -> ', chain_from, '\nDESTINATION -> ', chain_to)
    print ('Quantity of transactions:', trx_count)
    print ('The currency is set to:', currency)
    print ('One transaction cost:',  trx_cost, '\nTotal:', trx_cost * trx_count)
    print ('TRANSACTION COST IS ESTIMATED AND IT MAY BE BIGGER OR LOWER')

    
    threads = 1
    pool = Pool(threads)
    collections_user_info = []

    
    for wallet in wallets:
        user_info = {
            'amount': trx_cost,
            'currency': currency,
            'trx_count': trx_count,
            'chain_from': chain_from,
            'code': chain_to,
            'chain_to': chain_to,
            'wallet': wallet,
            'total_trxs_cost' : total_trxs_cost,
        }
        collections_user_info.append(user_info)

    pool.map(bridge, collections_user_info)


    